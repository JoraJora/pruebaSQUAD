from marshmallow import Schema, fields
from flask import abort
from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from math import lcm

class numericSchema(Schema):
    result = fields.Integer(default='Success')

class ListSchema(Schema):
    numbers = fields.List(fields.Integer(), required=True)

#  Restful way of creating APIs through Flask Restful

class sumAPI(MethodResource, Resource):
    @doc(description="""Endpoint al que se le pasará un query param llamado “number” 
        con un número entero. La respuesta será ese número + 1""", tags=['Numeric'])
    @marshal_with(numericSchema) 
    def get(self, number, **kwargs):
        '''
        GET: Endpoint al que se le pasará un query param llamado “number” 
        con un número entero. La respuesta será ese número + 1
        '''
        auxCount = number
        return {'result': number + 1}


class mcmAPI(MethodResource, Resource):
    @doc(description="""Endpoint al que se le pasará un query param llamado “numbers” 
        con una lista de números enteros. La respuesta de este endpoint 
        debe ser el mínimo común múltiplo de ellos""", tags=['Numeric'])
    @use_kwargs(ListSchema, location=('form'))
    @marshal_with(numericSchema)  # marshalling
    def post(self, **kwargs):
        '''
        POST:  Endpoint al que se le pasará un query param llamado “numbers” 
        con una lista de números enteros. La respuesta de este endpoint 
        debe ser el mínimo común múltiplo de ellos
        '''
        auxLcm = lcm(*kwargs['numbers'])
        return {'result': auxLcm}


