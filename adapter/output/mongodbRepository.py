from pymongo import MongoClient
from domain.entities.suscriber import Suscriber
import json 
from domain.suscriberRepositoryPort import SuscriberRepository


client = MongoClient('localhost:27017',username='training',password='password',authSource='training',authMechanism='SCRAM-SHA-256')
db = client['training']
suscribers = db['suscribers']

class MongodbInfra(SuscriberRepository):
    def __init__(self):
        pass

    def save(self,suscriber):        
        suscribers.insert_one(suscriber.__dict__)
        
    
    def getAll(self) -> list:
        result = list(suscribers.find({'key': { "$exists": True } },{'topic_name':1,'key':1, '_id':0}))
        
        return result
    
    def delete(self, topic_name) -> int:
        query = {"topic_name": topic_name}

        result = suscribers.delete_many(query)
        print(result.deleted_count, " documents deleted.")
        return result.deleted_count
    
    def searchByTopic(self, topic_name) -> dict:
         query = {"topic_name": topic_name}
         suscribe = suscribers.find_one(query)         
         return suscribe
        
    
