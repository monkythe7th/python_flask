from flask import g, current_app
from flask_pymongo import PyMongo


def get_db():
    db = getattr(g, "_database", None)

    if db == None:
        mongodb_client = PyMongo(current_app, uri="mongodb+srv://cluster0.7nocv.mongodb.net/helloFlaskDB?retryWrites=true&w=majority")
        db = g._database = mongodb_client.db

    return db

def get_col(collection):
    col = get_db()[collection]
    return col
