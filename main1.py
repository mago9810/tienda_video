from funciones_validar_acceso_menu_principal_py import validar_credenciales
# from variables_control import MENU,CLIENTE,EMPLEADO
from funcion_imprimir_menu_principal import imprimir_menu_principal

def main():
    opc = 1
    username = input(f"ingrese el usuario:  ")
    clave = input(f"ingrese su clave:  ")
    usuario = validar_credenciales(username, clave)
    if len(usuario) == 0:
        # Las credenciales no son validas
        print(f"""{username} o {clave} no existen""")
    else:
        # Las credenciales son validas y se imprime un menu acorde al perfil
        while opc == 1:                                 #
            imprimir_menu_principal(usuario)            #
            print("""Deseas abandonar el sistema?
            1. Para hacer una nueva operacion
            2. Para salir del sistema
            """)       # Inclui un while para que pueda hacer varias operaciones o consultas por validacion de credenciales
            opc = int(input())
            if opc != 1:                                #
                print("""                               
                Gracias por utilizar el sistema.        
                Hasta pronto
                """)                                    #
