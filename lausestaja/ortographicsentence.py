# -*- coding:utf-8 -*-

class OrtographicSentence:
    '''Represents an ortographic sentence, most usually segmented as seen fit
    by the OrtographicText segmenter'''

    def __init__.(self):
        '''Initializes an empty ortographic sentence'''
        self._beginning_position = None
        self._end_position = None
        self._position_in_text = None
        self._is_part_of_text = None
        self._content_text = None
#   __beginning_pos: int
#   __end_pos: int
#   __part_of_text: SentenceList
#   __position_in_text: int
#   __sentence_text: str
#
    def set_content_text(self, text, preserve_ws = True):
        '''Sets the content text of the ortographic sentence to text,
        setting preserve_ws to False will strip whitespace in both ends'''
        if not preserve_ws:
            text = text.strip()
        
        self._content_text = text
    
    def get_content_text(self, preserve_ws = True):
        '''Returns the content text of the ortographic sentence, setting
        preserve_ws to False will strip whitespace in both ends of the
        returned text'''
        if not preserve_ws:
            return self._content_text.strip()
        
        return self._content_text
    
#   get_coord()               -> returns (start, stop)
#   get_sentence_text(strip_ws=None)   -> returns the sentence text
#   get_pos_in_textl()             -> returns the position in original text
#   get_rule_matched()        -> returns the rule that caused the segmentation
#   merge_w_next()        -> causes the sentence to merge together w next 
#   merge_w_previous()    -> causes the sentence to merge together previous

#class OrtographicText
#   __sentences: List
#   __seg_possible_list: List
#   __seg_stop_list: List
#   __seg_force_list: List
#   
#   segmenter
