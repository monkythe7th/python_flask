from pymongo import MongoClient
import pymongo

uri = "test server connection url"
client = MongoClient(uri,
                    tls=True,
                    tlsCertificateKeyFile='./api/X509-cert.pem')
db = client["helloFlask"]

def get_col(col):
    return db[col]
