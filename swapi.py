import requests

starships = None
url_starship = "https://swapi.dev/api/starships"
try:
    response = requests.get(url_starship)
    starships = response.json()
except:
    print("invalid requests")


def get_pilots(pilot_url):
    try:
        if pilot_url:
            pilot_response = requests.get(pilot_url)
            pilot_results = pilot_response.json()
            return pilot_results
    except:
        print("pilots don't exists!")
