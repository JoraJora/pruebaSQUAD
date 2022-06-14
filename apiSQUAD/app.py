import os
from flask import Flask
from flask_restful import Api
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from resources.chistes import ChistesAPI, consultaAPI, consultaAPIPath
from resources.numeric import sumAPI, mcmAPI

app = Flask(__name__)  # Flask app instance initiated
app.config['BUNDLE_ERRORS'] = True
api = Api(app, catch_all_404s=True)  # Flask restful wraps Flask app around it.
 
# Config Swagger
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Prueba SQUADMAKERS',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

# Config endpoints
api.add_resource(consultaAPI, '/consultachistes')
api.add_resource(consultaAPIPath, '/consultachistes/<path>')
api.add_resource(ChistesAPI, '/chistes')
api.add_resource(sumAPI, '/sumauno/<int:number>')
api.add_resource(mcmAPI, '/MCM')
docs.register(consultaAPI)
docs.register(consultaAPIPath)
docs.register(ChistesAPI)
docs.register(sumAPI)
docs.register(mcmAPI)


if __name__ == '__main__':
    #define the localhost ip and the port that is going to be used
    # in some future article, we are going to use an env variable instead a hardcoded port 
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
