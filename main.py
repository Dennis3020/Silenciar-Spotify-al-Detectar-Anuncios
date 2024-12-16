from trackDetector import ejecutar

def contenidoMenu():
    """
    Imprime un menu con las opciones disponibles para el usuario.
    """
    
    print(f"""
      ###################################################################
      ###################################################################
    ##                                                                   ##
    ##    Menu:                                                          ##
    ##        1) Iniciar el gestionador de anuncios de spotify.          ##
    ##        2) Cerrar programa.                                        ##
    ##                                                                   ##
      ###################################################################
      ###################################################################
            """)

def opcionesMenu():
    """
    Solicita al usuario que seleccione una opcion del menu.

    Valida la opcion ingresada y determina si se debe
    iniciar el gestor de anuncios o cerrar el programa.
    """ 
    while True:
        try:
            user_choice = int(input('Ingrese una opcion: '))
            if user_choice in [1, 2]:
                return user_choice
            else:
                print('Por favor, elija un valor valido (1 o 2).')
        except ValueError:
            print("El valor ingresado no es un numero.")

def ejecutarOpcion(opcion):
    """
    Ejecuta la accion correspondiente segun la opcion ingresada por el usuario.

    Si la opcion es 1, se ejecutara el gestor de anuncios de spotify.
    Si la opcion es 2, se finalizara el programa.
    """
    if opcion  == 1:
        ejecutar()
    elif opcion == 2:
        return True
            
if __name__ == "__main__":
    """
    Punto de anexo del codigo, Imprime el menu principal e
    gestiona las opciones del usuario para iniciar el gestor de anuncios
    o finalizar el programa.
    """
    while True:
            contenidoMenu()
            user_choice = opcionesMenu()
            if ejecutarOpcion(user_choice):
                break
 
