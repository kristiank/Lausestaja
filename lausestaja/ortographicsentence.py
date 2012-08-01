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

    def set_content_text(self, text): #DEPRECATED
        '''Sets the content text of the ortographic sentence to text'''
        self._content_text = text
    
    def get_content_text(self): #DEPRECATED
        '''Returns the content text of the ortographic sentence'''
        return self._content_text
    
    def lstrip(self, strip_pattern=r'^\s*'):
        '''Trims all whitespace away from the start of the sentence.
        Note however that this doesn't delete anything, it only moves the
        starting position of the sentence pass the whitespace to the real
        ortographic beginning of the sentence.'''
        strip = regex.match(strip_pattern, self._content_text)
        self._start_char_pos += strip.end()

    def rstrip(self, strip_pattern=r'\s*$'):
        '''Trims all whitespace away from the end of the sentence.
        Note however that this doesn't delete anything, it only moves the
        ending position of the sentence pass the whitespace to the real
        ortographic ending of the sentence.'''
        strip = regex.search(strip_pattern, self._content_text)
        self._end_char_pos -= strip.end()

    def strip(self):
        '''Trims all whitespace from the starting and ending of the sentence.
        Note however that this doesn't delete anything, only the starting and
        ending positions of the sentence are corrected.'''
        self.lstrip()
        self.rstrip()


#   get_coord()               -> returns (start, stop)
#   get_sentence_text(strip_ws=None)   -> returns the sentence text
#   get_pos_in_textl()             -> returns the position in original text
#   get_rule_matched()        -> returns the rule that caused the segmentation
#   merge_w_next()        -> causes the sentence to merge together w next 
#   merge_w_previous()    -> causes the sentence to merge together previous
