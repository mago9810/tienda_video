
from funciones_validar_acceso_menu_principal_py import validar_acceso_funcion

from variables_control import db_peliculas

def mostrar_listado_peliculas(usuario):
    if validar_acceso_funcion(usuario['tipo_usuario'], 'Mostrar_listado_peliculas'):
        print("tiene acceso")
        print()
        print("MOSTRAR INVENTARIO DE PELICULAS".center(50))
        print("""===============================""".center(50))
        print()
        print("------------")
        print("INVENTARIO")
        print("------------")
        for pelicula in db_peliculas:  #este recorre la cantidad cajones
            for clave, valor in pelicula.items():
                print(clave," : ", valor)
            print("_____________________________________________________________________________________")

    else:
        print("Acceso denegado")
        # imprimir_menu_principal(usuario)

def ingresar_nueva_pelicula(usuario):
    if validar_acceso_funcion(usuario['tipo_usuario'], 'Ingresar_nueva_pelicula'):
        print("tiene acceso")
    
        opc = 1
        while opc == 1:
            print("INGRESAR UNA NUEVA PELICULA".center(50))
            print("""=======================""".center(50))
            nueva_pelicula={
            'id'         : '',
            'titulo'     : " ",
            'director'   : "",
            'año'        : "",
            'actores'    :  [],
            'genero'     : ["Accion"],
            'descripcion': "",
            'estado'     : '',
            'disponible' : "",
            'cantidad'   : ""
            }

            nueva_pelicula["id"] = input("Ingrese el id de la pelicula: ")
            nueva_pelicula['titulo'] = input("Ingrese el titulo de la pelicula: ")
            nueva_pelicula['director'] = input("Ingrese el director de la pelicula: ")
            nueva_pelicula['año'] = int(input("Ingrese el 'año de la pelicula: "))
            nueva_pelicula['actores'] = input("Ingrese los actores de la pelicula: ")
            nueva_pelicula['genero'] = input("Ingrese el genero de la pelicula: ")
            nueva_pelicula['descripcion'] = input("Ingrese la descripcion de la pelicula: ")
            nueva_pelicula['estado' ] = input("Ingrese el estado de la pelicula: ")
            nueva_pelicula['disponible'] = input("Ingrese la disponibilidad de la pelicula: ")
            nueva_pelicula['cantidad'] = int(input("Ingrese la cantidad de la pelicula: "))

            print(nueva_pelicula)

            db_peliculas.append(nueva_pelicula)
            opc = int(input("""
            "---------------------------"
            1. incertar una nueva pelicula
            2. Salir y consultar
            "---------------------------"
                
            """))
    else:
        print("Acceso denegado")
        # imprimir_menu_principal(usuario)

def consulta_pelicula(usuario):
    if validar_acceso_funcion(usuario['tipo_usuario'], 'Consulta_pelicula'):
        print("tiene acceso")
        opc_llenar_lista = 1
        lista_busqueda = []
        print("CONSULTAR UNA PELICULA".center(50))
        print("""=======================""".center(50))

        while opc_llenar_lista == 1:
            id_pelicula = input("Ingrese el id, titulo, o director de la pelicula: ")
            lista_busqueda.append(id_pelicula)
            # print(lista_busqueda)
            opc_llenar_lista = int(input("""
            "---------------------------"
            1. incertar un nuevo ID
            2. Salir y consultar
            "---------------------------"
                """.center(50)))
            print("---------------------------")
        print("DISPONIBILIDAD DE PELICULAS")
        for id_buscado in lista_busqueda:
            for pelicula in db_peliculas:
                if id_buscado in pelicula.values():
                    print("___________________________")
                    print(f"""ID    : {pelicula['id']}""")
                    print(f"""Titulo: {pelicula['titulo']}""")
                    print(f"""Estado: {pelicula['estado']}""")
                    print("___________________________")
                else:
                    continue
    else:
        print("Acceso denegado")
        # imprimir_menu_principal(usuario)

def modificar_pelicula(usuario):

    if validar_acceso_funcion(usuario['tipo_usuario'], 'modificar_pelicula'):
        print("tiene acceso")
        print("""MODIFICAR UNA PELICULA DEL INVENTARIO""".center(50))
        print("""====================================""".center(50))
        id_pelicuala_modificar = input("""
        ------------------------------------------------
        Ingrese al Id de la pelicula que desea modificar: 
        ------------------------------------------------
        """)
        for pelicula in db_peliculas:
            if id_pelicuala_modificar == pelicula["id"]:
                pelicula["id"] = input("Ingrese el nuevo id: ")
                print("estoy en la db de peliculas")
                print("pelicula modificada correctamente")
            else:
                continue
            print(db_peliculas)      


    else:
        print("Acceso denegado")
        # imprimir_menu_principal(usuario)

def eliminar_pelicula(usuario):
    if validar_acceso_funcion(usuario['tipo_usuario'], 'eliminar_pelicula'):
        print("tiene acceso")

        print("""ELIMINAR UNA PELICULA DEL INVENTARIO""".center(50))
        print("""====================================""".center(50))
        id_pelicuala_eliminar = input("""
        ------------------------------------------------
        Ingrese al Id de la pelicula que desea eliminar: 
        ------------------------------------------------
        """)
        for pelicula in db_peliculas:
            if id_pelicuala_eliminar == pelicula["id"]:
                db_peliculas.remove(pelicula)
                print("pelicula removida del inventario de peliculas")
            else:
                continue
    else:
        print("Acceso denegado")
        # imprimir_menu_principal(usuario)


