from pymongo import MongoClient
from marshmallow import Schema, fields
from flask_restful import Resource, reqparse
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

# Config mongo  conection
client = MongoClient('mongodb://consultaSQUAD:consulta2413@dbnosql:28108/apisquad')
db = client.apisquad

class ChistesResponseSchema(Schema):
    message = fields.Str(default='Success')

class ChistesRequestSchema(Schema):
    number = fields.Integer(required=True, description="Nombre")
    chiste = fields.String(required=True, description="Nombre")
    
#  Restful way of creating APIs through Flask Restful
class ChistesAPI(MethodResource, Resource):
    @doc(description='My First GET Chistes API.', tags=['Chistes'])
    @marshal_with(ChistesResponseSchema)  # marshalling
    def get(self):
        '''
        Get method represents a GET API method
        '''
        return {'message': 'My First Chistes API'}

    @doc(description='My First GET Chistes API.', tags=['Chistes'])
    @use_kwargs(ChistesRequestSchema, location=('form'))
    @marshal_with(ChistesResponseSchema)  # marshalling
    def post(self, **kwargs):
        '''
        Get method represents a GET API method
        '''
        user = {'name': kwargs['name'],
                'lastname': kwargs['lastname']}
        db.squadCollection.insert_one(user)
        return {'message': 'My First Chistes API'}


