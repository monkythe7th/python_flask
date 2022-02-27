from .db_conn import *

def get_one(c,item=None):
    col = get_col(c)
    if item:
        x = col.find_one(item)
        return x
    else:
        return col.find_one()

def get_all(c):
    return get_col(c).find()
    