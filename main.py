# -*- coding:utf-8 -*-

import lausestaja

def main():
    '''do some test and show off the module'''

    sample_text = 'Midagi taolist seal öeldi. Nii see oli 3. aastal! Polnd muud.'
    ot = lausestaja.OrtographicText(sample_text)
    #print(str(ot.get_number_of_sentences()))
    #ot.append_sentence(sample_text, 0, len(sample_text))
    ot.segment()
    print(ot.get_sentence_list())

    # use fileinput to process all files from sys.argv[1:]
    # import fileinput
    # for line in fileinput.input():
    #     process(line)

if __name__ == "__main__":
    main()
