import genanki

# Define the Hymmnos alphabet mapping (You need to provide this data)
alphabet = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '#',
  '.', ',', "-", "/", ':', '<', '=', '>', '=>', '>>', '->', '<-x', 'Xc='
]

# Anki model definition with support for custom fonts
hymmnos_model = genanki.Model(
  1741992031,
  "Hymmnos Alphabet Model",
  fields=[
    {"name": "Letter"},
    {"name": "Hymmnos"},
  ],
  templates=[
    {
      "name": "Card 1",
      "qfmt": "<div class='hymmnosWord' style='text-align: center; font-family: hymmnos;'>{{Hymmnos}}</div>",
      "afmt": "{{FrontSide}}<br><div style='text-align: center; font-size: 2em;'>{{Letter}}</div>",
    },
  ],
  css="""
:root {
  --line-opacity: 20%;
}
@font-face {
  font-family: 'hymmnos';
  src: url('_hymmnos.ttf') format("truetype");
}
.hymmnosWord {
  position: relative;
  font-size: 6em;
  font-family: hymmnos;
  margin-bottom: .25em;
}
.hymmnosWord:before {
  content:"";
  width: 100%;
  height: 100%;
  z-index: -1;
  mix-blend-mode: difference;
  border-top: 1px solid white;
  border-bottom: 1px solid white;
  display: block;
  position: absolute;
  opacity: var(--line-opacity);
}
.hymmnosWord:after {
  content:"";
  width: 100%;
  height: 1px;
  top: 50%;
  z-index: -1;
  background: white;
  mix-blend-mode: difference;
  display: block;
  position: absolute;
  opacity: var(--line-opacity);
}
"""
)

deck = genanki.Deck(2059400110, "Hymmnos Alphabet")

for letter in alphabet:
  hymmnos = letter
  reading = letter
  match letter:
    case "=>":
      reading = "tab"
    case "->":
      reading = "pass"
    case ">>":
      reading = "tras"
    case "Xc=":
      reading = "xeku"
    case "<-x":
      reading = "(s)pag"
  note = genanki.Note(model=hymmnos_model, fields=[reading, hymmnos])
  deck.add_note(note)

if not os.path.exists("_hymmnos.ttf"): 
  print("Could not locate font file, stopping generation of anki deck.")
  exit

package = genanki.Package(deck)
package.media_files = ['_hymmnos.ttf']
package.write_to_file("hymmnos_alphabet.apkg")

print("Anki deck generated: hymmnos_alphabet.apkg")
