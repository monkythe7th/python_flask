from .db_conn import *

def create(item,c):
    print(item)
    col = get_col(c)
    x = col.insert_one(item)
    return x.inserted_id