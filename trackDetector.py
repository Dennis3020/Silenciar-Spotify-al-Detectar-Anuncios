import requests

import json

from spotipy import Spotify

from spotipy.oauth2 import SpotifyOAuth, SpotifyOauthError

from adSilencer import mutearSpotify

import time

def obtenerInfoUsuario():
    
    """
    Esta función carga las credenciales desde un archivo `config.json` y crea un objeto
    de autenticación para interactuar con la API de Spotify. Esto permite obtener la
    información del usuario actual, como la canción que está reproduciendo.
    """
    
    with open('config.json') as config_file:
        config = json.load(config_file)
        
    return Spotify(auth_manager=SpotifyOAuth(
        client_id=config["CLIENTID"],
        client_secret=config["CLIENTSECRET"],
        redirect_uri=config["REDIRECTURI"],
        scope="user-read-currently-playing"))


def obtenerCancionActual():
    
    """
    Esta función interactúa con la API de Spotify para obtener información sobre lo que
    el usuario está reproduciendo actualmente. Retorna un diccionario con los detalles de la canción
    si se está reproduciendo un track, o identifica si es un anuncio o si no hay nada en reproducción.
    """
    sp = obtenerInfoUsuario()
    try:
        currentUser = sp.current_user_playing_track()
        if not currentUser:
            return "Error al obtener informacion de la cancion, es probable que no se este reproduciando nada.", 2
    except requests.exceptions.ConnectionError:
        return "Error de conexion."
    except SpotifyOauthError:
        return "Error de autenticación:\n las credenciales de cliente son incorrectas o están incompletas.\n Verifica el archivo 'config.json' y asegúrate de que los valores de\n CLIENTID, CLIENTSECRET y REDIRECTURI sean correctos.", 2 
         

    trackType = currentUser["currently_playing_type"]

    if(trackType == "track"):

        trackId= currentUser["item"]["id"]
        trackName= currentUser["item"]["name"]
        link = currentUser["item"]["external_urls"]["spotify"]

        cancionInfo ={
            "name": trackName,
            "link": link
            }

        return cancionInfo, 0

    
    elif(trackType == "ad"):
        return "La cancion actual es un anuncio", 1
    

def ejecutar():

    """
    Esta función implementa un bucle continuo para gestionar la reproducción de Spotify.
    Monitorea la canción actual y, en función de su estado (normal, anuncio, o error crítico),
    ejecuta acciones específicas como silenciar o detener la ejecución.
    """
    Funciona=False
    contIntentos = 0
    while True:
        try:
            cancionActual,mute = obtenerCancionActual()
            if(mute==2):
                print(cancionActual)
                return
            mutearSpotify(mute)
            time.sleep(4)
            if not Funciona:
                print("El programa esta funcionando correctamente.")
                Funciona = True  

        except KeyError:
            contIntentos+=1
            if(contIntentos == 10):
                print("Es posible que el token haya expirado")
                return
            pass
        except ValueError:
            contIntentos+=1
            pass
