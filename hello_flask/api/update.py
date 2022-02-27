from .db_conn import *

def update(c,user,item):
    col = get_col(c)
    return col.update_one(user,item).acknowledged