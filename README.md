# pruebaSQUAD (Jorge Mario Carrasco Ortiz)
Repositorio para integración de servicios icanhazdadjoke y chucknorris

Pasos para la integración del proyecto:

* Definición de proyecto
	- Configuración de repositorio y configuración de clave SSH para usar github **(DONE)**
	- Definición de carpetas estandar de API usando flask-restful **(DONE)** https://flask-restful.readthedocs.io/en/latest/intermediate-usage.html#project-structure)
	- Configuración del proyecto para crea un Swagger para documentar el API **(DONE)**
	- Definición de servicios de bases de datos que se van a usar **(DONE)**
	
* Intregración de bases de datos
	* Creación de servicio MongoDB (icanhazdadjoke)
		- Configuración del docker para creación de la base de datos **(DONE)**
		- Configuración del API conectarse con MongoDB **(DONE)**
	
	* Construcción de API de chsites
		- Construcción de función para lanzar chucknorris **(DONE)**
		- Construcción de función para lanzar icanhazdadjoke **(DONE)**
		- Construcción de end-point para lanzar final (si se envía el path param habrá que comprobar si tiene el valor “Chuck” o el valor “Dad”) **(DONE)**
		- Construcción de exepción en caso de que no sea "Chuk" o "Dad" **(DONE)**
		- Construcción de metodo post para guardar chiste **(DONE)**
		- Construcción de metodo put para actualizar chiste **(DONE)**
		- Construcción de metodo delte para eliminar chiste **(DONE)**
	* Construcción de ENDPOINT MATEMÁTICO
		- GET: Endpoint al que se le pasará un query param llamado “numbers” con una lista de números enteros. La  respuesta de este endpoint debe ser el mínimo común múltiplo de ellos. **(DONE)**
		- GET: Endpoint al que se le pasará un query param llamado “number” con un número entero. La respuesta será ese número + 1. **(DONE)**
* Crear pruebas unitarias. 
* Construcción de archivo readme.md con la explicación **(DONE)**


# ¿ Cómo he ejecutado el proyecto?

Para la elaboración de este proyecto se siguio las lista de requerimientos que se observa en el punto anterior, adicionalmente utilice un servidor local con las siguientes caracteristicas: 

 ![Servidor](/screenshots/Captura_server.PNG?raw=true)

Este servidor esta usando la ip local http://192.168.90.40/, realice la construcción de los siguientes directorios: 

![Servidor](/screenshots/Captura_carpetas.PNG?raw=true)


Se definieron los siguientes servicios utilizando docker-compose: 

```yaml
version: '3.8'
services:  
    dbnosql:
        image: mongo:latest
        environment:
            MONGO_INITDB_DATABASE: apisquad
            MONGO_INITDB_ROOT_PASSWORD: vagrant3
            MONGO_INITDB_ROOT_USERNAME: admin
        command: mongod --port 28108
        volumes:
            - ./init-mongo.js:/docker-entrypoint-initdb.d/mongo-init.js:ro
            - ./mongo_backup:/data/backup
            - mongodataSquad:/data/db
        ports:
            - 28108:28108
    api-service:
        build: ./apiSQUAD/
        volumes: 
            - ./apiSQUAD/:/usr/src/app/
        ports: 
            - 5004:5004
        environment: 
            PORT: 5004
            FLASK_DEBUG: 1

volumes:
  mongodataSquad:
    driver: local
```

La siguiente fue la configuración del `Dockerfile` del servicio **api-service**:

```
FROM python:latest
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/

EXPOSE 5004
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python", "app.py"]
```

Con los siguientes paquetes definidos en el `requirements`: 

```
Flask
Flask-PyMongo
requests
flask-restful
flask-apispec==0.11.0
invoke
```


Defini utilizar la libreria **flask_restful** para la definición de los enpoints de la API, **flask_apispec** para generar la documentación en Swagger(el cual se puede ver en https://jorajora.github.io/pruebaSQUAD/) y adicionalmente utilic el paquete **pymongo** para conectarme a la base de datos de MongoDB que desplegue para el proyecto.


# Preguntas del punto 2 (¿Qué repositorio utilizarias?)

PostgreSQL, MariaDB, Casandra, MongoDB, ElasticSearch, Oracle, SQL Server.

**Respuesta**: Decidí utilizar MongoDB dado el siguiente ranking de bases de datos no relacionales (https://db-engines.com/en/ranking/document+store), en este ranking se mide, entre otras cosas, el número de menciones del sistema sobre los sitios web, por esta razón es casi probable que cualquier dificultad pueda ser encontrada en los foros y hace un poco más ágil el desarrollo. Sin embargo, considero que la elección depende del ambiente de desarrollo en el que se esté trabajando es muy probable, por ejemplo, que si el cliente tiene Azure uno termine usando CosmoDB.

## Razona tú respuesta.

* Utilizaría una base de datos NoSQL debido a que las dos fuentes de datos (Chuck y Dad) son heterogéneas, es decir los campos no son iguales, adicionalmente puede ser que exista más de una categoría y/o existan campos que sea mejor guardarlos como tipo lista. 

## Crea la sentencia para crear la BBDD y el modelo de datos requeririas

* La creación y parametrización de la base de datos se puede ver en la configuración del docker: https://github.com/JoraJora/pruebaSQUAD/blob/main/docker-compose.yml  
* Adicionalmente se personaliza el inicio de mongo db con la creación y configuración inicial se puede ver en:  https://github.com/JoraJora/pruebaSQUAD/blob/main/init-mongo.js
* Finalmente es consultada y almacenada usando los endpoint que se pueden ver en: https://github.com/JoraJora/pruebaSQUAD/blob/main/apiSQUAD/resources/chistes.py

## Lo mismo que el punto anterior (si lo hiciste con SQL) pero para un repositorio noSQL

* No aplica dado que lo hice con MongoDB

