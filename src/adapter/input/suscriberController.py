from flask import request
from flask_restful import Resource
from http import HTTPStatus
import json
from src.domain.entities.suscriber import Suscriber, suscriber_list
from src.adapter.schema.suscriber import SuscriberSchema, SuscriberCreatedSchema
from src.adapter.output.mongodbRepository import MongodbInfra
from webargs import fields
from webargs.flaskparser import use_kwargs
from src.adapter.input.extensions import cache
from src.domain.suscriberService import SuscriberService
from src.domain.exceptions.exceptions import AlreadyRegisteredException, NotFoundRegisterException, ForbiddenException


suscriber_schemaList = SuscriberSchema(many=True)
suscriber_schemaSingle = SuscriberSchema()
suscriberPost_schemaSingel = SuscriberCreatedSchema()
mongodb = MongodbInfra()
service = SuscriberService(mongodb)

class SuscriberListResource(Resource):

    def get(self):
        suscribers = service.searchAll()
        return suscriber_schemaList.dump(suscribers).data, HTTPStatus.OK
        
    def post(self):
        try:
            
            json_data = request.get_json()
            
            data, errors = suscriber_schemaSingle.load(data=json_data)
            if errors:
                return {'message': 'Validation errors', 'errors': errors}, HTTPStatus.BAD_REQUEST
            suscriber = Suscriber(topic_name=data['topic_name'], client_id=data['client_id'])
            result = service.create(suscriber)
            return "Created", HTTPStatus.CREATED
        
        except AlreadyRegisteredException:
            return {'message': 'Topic Name is already'}, HTTPStatus.ALREADY_REPORTED
        except Exception as e:
            print(e)
            return {'message': 'System Error'}, HTTPStatus.INTERNAL_SERVER_ERROR
        
class SuscriberResource(Resource):

    def delete(self, topic_name):
        try:
            service.delete(topic_name)

            return {'message': 'Topic Name deleted'}, HTTPStatus.ACCEPTED
        except NotFoundRegisterException:
             return {'message': 'Topic Name not found'}, HTTPStatus.NOT_FOUND
        except Exception as e:
            print(e)
            return {'message': 'System Error'}, HTTPStatus.INTERNAL_SERVER_ERROR
          
    @use_kwargs({'client_id': fields.Str(missing='not_found')})
    @cache.cached(query_string=True)
    def get(self, topic_name, client_id):
        try:
            print('entro en el search, topic_name: ' + topic_name +", client_id: " + client_id)

            if client_id == 'not_found':
                return {'message': 'Parameter key is required'}, HTTPStatus.BAD_REQUEST
            
            result = service.searchByTopicNameAndClientId(topic_name, client_id)
            print("result->",result)

            return suscriber_schemaSingle.dump(result).data, HTTPStatus.ACCEPTED
        except ForbiddenException:
            return {'message': 'Register not found or key is incorrect'}, HTTPStatus.UNAUTHORIZED
        except Exception as e:
            print(e)
            return {'message': 'System Error'}, HTTPStatus.INTERNAL_SERVER_ERROR