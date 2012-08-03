==========
Lausestaja
==========

Lausestaja on suvalise teksti lauseteks segmenteerija. See kasutab ühte väga
lihtsat ent siiski võimast segmenteerimisalgoritmi.
Segmenteerimismudel koosneb kolmetasandilisest keela-luba-keela reeglite
kogumist, mida on lihtne ise muuta ja täiendada. Seetõttu on lihtne ka uusi
mudeleid luua uutele keeltele. Praegu on üks üldine eesti keele jaoks, ja üks
spetsiifiline võru keele jaoks.


Kasutamine
==========

Teksti lihtne lausestamine paistab tavaliselt niimoodi välja:

    from lausestaja import ortographictext
    
    tekst = 'Issand! hüüdis ta hämmastunult. Praegu käib ta alles 3. klassis!'
    
    ot = ortographictext.OrtographicText()
    ot.segment(tekst)
    
    for lause in ot.sentence_list():
        print("Uus lause algab kohalt: ", str(lause.start_char_pos()), sep='')
        print("ja lõppeb kohal: ", str(lause.end_char_pos()), sep='')
        print(lause.text())


Installimine
------------

Vaata faili INSTALL.txt


Algoritm
========
Algoritmi kirjeldus asub praegu siin seal OrtographicSegmenter klassi koodis.


Edasise arenduse sihid ja võimalused
====================================

* Python.org kasutab src/ kataloogi, järgi seda
* Kirjutada parem proovitekst bin/proov1.py-sse
* Vaadata litsents ja autoriõigused läbi, et ei jääks kellegi omaks
* Lisada üldine kirjeldus mooduli üldisest ülesehitusest ja kasutamisest
  samuti teha help() ja dir() selgeks
* Valida kas kasutada või mitte get_... set_... funktsiooninimesid
  ja kasutada seda läbivalt!
* Lisada testid

Varasemad kaasalööjad
---------------------

Kristian Kankainen
