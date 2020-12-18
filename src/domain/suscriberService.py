from src.domain.suscriberRepositoryPort import SuscriberRepository
from src.domain.entities.suscriber import Suscriber
from src.domain.exceptions.exceptions import AlreadyRegisteredException,NotFoundRegisterException, ForbiddenException
from src.application.utils import encrypt_message, decrypt_message, check_password
import logging

class SuscriberService:

    def __init__(self, repository: SuscriberRepository):
        self.logger = logging.getLogger(__class__.__name__)
        self.repository = repository

    def searchAll(self) -> list:
        return self.repository.getAll()
        
    def searchByTopicNameAndClientId(self, topic_name:str, client_id:str) -> dict:
        
        self.logger.debug('searching topic: %s and client id: %s', client_id, topic_name)
       
        client_id_encrypt= encrypt_message(client_id)        

        result = self.repository.searchByTopic(topic_name)        

        if not result or not check_password(client_id, result['client_id']):
            self.logger.warning("topic name (%s) and client (%s) there isn't a relationship", topic_name, client_id)
            raise ForbiddenException
        
        self.logger.debug("resulted-> %s",result)
        return result

    def delete(self, topic_name:str)-> int:
        self.logger.debug("deleting topic %s", topic_name)
        count_deleted= self.repository.delete(topic_name)
        self.logger.debug("is deleted topic? %s", count_deleted)
        if count_deleted == 0:
             raise NotFoundRegisterException

    def create(self, suscriber:Suscriber) -> Suscriber:
        self.logger.debug("create suscriber and topic, %s", suscriber)
        result = self.repository.searchByTopic(suscriber.topic_name)
        
        if result:
            self.logger.warning("already the suscriber, %s", result)
            raise AlreadyRegisteredException
        suscriber.client_id=encrypt_message(suscriber.client_id)
        
        self.repository.save(suscriber)
        self.logger.debug('suscriber saved in bd')
        # suscriber.client_id = decrypt_message(suscriber.client_id)

        return suscriber