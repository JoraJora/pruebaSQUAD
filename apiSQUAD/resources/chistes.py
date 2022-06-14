from pymongo import MongoClient, ReturnDocument
from marshmallow import Schema, fields
from webargs import fields as webfields
from flask import abort
from flask_restful import Resource, reqparse
from flask_apispec import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from common.utilsRequest import consultaChiste
from random import random

def custom_error(message, status_code): 
    return make_response(jsonify(message), status_code)

# Parser path
#parser = reqparse.RequestParser()
#parser.add_argument('path', required=False, help="Por favor selecciones la opción ")

# Config mongo  conection
client = MongoClient('mongodb://consultaSQUAD:consulta2413@dbnosql:28108/apisquad')
db = client.apisquad

class chisteResponseSchema(Schema):
    id = fields.Str(default='')
    chiste = fields.Str(default='')

class mensajeResponseSchema(Schema):
    message = fields.Str(default='Success')

class idUpdate(Schema):
    _id = fields.Integer(required=True, description="Ingrese el id del chiste")
    chiste = fields.String(required=True, description="Chiste que desea actualizar")
    
class idRequestSchema(Schema):
    _id = fields.Integer(required=True, description="Ingrese el id del chiste")

class ChistesRequestSchema(Schema):
    chiste = fields.String(required=True, description="Chiste que desea guardar")

#  Restful way of creating APIs through Flask Restful
class consultaAPIPath(MethodResource, Resource):
    @doc(description="""GET:
* Si se envía el path param habrá que comprobar si tiene el valor “Chuck” o el valor “Dad”
* Si tiene el valor “Chuck” se conseguirá el chiste de este API https://api.chucknorris.io
* Si tiene el valor “Dad” se conseguirá del API https://icanhazdadjoke.com/api
* En caso de que el valor no sea ninguno de esos dos se devolverá el error correspondiente""", tags=['Chistes'])
    @marshal_with(mensajeResponseSchema)  # marshalling
    def get(self, path):
        '''
        Get method represents a GET API method
        '''
        if not path is None:
            auxConsulta = consultaChiste(path)            
            if path.lower() in "chuck":
                abort(400, "_>_<_ Entro Chunk %s"%str(auxConsulta.response.json()))
            else:
                abort(400, "_>_<_ Entro Dad %s"%str(auxConsulta.response.json()))
        else:
            abort(400, "_>_<_ (BAD Requests) se debe pasar 'Ckuck' o 'Dad' como parametro")

class consultaAPI(MethodResource, Resource):
    @doc(description="""GET: Se devolverá un chiste aleatorio si no se pasa ningún path param.
                        Genera un chiste con probabilidad 0.5 entre Ckuck(https://api.chucknorris.io) y Dad (https://icanhazdadjoke.com/api)""", tags=['Chistes'])
    @marshal_with(mensajeResponseSchema)  # marshalling
    def get(self):
        '''
        Get method represents a GET API method
        '''
        auxRandom = "chuck" if random() <= 0.5 else "dad"
        auxConsulta = consultaChiste(auxRandom)
        return {'message': f'My response {auxConsulta.path} {str(auxConsulta.response.json())}'}

#  Restful way of creating APIs through Flask Restful
class ChistesAPI(MethodResource, Resource):

    @doc(description='POST: guardará en una base de datos el chiste (texto pasado por parámetro)', tags=['Chistes'])
    @use_kwargs(ChistesRequestSchema, location=('form'))
    @marshal_with(mensajeResponseSchema)  # marshalling
    def post(self, **kwargs):
        '''
        Get method represents a GET API method
        '''
        # buscando siguiente id de la lista
        new_id = db.squadCollection.find_one_and_update(filter = { '_id': 'itemId'},
                                                   update = { '$inc': {'seq': 1}}, upsert = True,
                                                   return_document = ReturnDocument.AFTER)
        user = {'_id': new_id['seq'], 
                'chiste': kwargs['chiste']}
        db.squadCollection.insert_one(user)
        return {'message': 'Se creo chiste con id %d'%new_id['seq']}

    @doc(description='actualiza el chiste con el nuevo texto sustituyendo al chiste indicado en el parámetro *number*', tags=['Chistes'])
    @use_kwargs(idUpdate, location=('form'))
    @marshal_with(mensajeResponseSchema)  # marshalling
    def put(self, **kwargs):
        '''
        Get method represents a GET API method
        '''
        # buscando siguiente id de la lista
        putAux = db.squadCollection.find_one_and_update({ '_id': kwargs['_id']}, 
                                                      update = {'$set': {'chiste': kwargs['chiste']}}, upsert = False)
        if putAux:
            putAux = db.squadCollection.find_one({ '_id': kwargs['_id']})
            return {'message': 'Se actualizo chiste %s'%str(putAux)}
        else:
            abort(404, 'NO SE ENCONTRO chiste con id %d'%kwargs['_id'])

    @doc(description='elimina el chiste indicado en el parametro *number*', tags=['Chistes'])
    @use_kwargs(idRequestSchema, location=('form'))
    @marshal_with(mensajeResponseSchema, code=204)
    def delete(self, **kwargs):
        '''
        Get method represents a GET API method
        '''
        # buscando siguiente id de la lista
        elimAux = db.squadCollection.delete_one({ '_id': kwargs['_id']})
        if elimAux.deleted_count:
            return {'message': 'Se elimino chiste con id %d'%kwargs['_id']}
        else:
            abort(404, 'NO SE ENCONTRO chiste con id %d'%kwargs['_id'])



