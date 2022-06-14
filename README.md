# pruebaSQUAD (Jorge Mario Carrasco Ortiz)
Repositorio para integración de servicios icanhazdadjoke y chucknorris

Pasos para la integración del proyecto:

* Definición de proyecto
	- Definición de carpetas estandar de API usando flask-restful **(DONE)**https://flask-restful.readthedocs.io/en/latest/intermediate-usage.html#project-structure)
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
* Construcción de archivo readme.md con la explicación 


# ¿ Cómo he ejecutado el proyecto?

* 


# Preguntas del punto 2 (¿Qué repositorio utilizarias?)

PostgreSQL, MariaDB, Casandra, MongoDB, ElasticSearch, Oracle, SQL Server.

## Razona tú respuesta.

* Utilizaria una base de datos noSQL debido a que las dos fuentes de datos (Chuck y Dad) son heterogeneas, es decir los campos no son iguales, adicionalmente puede ser que exista más de una categoria 

## Crea la sentencia para crear la BBDD y el modelo de datos requeririas

* La creación de la base de datos se puede ver en:  
* Adicionalmente se personaliza el inicio de mongo db con la creción y configuración incial se puede ver en:
* Finalmente es utilizada y almacenado los chistes usando los endpoint que se pueden ver en: 

## Lo mismo que el punto anterior (si lo hiciste con SQL) pero para un repositorio noSQL

* No aplica dado que lo hice con MongoDB

