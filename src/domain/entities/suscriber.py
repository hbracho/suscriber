import secrets
import uuid
suscriber_list = []
    
class Suscriber:
    
    def __init__(self,topic_name, client_id):
        self.topic_name=topic_name
        self.client_id=client_id
        self._id=uuid.uuid4().hex
    
    @property
    def data(self):
        print ("entro en data => ", self.topic_name)
        return {
            'client_id': self.client_id,
            'topic_name': self.topic_name
        }
    def __str__(self):
        return "{topic_name: " + self.topic_name + ", client_id: "+self.client_id.decode("utf-8")+"}"