from pilots_name_to_id import *

# print(db.starships.find_one({"name": "CR90 corvette"}))
print(starships["results"])

# for ship in starships["results"]:
#     db.starships.insert_one(ship)

# db.starships.update_many(
#     {
#         "pilot": None
#     },
#     {
#         "$unset": {"pilots": ""}
#     })
