# -*- coding:utf-8 -*-
import regex
import os.path

class OrtographicSegmenter(object):
    '''This is the segmenter that segments an OrtographicText into
    OrtographicSentences. It consists of a very simple model and algorithm:
      step 1) match the text for possible segment splits using regular
              expression rules given in the seg_possible_list
      step 2) narrow the possibilities down by matching with the regular
              expression rules given in the seg_allow_list. These rules have
              to parts, one that is matched against the previous segment, and
              another that is matched against a span of 100 chars from the
              possible new segment start.
      step 3) optional: if matched against an allowing rule, check for forcing
              rules that narrow the allowing rule even further'''
    
    def __init__(self, parent = None,
                 possible_list_filename='possible_list.txt',
                 allowed_list_filename='allowed_list.txt',
                 force_list_filename=None):
        '''Initializes the segmenter, if no rule list filenames are given,
        defaults are used (very Estonian specific).'''
        self.__parent = parent
        self._data_folder_path = os.path.dirname(os.path.abspath(__file__))
        self._data_folder_path = os.path.join(self._data_folder_path, 'data')
        
        self._possible_list_filename = os.path.join(self._data_folder_path,
                                                    possible_list_filename)
        self._reload_possible_list_file()
        
        self._allowed_list_filename = os.path.join(self._data_folder_path,
                                                    allowed_list_filename)
        self._reload_allowed_list_file()

#   __seg_possible_list: List
#   __seg_allow_list: List of tuples
#   __seg_force_list: dictionary with tuple as key

    def _reload_possible_list_file(self):
        '''(Re)loads the list with rules for possible segment splits. The
        filename is given in OrtographicSegmenter.__init__, and the default
        is "./data/possible_list".

        See the __init__() and segment() function for more about the algorithm.
        ATTENTION note that verbose regexps are used.'''

        # try to open the file
        with open(self._possible_list_filename, 'r') as f:
            _filedata = f.readlines()

        # truncate old rules and load new from file
        self._possible_regexps = list()
        for i in range(len(_filedata)):
            # all lines beginning with a # are ignored
            if _filedata[i].startswith('#'):
                continue
            # all other lines will be handled as verbose regular expressions
            # so be careful with empty lines in the file!
            self._possible_regexps.append(
                regex.compile(_filedata[i], regex.VERBOSE))


    def _reload_allowed_list_file(self):
        '''(Re)loads the list with rules for non-segment borders, e.g stops
        the possible segment border being split (if not forced by a forcing
        rule specified for the stop rule. The stop rules are pairs of two rules
        of which the first is matched against the segment to the left, and the
        latter is matched against the segment to the right. The filename is
        given in the __init__, and the default file is "./data/stop_list".

        See the __init__() and segment() function for more about the algorithm.
        ATTENTION note that verbose regexps are used.'''

        with open(self._allowed_list_filename, 'r') as f:
            _filedata = f.readlines()
        
        self._allowed_regexps = list()
        _rule_left = ''
        _rule_right = ''

        for i in range(len(_filedata)):
            # rules must be specified in correct order: first left, then right
            if _filedata[i].startswith('LEFT:'):
                _rule_left = regex.compile(_filedata[i][5:], regex.VERBOSE)
            elif _filedata[i].startswith('RIGHT:'):
                _rule_right = regex.compile(_filedata[i][6:], regex.VERBOSE)
                self._allowed_regexps.append((_rule_left, _rule_right))
                _rule_left = ''
                _rule_right = ''
            else:
                # everything else is ignored
                continue
            
            
    def segment(self, text):
        '''Segments a text using rules explained in __init__
        Algorithm explained:
        for all possible segment splits
          check if an allowing rule matches previous segment end and/or
            next segment start
              if found, check if allowing rule pair has any exceptions
                in the force dictionary'''
        ret_sentences = list()
        for regexp in self._possible_regexps:
            start_char_pos = 0
            eof_char_pos = len(text)
            end_char_pos = eof_char_pos
            no_possible_match_found = False
            
            for possible_match in regexp.finditer(text):
                _new_start_char_pos = possible_match.end()
                _left_side = text[start_char_pos:possible_match.end()]
                _right_side = text[possible_match.end():]
                
                for allowed_rule in self._allowed_regexps:
                    if allowed_rule[0].search(_left_side):
                        if allowed_rule[1].match(_right_side):
                            # we found an allowing rule, thus we don't start
                            # a new sentence
                            _new_start_char_pos = start_char_pos
                if not start_char_pos == _new_start_char_pos:
                    # if we have a new starting character, we have to save the
                    # previously found sentence
                    end_char_pos = possible_match.end()
                    sentence_text = text[start_char_pos:end_char_pos]
                    matched_rule = (possible_match.re)
                    self.__parent.append_sentence(sentence_text,
                                                  start_char_pos,
                                                  end_char_pos,
                                                  matched_rule)
                                                  
                start_char_pos = _new_start_char_pos
            else:
                no_possible_match_found = True
                
            # we might have dangling sentence text here, if either 
            # 1) no possible_match was found in the text or
            # 2) no possible_match was found in the last sentence
            if no_possible_match_found: # case 1
                end_char_pos = start_char_pos
            if end_char_pos < eof_char_pos: # case 2
                sentence_text = text[end_char_pos:eof_char_pos]
                if not sentence_text.isspace():
                    matched_rule = 'dangling sentence text'
                    self.__parent.append_sentence(sentence_text,
                                                  end_char_pos,
                                                  eof_char_pos,
                                                  matched_rule)
            
        return ret_sentences


#if __name__ == "__main__":
#    tests()
