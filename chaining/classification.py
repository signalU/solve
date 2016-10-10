from pymongo import MongoClient
from bson.objectid import ObjectId


class Classification(object):
    # client = MongoClient('mongodb://localhost:3001/')
    # db = client['meteor']
    # propositions = db.singleProposition
    # sentences = db.sentences
    # rules = db.rules

    def __init__(self):
        self.something = "test"
        client = MongoClient('mongodb://localhost:3001/')
        db = client['meteor']
        self.propositions = db.singleProposition
        sentences = db.sentences
        self.rules = db.rules

    def conclusions(self):
        complete_rules = self.rules.find({})

        print()
        # print(complete_rules)
        # for document in complete_rules:
        #     print(document)

        # tags = db.mycoll.find({"category": "movie"}).distinct("tags")
        tags = self.rules.find({}).distinct("consequent._idConsequent")
        print()
        # print(tags)

        conclusions = list()
        for _id in tags:
            proposition = self.propositions.find_one({"_id": ObjectId(_id)}, {"name": 1})
            # print(proposition)
            conclusions.append(proposition)

        all_conclusion = list()
        for item in conclusions:
            # print(item["_id"])
            all_conclusion.append(str(item["_id"]))
        return all_conclusion

    def antecedent(self):
        complete_rules = self.rules.find({})

        print()
        # print(complete_rules["consequent"])
        predecessor = list()
        for rule in complete_rules:
            # print(rule)
            # print(rule["predecessor"])
            for item in rule["predecessor"]:
                # print(predecessor['_idAntecesorProposition'])
                _id_predecessor = item['_idAntecesorProposition']
                # print(_id_predecessor)
                if _id_predecessor not in predecessor:
                    predecessor.append(_id_predecessor)

        # print(predece)
        return predecessor
        # print(complete_rules)

    def show_names(self, _ids):
        for _id in _ids:
            proposition = self.propositions.find_one({"_id": ObjectId(_id)}, {"name": 1})
            print(proposition)
