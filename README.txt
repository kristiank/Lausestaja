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

Lausestaja üldine töömõte on peegeldatud selle moodulite jagamises, millest
OrtographicText on siduvaks aluspunktiks -- OrtographicText representeerib
ühte tervikteksti, mille saab sisestada nt load_text() funktsiooniga.
Tekst tükeldatakse OrtographicSegmenteriga, mis laaditakse automaatselt vaikiv-
reeglistikuga OrtographicText loomisel. Edasi tükeldatakse tekst 
OrtographicText.segment() funktsiooniga. Tükeldatud teksti laused salvestatakse
OrtographicSentence-etina listi, mis saadakse kätte
OrtographicText.sentence_list() funktsiooniga.

Kaustas 'bin/' on python skripte mis näitavad lausestaja paketti kasutamist. Ent
olgu siin mainitud lihtne kasutamisjuhtum:

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

* Kirjutada parem proovitekst bin/proov1.py-sse
* Lisada OrtographicSegmenter.segment(debug = False) mis prindib iga
  reegli kohta kas sobitub või mitte (if debug == 2: wait_for_keypress())
* Vaadata litsents ja autoriõigused läbi, et ei jääks kellegi omaks
* Lisada üldine kirjeldus mooduli üldisest ülesehitusest ja kasutamisest
  samuti teha help() ja dir() selgeks
* Valida kas kasutada või mitte get_... set_... funktsiooninimesid
  ja kasutada seda läbivalt!
* Lisada testid

Varasemad kaasalööjad
---------------------

Kristian Kankainen
