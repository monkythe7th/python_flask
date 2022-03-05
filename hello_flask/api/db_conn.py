from pymongo import MongoClient
import pymongo

uri = "mongodb+srv://cluster0.7nocv.mongodb.net/myFirstDatabase?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = MongoClient(uri,
                    tls=True,
                    tlsCertificateKeyFile='./api/X509-cert-5642347178223945930.pem')
db = client["helloFlask"]

def get_col(col):
    return db[col]