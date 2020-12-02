
from marshmallow import Schema, fields


class SuscriberSchema(Schema):
    topic_name = fields.String(required=True)
    key = fields.String(dump_only=True)

    class Meta:
        exclude = ('key',)
    
    
   

