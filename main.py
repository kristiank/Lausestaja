# -*- coding:utf-8 -*-

import lausestaja.ortographictext

def main():
    '''do some test and show off the module'''

    sample_text = 'Midagi taolist seal öeldi. Nii see oli 3. aastal! See oli hirmus! see 2. Maailmasõda. Polnd mõistust. Keegi K. Kankainen ja J. V. Veski ja K.J.Petersonil oli sünnipäev 3. mail. 3. Tartu maaraton s.o suur jooks. Juhtuski 3000. a e.m.a.'
    ot = lausestaja.ortographictext.OrtographicText(sample_text)
    ot.segment()

    for sentence in ot.get_sentence_list():
        print(sentence.get_pos_in_text(),
              sentence.get_content_text(),
              sentence.get_start_char_pos(),
              sentence.get_end_char_pos(),
              sep=', ')
    
    # use fileinput to process all files from sys.argv[1:]
    # import fileinput
    # for line in fileinput.input():
    #     process(line)

if __name__ == "__main__":
    main()
