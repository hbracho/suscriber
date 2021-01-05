from flask import Flask
from flask_restful import Api
from src.adapter.input.extensions import cache
from src.adapter.input.config import Config
from src.adapter.input.suscriberController import SuscriberListResource, SuscriberResource
import logging
import logging.config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)
    return app

def register_extensions(app):
    cache.init_app(app)
    
    # @app.before_request
    # def before_request():
    #     print(cache.cache._cache.keys())
    #     print('\n=======================================================\n')
    # @app.after_request
    # def after_request(response):
    #     print('\n==================== AFTER REQUEST ====================\n')
    #     print(cache.cache._cache.keys())
    #     print('\n=======================================================\n')
    #     return response

def register_resources(app):
    api = Api(app)
    api.add_resource(SuscriberListResource, '/suscribers')
    api.add_resource(SuscriberResource, '/suscribers/<string:topic_name>')


if __name__ == '__main__':
    logging.config.fileConfig(fname='logger.ini')
    logger = logging.getLogger(__name__)
    app = create_app()
    # app.run(port=5000, debug=True)
    app.run(host= '0.0.0.0',port=80)

