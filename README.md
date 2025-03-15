# HymmnoAnki

This is a collection of short scripts that can be used to generate Hymmnos Anki decks from the resources provided by [HymmnoServer](https://hymmnoserver.uguu.ca) ([repo](https://github.com/flan/hymmnoserver)).

Hymmnos is a language created for the Ar tonelico series.

## Usage
**This project requires Python 3.10+**
- Navigate to project folder
- `pip install -r requirements.txt`
  Install the requirements.
- `python 1._hymmnosFontDonwloader.py`
  This downloads the `hymmnos.ttf` font to be packaged with the Anki deck.
- `python 2._scrapeHymmnosDictionary.py`
  This scrapes the HymmnoServer dictionary page and saves all words to a local json file for later use.
- `python 3._hymmnosDictionaryAnki.py`
  This uses the saved json dictionary to generate an Anki deck of all the words on HymmnoServer.
- `python 4._hymmnosAlphabetAnki.py`
  This generates an Anki deck of the characters of the Hymmnos alphabet.