# -*- coding:utf-8 -*-
import sys
from lausestaja import ortographictext


## See näide avab kõik failid mis antakse käsurealt ja näitab kõik tuvastatud
#  laused ekraanil. Hea kui on vaja järele proovida, kas reeglitega on korras.


# teeme ühe tühja teksti
ot = ortographictext.OrtographicText()

# kõik tekst mis käsureal on antud pärast meie skripti nime, on kättesaadav
# sys.argv[1:], näiteks python3 proov2.py üks.txt kaks.txt kolm.txt
# võib ka kasutada käsurea jokereid python3 proov2.py *.txt, need antakse
# pythonile ette kui õiged failinimed


if len(sys.argv) < 2:
    print("Kasutada koos failinimede loendiga, näiteks:")
    print("python3", sys.argv[0], "üks.txt", "kaks.txt", sep=' ')
    exit()

for filename in sys.argv[1:]:
    with open(filename, 'r') as f:
        print("===== faili algus: filename")
        file_text = f.read()
        ot.set_text(file_text)

        for lause in ot.sentence_list():
            print(lause.start_char_pos(),
                  lause.text(),
                  sep=': ')
            print(lause.matched_rule())

        print("===== faili lõpp: filename")


#    print(sentence.get_pos_in_text(),
#          sentence.text(),
#          sentence.start_char_pos(),
#          sentence.end_char_pos(),
#          sep=', ')
    
