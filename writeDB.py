# import pymongo

# from pymongo import MongoClient
from pymongo import MongoClient


def insert_proposition(name):
    name = str(name)
    exist = propositions.find({'name': name}).count() > 0
    # exist = False
    # print(exist, "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!")
    if exist:
        pass
        print("This item already exits")
    else:
        print(type(name), name)
        proposition = {
            "name": name,
            "status": True
        }
        propositions.insert_one(proposition)
        print("Element added")


def insert_sentence(predecessor, successor):
    sentence = {
        'predecessor': predecessor,
        'successor': successor
    }
    sentences.insert_one(sentence)


def insert_sentence2(predecessor, successor):
    # id_predecessor =
    # print(len(predecessor), "len")
    rule = {}
    elements = []
    for item in predecessor:
        # item[0] = propositions.find_one({"name": item[0]})["_id"]
        item[0] = propositions.find_one({"name": item[0]}).get('_id')
        item[0] = str(item[0])
        data = {
            "_idAntecesorProposition": item[0],
            "isFalse": not item[1]
        }
        elements.append(data)

        # single = propositions.find_one({"name": item[0]})
        # item[0] = si
    rule['predecessor'] = elements
    # print(successor, "successor", successor[0])
    # successor[0] = propositions.find_one({"name": successor[0]}).get('_id')
    # print(propositions.find_one({"name": successor[0]}).get('_id'))
    _idConsequent = propositions.find_one({"name": successor[0]}).get('_id')
    _idConsequent = str(_idConsequent)
    # successor[0] = str(successor[0])
    rule['consequent'] = {
        # "_idConsequent":  successor[0],
        "_idConsequent":  _idConsequent,
        "isFalse": not successor[1]
    }
    rules.insert_one(rule)
    print(predecessor)





client = MongoClient('mongodb://localhost:3001/')

db = client['meteor']

propositions = db.singleProposition
sentences = db.sentences
rules = db.rules
# rule = rules.find_one()
# print(rule)

# insert_proposition("python proposition")


# for rules in rules.find():
#     print(rules)
