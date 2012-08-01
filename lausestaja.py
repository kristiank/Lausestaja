# -*- coding:utf-8 -*-
import regex
import os.path

class OrtographicSentence:
    '''Represents an ortographic sentence, most usually segmented as seen fit
    by the OrtographicText segmenter'''

    def __init__(self, text, pos_in_text, start_char_pos, end_char_pos):
        '''Initializes an empty ortographic sentence'''
        self._start_char_pos = start_char_pos
        self._end_char_pos = end_char_pos
        self._position_in_text = pos_in_text
        self._content_text = text
        #self._part_of_text holds the OrtographicText instance?

    def set_content_text(self, text):
        '''Sets the content text of the ortographic sentence to text'''
        self._content_text = text
    
    def get_content_text(self):
        '''Returns the content text of the ortographic sentence'''
        return self._content_text
    
#   get_coord()               -> returns (start, stop)
#   get_sentence_text(strip_ws=None)   -> returns the sentence text
#   get_pos_in_textl()             -> returns the position in original text
#   get_rule_matched()        -> returns the rule that caused the segmentation
#   merge_w_next()        -> causes the sentence to merge together w next 
#   merge_w_previous()    -> causes the sentence to merge together previous

class OrtographicText:
    '''Container for an ortographic text, which consists of a list of
    ortographic sentences. The ortographic text also has a changeable
    text segmenter, which can be used to segment an inputted text.'''
    def __init__(self, text=None):
        '''Initializes an empty text with the default segmenter.'''
        self._sentence_list = []
        self._text = text
        self._length = len(self._sentence_list)
        self._segmenter = OrtographicSegmenter()

    def get_sentence_list(self, preserve_ws=True):
        '''Returns the list of ortographic sentences, setting preserve_ws to
        False will strip whitespace of each sentence's beginning and end.'''
        return self._sentence_list

    def get_number_of_sentences(self):
        '''Returns the number of sentences currently held in the text.'''
        return len(self._sentence_list)

    def append_sentence(self, sentence_text, start_char_pos, end_char_pos):
        '''Appends an ortographic sentence with given text, first and last
        character positions. Setting preserve_ws to False will strip the
        whitespace of the sentence text.'''
        pos_in_text = self.get_number_of_sentences()
        os = OrtographicSentence(sentence_text,
                                 pos_in_text,
                                 start_char_pos,
                                 end_char_pos)
        self._sentence_list.append(os)

    def get_sentence_in_pos(self, pos):
        '''Returns the OrtographicSentence in the ordinal text position given
        e.g pos=1 returns the first sentence, 2 the second etc'''
        return self._sentence_list[pos-1]

    def segment(self, text=None):
        '''Segments the held text, if a new text is given, the old will be
        replaced!'''
        if text is not None:
            self._text = text
        self._segmenter.segment(self._text)
        

class OrtographicSegmenter:
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
    
    def __init__(self, possible_list_filename='./data/possible_list',
                 allowable_list_file=None,
                 force_list_file=None):
        '''Initializes the segmenter, if no rule list filenames are given,
        defaults are used (very Estonian specific).'''

        # if possible_list_filename is not None:
        self._possible_list_filename = possible_list_filename
        # else:
        #     self._possible_list_filename = ''
        self._reload_possible_list_file()
        #     self._possible_rules = [r'[.!?](?=\s*\m)']

        if allowable_list_file is None:
            self._allowable_rules = [r'[.]\s*(a[ ]|a[.][ ]|aasta)']
        if force_list_file is None:
            self._force_rules = None
        self._initialize_rules_from_lists()

#   __seg_possible_list: List
#   __seg_allow_list: List of tuples
#   __seg_force_list: dictionary with tuple as key

    def _reload_possible_list_file(self):
        '''(Re)loads the list with rules for possible segment splits. The
        filename is given in OrtographicSegmenter.__init__, and the default
        is "./data/possible_list".'''
        # try to open the file
        with open(self._possible_list_filename, 'r') as f:
            _filedata = f.readlines()

        # truncate old rules
        self._possible_rules = list()
        for i in range(len(_filedata)):
            # all lines beginning with a # are ignored
            if _filedata[i].startswith('#'):
                continue
            # all other lines will be handled as verbose regular expressions
            self._possible_rules.append(
                regex.compile(_filedata[i], regex.VERBOSE))
        print(self._possible_rules)


    def _initialize_rules_from_lists(self):
        '''Initializing the rules compiles the rules given in the lists into
        regular expressions lists named possible_regexps, allowable_regexps and
        force_regexps. See reload_lists() for reloading the files.
        ATTENTION note that verbose regexps are used.'''

        self._possible_regexps = list()
        for rule in self._possible_rules:
            self._possible_regexps.append(regex.compile(rule, regex.VERBOSE))
            
            
    def segment(self, text):
        '''Segments a text using rules explained in __init__
        Algorithm explained:
        for all possible segment splits
          check if an allowing rule matches previous segment end and/or
            next segment start
              if found, check if allowing rule pair has any exceptions
                in the force dictionary'''
        for regexp in self._possible_regexps:
            start = 0
            for match in regexp.finditer(text):
                #print(match.span())
                #print(match.group())
                print(text[start:match.end()])
                start = match.end()
