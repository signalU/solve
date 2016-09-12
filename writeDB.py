# import pymongo

# from pymongo import MongoClient
from pymongo import MongoClient


def insert_proposition(name):
    exist = propositions.find({'name': name}).count() > 0
    if exist:
        pass
        # print("This item already exits")
    else:
        proposition = {
            "name": name,
            "status": True
        }
        propositions.insert_one(proposition)
        # print("Element added")


client = MongoClient('mongodb://localhost:3001/')

db = client['meteor']

propositions = db.singleProposition
rules = db.rules
rule = rules.find_one()
# print(rule)

insert_proposition("python proposition")


for rules in rules.find():
    print(rules)
