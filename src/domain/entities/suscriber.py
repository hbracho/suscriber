import secrets
import uuid
suscriber_list = []
    
class Suscriber:
    
    def __init__(self,topic_name):
        self.key=secrets.token_urlsafe(20)
        self.topic_name=topic_name
        self._id=uuid.uuid4().hex
    
    @property
    def data(self):
        return {
            'key': self.token,
            'topic_name': self.topic_name
        }
    def __str__(self):
        return "{topic_name: " + self.topic_name + ", key: "+self.key+"}"