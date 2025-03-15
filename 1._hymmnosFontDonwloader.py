import requests
import os

if os.path.exists("hymmnos.ttf"):
  os.rename("hymmnos.ttf", "_hymmnos.ttf")
  print(f"hymmnos.ttf already exists, renaming file.")
elif not os.path.exists("_hymmnos.ttf"):
  print("hymmnos.ttf not found. Downloading...")
  response = requests.get("https://hymmnoserver.uguu.ca/static/hymmnos.ttf", stream=True)
  
  if response.status_code == 200:
    with open("_hymmnos.ttf", 'wb') as file:
      for chunk in response.iter_content(1024):
        file.write(chunk)
    print(f"Downloaded hymmnos.ttf successfully.")
    # rename file
  else:
      print(f"Failed to download file. HTTP Status Code: {response.status_code}")
elif os.path.exists("_hymmnos.ttf"):
  print(f"_hymmnos.ttf already exists.")