from pymongo import MongoClient
from src.domain.entities.suscriber import Suscriber
import json 
from src.domain.suscriberRepositoryPort import SuscriberRepository
import os

host=os.environ['HOST']
port = os.environ['PORT']
database = os.environ.get('DATABASE_NAME')
authsource = os.environ.get('AUTHSOURCE')
username=os.environ.get('USER_NAME')
password = os.environ.get('PASSWORD')
source=host+":"+port
#client = MongoClient('localhost:27017',username='training',password='password',authSource='training',authMechanism='SCRAM-SHA-256')
#db = client['training']
#suscribers = db['suscribers']
# 

class MongodbInfra(SuscriberRepository):
    def __init__(self):
        client = MongoClient(source,username=username,password=password,authSource=authsource,authMechanism='SCRAM-SHA-256')
        db = client[database]
        self.suscribers = db['suscribers']

    def save(self,suscriber):        
        self.suscribers.insert_one(suscriber.__dict__)
        
    
    def getAll(self) -> list:
        result = list(self.suscribers.find({'client_id': { "$exists": True } },{'topic_name':1,'client_id':1, '_id':0}))
        
        return result
    
    def delete(self, topic_name) -> int:
        query = {"topic_name": topic_name}

        result = self.suscribers.delete_many(query)
        print(result.deleted_count, " documents deleted.")
        return result.deleted_count
    
    def searchByTopic(self, topic_name) -> dict:
         query = {"topic_name": topic_name}
         suscribe = self.suscribers.find_one(query)         
         return suscribe
        
    
