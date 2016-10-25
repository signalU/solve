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
        all_final_s = []


    def propositions_implies_from(self, final, values):
        # implies = list()
        implies = values

        conclusions = self.conclusions()
        predecessors = self.antecedent()
        intermediate_conclusions = set(conclusions) & set(predecessors)

        # print(conclusions)
        # print(predecessors)
        final_conclusions = set(conclusions) - set(predecessors)
        # print(intermediate_conclusions)

        final_rule = self.rules.find({"consequent._idConsequent": final})
        for rule in final_rule:
            implies.append(rule)
            for item in rule["predecessor"]:
                # print(item["_idAntecesorProposition"])
                # print(self.rules.find({"consequent._idConsequent": item["_idAntecesorProposition"]}))
                if item["_idAntecesorProposition"] in intermediate_conclusions:
                    self.propositions_implies_from(item["_idAntecesorProposition"], implies)

            # return implies
            # print(rule)
        # print(final_rule)
        # all_implies = list()
        # for item in implies:
        #     # print(item["_id"])
        #     all_implies.append(item)
        return implies
        # print(implies)
        # print(all_implies)
        # return all_implies
        # self.all_final_s


    # def helper_implies(self, _id):



    def conclusions(self):
        complete_rules = self.rules.find({})


        # print(complete_rules)
        # for document in complete_rules:
        #     print(document)

        # tags = db.mycoll.find({"category": "movie"}).distinct("tags")
        tags = self.rules.find({}).distinct("consequent._idConsequent")

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


    def guieded_conclusions(self, id_rules):
        conclusions = list()
        for _id in id_rules:
            pass

    def antecedent(self):
        complete_rules = self.rules.find({})


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

    def control_antecedent(self, id_rules):
        predecessor = list()
        rules = list()
        for _id in id_rules:
            rules.append(self.rules.find_one({"_id": ObjectId(_id)}))

        complete_rules = rules

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
        # print(predecessor)
        # self.show_names(predecessor)
        return predecessor



    def show_names(self, _ids):
        for _id in _ids:
            proposition = self.propositions.find_one({"_id": ObjectId(_id)}, {"name": 1})
            print(proposition)
