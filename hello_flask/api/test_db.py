from db_conn import *
from create import create
# import pytest

def test_db():
    db = client.test
    print(db)
    col = get_col("auth")
    # assert db != None
    assert col != None

def test_create():
    item = {
        "username": "tester",
        "password": "tester1pass"
    }
    x = create(item,"auth")
    assert x != None