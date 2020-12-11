from src.domain.suscriberRepositoryPort import SuscriberRepository
from src.domain.entities.suscriber import Suscriber
from src.domain.exceptions.exceptions import AlreadyRegisteredException,NotFoundRegisterException, ForbiddenException
from src.application.utils import encrypt_message, decrypt_message, check_password
class SuscriberService:

    def __init__(self, repository: SuscriberRepository):
        self.repository = repository

    def searchAll(self) -> list:
        return self.repository.getAll()
        
    def searchByTopicNameAndClientId(self, topic_name:str, client_id:str) -> dict:
        print("client_id=>", client_id)
        client_id_encrypt= encrypt_message(client_id)        

        result = self.repository.searchByTopic(topic_name)
        print("result->",result)

        if not result or not check_password(client_id, result['client_id']):
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
        suscriber.client_id=encrypt_message(suscriber.client_id)
        
        self.repository.save(suscriber)
        # suscriber.client_id = decrypt_message(suscriber.client_id)

        return suscriber