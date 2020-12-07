from src.domain.suscriberRepositoryPort import SuscriberRepository
from src.domain.entities.suscriber import Suscriber
from src.domain.exceptions.exceptions import AlreadyRegisteredException,NotFoundRegisterException, ForbiddenException
from src.application.utils import hash_password, check_password
class SuscriberService:

    def __init__(self, repository: SuscriberRepository):
        self.repository = repository

    def searchAll(self) -> list:
        return self.repository.getAll()
        
    def searchByTopicName(self, topic_name:str, key:str) -> dict:
        
        result = self.repository.searchByTopic(topic_name)
        print("result->",result)

        if not result or not check_password(key, result['key']):
            raise ForbiddenException
        
        return result

    def delete(self, topic_name:str)-> int:
        count_deleted= self.repository.delete(topic_name)
        
        if count_deleted == 0:
             raise NotFoundRegisterException

    def create(self, suscriber:Suscriber) -> Suscriber:
        result = self.repository.searchByTopic(suscriber.topic_name)
        print("result->",result)
        if result:
            raise AlreadyRegisteredException
        key = suscriber.key
        suscriber.key=hash_password(key)
        self.repository.save(suscriber)        
        suscriber.key=key
        return suscriber

