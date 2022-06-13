# pruebaSQUAD
Repositorio para integración de servicios icanhazdadjoke y chucknorris

Pasos para la integración de los repositorios
* Definición de proyecto
	- Definición de carpetas estandar de API usando flask-restful ()https://flask-restful.readthedocs.io/en/latest/intermediate-usage.html#project-structure)
	- Configuración del proyecto para crea un Swagger para documentar el API (Done)
	- Definición de servicios de bases de datos que se van a usar. 
	
* Intregración de bases de datos
	* Creación de servicio MongoDB (icanhazdadjoke)
		- Configuración del docker para creación de la base de datos
		- Configuración del API conectarse con MongoDB
	* Creación de servicio Microsoft SQL-SERVER (chucknorris)
	* Construcción de end-point para descargar chucknorris
	* Construcción de end-point para descargar icanhazdadjoke

* Creación de end-point para hacer consumo de las dos bases de datos

* Crear pruebas unitarias. 
