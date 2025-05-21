import json
import requests #api 3rd party request
response = requests.get("https://itunes.apple.com/search?entity=song&limit=25&term=seedhemaut")
o= response.json()
for result in o["results"]:
    print(result["trackName"])