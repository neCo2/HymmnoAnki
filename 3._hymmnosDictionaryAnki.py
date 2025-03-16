import genanki
import json
import os



with open("hymmnosDictionary.json", "r") as file:
  hymmnos_dict = json.load(file)


hymmnos_model = genanki.Model(
  1738209632,
  "Hymmnos Dictionary Model",
  fields=[
    {"name": "Reading"},
    {"name": "Hymmnos"},
    {"name": "Meaning"},
    {"name": "Class"},
    {"name": "Kana"},
    {"name": "Dialect"},
  ],
  templates=[
    {
      "name": "Card 1",
      "qfmt": """
<div style='text-align: center;'>
  <div class="hymmnosWord">{{Hymmnos}}</div>
  <div style='font-size: 2em;'>
    <div class="spoiler">{{Reading}} {{Kana}}</div>
    <table style="margin:auto;">
      <tr>
        <td>Class</td>
        <td class="spoiler">{{Class}}</td>
      </tr>
      <tr>
        <td>Dialect</td>
        <td class="spoiler">{{Dialect}}</td>
      </tr>
    </table>
  </div>
</div>
""",
      "afmt": """
<div style='text-align: center;'>
  <div class="hymmnosWord">{{Hymmnos}}</div>
  <div style='font-size: 2em;'>
    <div>{{Reading}} {{Kana}}</div>
    <table style="margin:auto;">
      <tr>
        <td>Class</td>
        <td>{{Class}}</td>
      </tr>
      <tr>
        <td>Dialect</td>
        <td>{{Dialect}}</td>
      </tr>
    </table>
    <div style='font-size: 1.5em; font-weight: bold;'>{{Meaning}}</div>
  </div>
</div>
      """,
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
.spoiler {
  background: black;
  color: black;
}
.spoiler:hover {
  color: white;
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
table {
  font-size: 0.8em;
  font-style: italic;
}
td:nth-child(1) {
  text-align: right;
  padding-right: 1em;
}
td:nth-child(2) {
  text-align: left;
}
"""
)

deck = genanki.Deck(2059400111, "Hymmnos Dictionary")

for key, values in hymmnos_dict.items():

  if "E.S." in values["Class"]: 
    values["Class"] = values["Class"].replace("E.S.","Emotion Sound")

  if "E.V." in values["Class"]: 
    values["Class"] = values["Class"].replace("E.V.","Emotion Verb")

  if "adj." in values["Class"]: 
    values["Class"] = values["Class"].replace("adj.","Adjective")

  if "adv." in values["Class"]: 
    values["Class"] = values["Class"].replace("adv.","Adverb")

  if "conj." in values["Class"]: 
    values["Class"] = values["Class"].replace("conj.","Conjunction")

  if "cnstr." in values["Class"]: 
    values["Class"] = values["Class"].replace("cnstr.","Language Construct")

  if "intj." in values["Class"]: 
    values["Class"] = values["Class"].replace("intj.","Interjection")

  if "n." in values["Class"]: 
    values["Class"] = values["Class"].replace("n.","Noun")

  if "prep." in values["Class"]: 
    values["Class"] = values["Class"].replace("prep.","Preposition")

  if "pron." in values["Class"]: 
    values["Class"] = values["Class"].replace("pron.","Pronoun")

  if "prt." in values["Class"]: 
    values["Class"] = values["Class"].replace("prt.","Particle")

  if "v." in values["Class"]: 
    values["Class"] = values["Class"].replace("v.","Verb")

  note = genanki.Note(
    model=hymmnos_model, 
    fields=[key, values["Hymmnos"], values["Meaning"], values["Class"], values["Kana"], values["Dialect"]],
    tags=[s.strip().replace(' ', '_') for s in values["Class"].split(',')]
  )
  deck.add_note(note)



if not os.path.exists("_hymmnos.ttf"): 
  print("Could not locate font file, stopping generation of anki deck.")
  exit

package = genanki.Package(deck)
package.media_files = ['_hymmnos.ttf']
package.write_to_file("hymmnos_dictionary.apkg")

print("Anki deck generated: hymmnos_dictionary.apkg")
