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
