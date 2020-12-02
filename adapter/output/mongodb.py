from pymongo import MongoClient
from domain.entities.suscriber import Suscriber
import json 

client = MongoClient('localhost:27017',username='training',password='password',authSource='training',authMechanism='SCRAM-SHA-256')
db = client['training']
suscribers = db['suscribers']

class MongodbInfra:
    def __init__(self):
        pass

    def save(self,suscriber):
        #s = json.dumps(suscriber.__dict__) 
        #print(s)
        suscribers.insert_one(suscriber.__dict__)
        print('saved')
    
    def getAll(self):
        result = list(suscribers.find({'key': { "$exists": True } },{'topic_name':1,'key':1, '_id':0}))
        
        return result
    
    def delete(self, topic_name):
        query = {"topic_name": topic_name}

        x = suscribers.delete_many(query)
        print(x.deleted_count, " documents deleted.")
        return x.deleted_count
    
    def searchByTopic(self, topic_name):
         query = {"topic_name": topic_name}
         suscribe = suscribers.find_one(query)         
         return suscribe
        
    
