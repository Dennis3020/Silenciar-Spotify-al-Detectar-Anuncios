from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume

def mutearSpotify(mutear: bool):
        """
        Esta funcion controla el volumen de la aplicacion spotify segun
        el tipo de contenido que se esta reproduciendo.

        Revisa todas las secciones de audio activas y,
        si encuentra el proceso 'spotify.exe' procede a mutear o desmutear
        segun el valor del parametro 'mutear'.
        """
        secciones = AudioUtilities.GetAllSessions()

        for i in secciones:
            volumen = i._ctl.QueryInterface(ISimpleAudioVolume)
            if i.Process and i.Process.name() == "Spotify.exe":
                volumen.SetMute(mutear, None)
