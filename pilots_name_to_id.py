import pymongo
from swapi import *
client = pymongo.MongoClient()

db = client["starwars"]

for ship in starships["results"]:
    updated_pilots = []
    for pilot in ship["pilots"]:
        star_name = get_pilots(pilot)["name"]
        star_id = db.characters.find_one({"name": star_name}, {"_id": 1})
        pilot = star_id["_id"]
        updated_pilots.append(pilot)
    ship["pilots"] = updated_pilots

# for ship in starships["results"]:
#     print(ship["pilots"])

# for ship in starships["results"]:
#     print(ship)
