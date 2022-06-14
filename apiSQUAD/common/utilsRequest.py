import requests
from flask import abort

def chuckRandom():
	x = requests.get('https://api.chucknorris.io/jokes/random')
	if x.status_code == 200:
		return(x)
	else:
		abort(400, '_>_<_ (BAD Requests) No se pudo descargar de chucknorris')

def dadRandom():
	x = requests.get('https://icanhazdadjoke.com/',  headers={'Accept':'application/json'})
	if x.status_code == 200:
		return(x)
	else:
		abort(400, '_>_<_ (BAD Requests) No se pudo descargar de icanhazdadjoke')


class consultaChiste:
    def __init__(self, path):
        """Creación clase para lanzar consultas a los API de referencia
        Construye un objeto con la información recueprada de la consulta
        
        Parámetros:
        path -- Nombre del servicio a consultar
    
        Excepciones:
        Ninguna
        """       
        self.path = self._is_valid_path(path)
        self.response = chuckRandom() if path.lower() == 'chuck' else dadRandom()

    def _is_valid_path(self, path):
        if not path.lower() in ["chuck", "dad"]:
            abort(400, "_>_<_ (BAD Requests) se debe pasar 'Ckuck' o 'Dad' como parametro")
        return path




