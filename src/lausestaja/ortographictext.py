# -*- coding:utf-8 -*-
import regex
import os.path
import lausestaja
import lausestaja.ortographicsegmenter
import lausestaja.ortographicsentence

class OrtographicText(object):
    '''Container for an ortographic text, which consists of a list of
    ortographic sentences. The ortographic text also has a changeable
    text segmenter, which can be used to segment an inputted text.'''
    def __init__(self, text=None):
        '''Initializes an empty text with the default segmenter.'''
        self._sentence_list = []
        self._text = text
        self._length = len(self._sentence_list)
        self._segmenter = lausestaja.ortographicsegmenter.OrtographicSegmenter(self)

    def sentence_list(self, preserve_ws=True):
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
        os = lausestaja.ortographicsentence.OrtographicSentence(self,
                                                                sentence_text,
                                                                pos_in_text,
                                                                start_char_pos,
                                                                end_char_pos)
        os.strip()
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
        seg_sentences = self._segmenter.segment(self._text)
        
        #pos_in_text = 0
        #for sentence in seg_sentences:
        #    sentence_text = sentence[0]
        #    pos_in_text += 1
        #    start_char_pos = sentence[1]
        #    end_char_pos = sentence[2]

        #    self.append_sentence(sent
