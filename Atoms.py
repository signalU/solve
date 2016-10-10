# # import pymongo
#
# # from pymongo import MongoClient
# from pymongo import MongoClient
#
#
# def insert_proposition(name):
#     exist = propositions.find({'name': name}).count() > 0
#     if exist:
#         pass
#         # print("This item already exits")
#     else:
#         proposition = {
#             "name": name,
#             "status": True
#         }
#         propositions.insert_one(proposition)
#         # print("Element added")
#
#
# def insert_sentence(predecessor, successor):
#     sentence = {
#         'predecessor': predecessor,
#         'successor': successor
#     }
#     sentences.insert_one(sentence)
#
#
#
# client = MongoClient('mongodb://localhost:3001/')
#
# db = client['meteor']
#
# propositions = db.singleProposition
# sentences = db.sentences
# rules = db.rules