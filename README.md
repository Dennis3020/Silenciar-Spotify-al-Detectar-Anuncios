# Silenciar Spotify al Detectar Anuncios

Este proyecto es una herramienta desarrollada en Python que silencia automáticamente Spotify cuando detecta un anuncio, proporcionando una experiencia de usuario más agradable.

## Características
- Detecta anuncios en Spotify utilizando la API de Spotify.
- Silencia automáticamente el audio del sistema cuando se detecta un anuncio.


## Requisitos
Para ejecutar este proyecto necesitas tener instalado:

- Python 3.8 o superior
- Las siguientes bibliotecas de Python:
  - `spotipy`
  - `pycaw`
  - `requests`

## Instalación
1. Clona este repositorio o descarga el código fuente:

```
git clone https://github.com/tu-usuario/silenciar-spotify.git
cd silenciar-spotify
```

2. Instala las dependencias:

```
pip install pycaw requests spotipy
```
>Se dejó un archivo requirements.cmd que automatiza la instalación de las bibliotecas necesarias para el correcto funcionamiento del proyecto. 
3. Configura el archivo `config.json` ya incluido en el proyecto. Necesitarás las claves de Spotify para completar este paso:
 
   - Regístrate o inicia sesión en el [Panel de Desarrolladores de Spotify](https://developer.spotify.com/dashboard/applications), siempre con la cuenta utilizada en la PC.
   - Crea una nueva aplicación en el panel y copia el `Client ID` y el `Client Secret`.
   - En el archivo `config.json`, reemplaza los valores con tus claves:
     ```
     {
         "CLIENTID": "tuclientid",
         "CLIENTSECRET": "tuclientsecret",
         "REDIRECTURI": "turedirecturi"
     }
     ```
   - Asegúrate de que el `REDIRECTURI` coincida con el configurado en la aplicación de Spotify.
  >[!NOTE]
  > REDIRECTURI, recomendado localhost, ejemplo: http://localhost:8000/callback
## Uso

1. Ejecuta el script principal:

```
python main.py
```

2. Sigue las instrucciones en pantalla. Se abrirá una página en Spotify donde deberás autenticarte y validar el uso del programa.

3. Deja que el programa se ejecute en segundo plano mientras usas Spotify. El audio se silenciará automáticamente durante los anuncios.

## Personalización
Puedes ajustar ciertos parámetros, como los intervalos de verificación de anuncios, modificando las configuraciones en el código fuente o en el archivo `config.json`.


**Nota:** Este proyecto es únicamente con fines educativos y no está afiliado a Spotify.
