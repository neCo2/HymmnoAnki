import requests
from bs4 import BeautifulSoup
import time
import random
import json

special_words = {
  "nel": {
    "Hymmnos": "0",
    "Meaning": "",
    "Class": "Number",
    "Kana": "",
    "Dialect": "Central Standard Note",
  },
  "nnoi": {
    "Hymmnos": "1",
    "Meaning": "",
    "Class": "Number",
    "Kana": "",
    "Dialect": "Central Standard Note",
  },
  "ji": {
    "Hymmnos": "2",
    "Meaning": "",
    "Class": "Number",
    "Kana": "",
    "Dialect": "Central Standard Note",
  },
  "dri": {
    "Hymmnos": "3",
    "Meaning": "",
    "Class": "Number",
    "Kana": "",
    "Dialect": "Central Standard Note",
  },
  "fef": {
    "Hymmnos": "4",
    "Meaning": "",
    "Class": "Number",
    "Kana": "",
    "Dialect": "Central Standard Note",
  },
  "vira": {
    "Hymmnos": "5",
    "Meaning": "",
    "Class": "Number",
    "Kana": "",
    "Dialect": "Central Standard Note",
  },
  "ixe": {
    "Hymmnos": "6",
    "Meaning": "",
    "Class": "Number",
    "Kana": "",
    "Dialect": "Central Standard Note",
  },
  "hept": {
    "Hymmnos": "7",
    "Meaning": "",
    "Class": "Number",
    "Kana": "",
    "Dialect": "Central Standard Note",
  },
  "oct": {
    "Hymmnos": "8",
    "Meaning": "",
    "Class": "Number",
    "Kana": "",
    "Dialect": "Central Standard Note",
  },
  "nei": {
    "Hymmnos": "9",
    "Meaning": "",
    "Class": "Number",
    "Kana": "",
    "Dialect": "Central Standard Note",
  },
  "tab": {
    "Hymmnos": "=>",
    "Meaning": "",
    "Class": "Special",
    "Kana": "",
    "Dialect": "Central Standard Note",
  },
  "tras": {
    "Hymmnos": ">>",
    "Meaning": "",
    "Class": "Special",
    "Kana": "",
    "Dialect": "Central Standard Note",
  },
  "xeku": {
    "Hymmnos": "Xc=",
    "Meaning": "",
    "Class": "Special",
    "Kana": "",
    "Dialect": "Central Standard Note",
  },
  "pass": {
    "Hymmnos": "->",
    "Meaning": "",
    "Class": "Special",
    "Kana": "",
    "Dialect": "Central Standard Note",
  },
  "(s)pag": {
    "Hymmnos": "<-x",
    "Meaning": "",
    "Class": "Special",
    "Kana": "",
    "Dialect": "Central Standard Note",
  },
}

def fetch_and_parse_table(url):
  response = requests.get(url)
  response.raise_for_status() # Raise an error for bad responses
  
  soup = BeautifulSoup(response.text, 'html.parser')
  tables = soup.find_all('table')
  
  if len(tables) < 3:
    raise ValueError("The page does not contain at least three tables.")
  
  third_table = tables[2] # Get the third table
  rows = third_table.find_all('tr')
  
  headers = [header.get_text(strip=True) for header in rows[0].find_all('th')]
  data = {}
  
  for row in rows[1:]: # Skip header row
    values = [cell.get_text(strip=True) for cell in row.find_all('td')]
    entry = dict(zip(headers, values))
    key = values[0] if values else None # Use the first column as key
    if key:
      data[key] = entry
  
  return data

if __name__ == "__main__":
  base_url = "https://hymmnoserver.uguu.ca/browse.php?page={}"
  hymmnos_dict = {}
  
  for page in range(1, 15):
    print(f"scraping page {page}")
    url = base_url.format(page)
    page_data = fetch_and_parse_table(url)
    time.sleep(random.uniform(0.2, 2))
    hymmnos_dict.update(page_data) # Merge dictionaries
  
  hymmnos_dict.update(special_words) # Add special words

  print(f"Scraped {len(hymmnos_dict)} words.")

  with open("hymmnosDictionary.json", "w") as file:
    json.dump(hymmnos_dict, file, indent=2)

