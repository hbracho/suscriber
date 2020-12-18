from pymongo import MongoClient
from src.domain.entities.suscriber import Suscriber
import json 
from src.domain.suscriberRepositoryPort import SuscriberRepository
import os
import logging

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
        self.logger = logging.getLogger(__class__.__name__)        
        client = MongoClient(source,username=username,password=password,authSource=authsource,authMechanism='SCRAM-SHA-256')
        db = client[database]
        self.suscribers = db['suscribers']

    def save(self,suscriber):  
        self.logger.debug('saving a suscriber %s', suscriber)
        self.suscribers.insert_one(suscriber.__dict__)
        
    
    def getAll(self) -> list:
        self.logger.debug('getting all suscribers')
        result = list(self.suscribers.find({'client_id': { "$exists": True } },{'topic_name':1,'client_id':1, '_id':0}))
        self.logger.debug('getted all suscribers')

        return result
    
    def delete(self, topic_name) -> int:
        self.logger.debug('deleting a topic name: %s', topic_name)
        query = {"topic_name": topic_name}

        result = self.suscribers.delete_many(query)
        self.logger.debug('total record deleted for topic name: %s', result.deleted_count)
        return result.deleted_count
    
    def searchByTopic(self, topic_name) -> dict:
        self.logger.debug('searching a topic name: %s', topic_name)
        query = {"topic_name": topic_name}
        suscribe = self.suscribers.find_one(query)
        self.logger.debug('is searched the topic name? %s', suscribe)
        
        return suscribe
        
    
