import pymongo
import dnspython


client = pymongo.MongoClient("mongodb+srv://Mani_of_the_west:rCzgiHiwoy9LPfdK@cluster0.imele.mongodb.net/test?retryWrites=true&w=majority")


db = client.test

db.test_one({'x':1})