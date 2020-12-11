
from marshmallow import Schema, fields


class SuscriberSchema(Schema):
    topic_name = fields.String(required=True)
    client_id = fields.String(required=True)
    
class SuscriberCreatedSchema(Schema):
    topic_name = fields.String(required=True)
    client_id = fields.String(required=True)

        
   

