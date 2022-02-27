from pymongo import MongoClient
import pymongo

client = MongoClient("mongodb+srv://tester01:tester1P455@cluster0.7nocv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["helloFlask"]

def get_col(col):
    return db[col]