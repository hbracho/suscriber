from flask import request
from flask_restful import Resource
from http import HTTPStatus
import json
from domain.entities.suscriber import Suscriber, suscriber_list
from adapter.schema.suscriber import SuscriberSchema
from adapter.output.mongodb import MongodbInfra
from webargs import fields
from webargs.flaskparser import use_kwargs
from application.utils import hash_password, check_password
from adapter.input.extensions import cache

suscriber_schemaList = SuscriberSchema(many=True)
suscriber_schemaSingle = SuscriberSchema()
mongodb = MongodbInfra()

class SuscriberListResource(Resource):

    def get(self):
        print('new')
        suscribers=mongodb.getAll()
        for document in suscribers:
          print(document)
        return suscriber_schemaList.dump(suscribers).data, HTTPStatus.OK
        

    def post(self):
        json_data = request.get_json()
        data, errors = suscriber_schemaSingle.load(data=json_data)
        if errors:
            return {'message': 'Validation errors', 'errors': errors}, HTTPStatus.BAD_REQUEST
        suscriber = Suscriber(topic_name=data['topic_name'])

        result = mongodb.searchByTopic(suscriber.topic_name)
        print("result->",result)

        if result:
            return {'message': 'Topic Name is already'}, HTTPStatus.ALREADY_REPORTED

        key= suscriber.key
        suscriber.key=hash_password(key)
        mongodb.save(suscriber)
        
        suscriber.key=key
        return suscriber_schemaSingle.dump(suscriber).data, HTTPStatus.CREATED

class SuscriberResource(Resource):

    def delete(self, topic_name):
        count_deleted= mongodb.delete(topic_name)
        
        if count_deleted == 0:
             return {'message': 'Topic Name not found'}, HTTPStatus.NOT_FOUND

        return {'message': 'Topic Name deleted'}, HTTPStatus.ACCEPTED
    
    @use_kwargs({'key': fields.Str(missing='not_found')})
    @cache.cached(query_string=True)
    def get(self, topic_name, key):

        print('entro en el search' + topic_name +" key " + key)

        if key == 'not_found':
            return {'message': 'Parameter key is required'}, HTTPStatus.BAD_REQUEST
        
        result = mongodb.searchByTopic(topic_name)
        print("result->",result)

        if not result or not check_password(key, result['key']):
            return {'message': 'Register not found or key is incorrect'}, HTTPStatus.UNAUTHORIZED
        
        
        return suscriber_schemaSingle.dump(result).data, HTTPStatus.ACCEPTED

        


