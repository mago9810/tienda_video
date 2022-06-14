
from multiprocessing.spawn import import_main_path

from funciones_validar_acceso_menu_principal_py import validar_acceso_funcion

from variables_control import db_usuarios

def mostrar_listado_clientes(usuario):
    if validar_acceso_funcion(usuario['tipo_usuario'], 'mostrar_listado_clientes'):
        print("tiene acceso")
        print()
        print("MOSTRAR LA LISTA DE CLIENTES".center(50))
        print("""===============================""".center(50))
        print()
        print("------------")
        print("LISTADO DE CLIENTES")
        print("------------")
        for usuario in db_usuarios:  
            for clave, valor in usuario.items():
                print(clave," : ", valor)
            print("_____________________________________________________________________________________")
        print()
    else:
        print("Acceso denegado")
        imprimir_menu_principal(usuario)

def ingresar_nuevo_cliente(usuario):
    if validar_acceso_funcion(usuario['tipo_usuario'], 'ingresar_nuevo_cliente'):
        print("tiene acceso")
        opc = 1
        while opc == 1:
            print("INGRESAR UN NUEVO CLIENTE".center(50))
            print("""=======================""".center(50))
            # Crea un directorio
            nuevo_cliente={
            'usuario': '',
            'contraseña': '',
            'id': "",
            'nombre': "",
            'correo': "",
            'edad': 39,
            'direccion':  '',
            'estado_civil': '',
            'celular': ['', ''],
            'estado': '',
            'tipo_usuario': ''
            }                
            nuevo_cliente["usuario"] = input("Ingrese el nombre del usuario: ")
            nuevo_cliente['contraseña'] = input("Ingrese la contraseña del usuario: ")
            nuevo_cliente['id'] = int(input("Ingrese el id del usuario: "))
            nuevo_cliente['nombre'] = input("Ingrese el nombre del usuario: ")
            nuevo_cliente['correo'] = input("Ingrese el e-mail del usuario: ")
            nuevo_cliente['edad'] = int(input("Ingrese la edad del usuario: "))
            nuevo_cliente['direccion'] = input("Ingrese la direccion del usuario: ")
            nuevo_cliente['estado_civil' ] = input("Ingrese el estado civil del usuario: ")
            nuevo_cliente['celular'] = input("Ingrese el celular del usuario: ")
            nuevo_cliente['estado'] = (input("Ingrese el estado del usuario: "))
            nuevo_cliente['tipo_usuario'] = (input("Ingrese el tipo de usuario: "))
            print(nuevo_cliente)

            db_usuarios.append(nuevo_cliente)
            print(id(db_usuarios))
            print(db_usuarios)
            opc = input("""
            "---------------------------"
            1. incertar una nueva pelicula
            2. Salir y consultar
            # "---------------------------"
                    """)
    else:
        print("Acceso denegado")
        imprimir_menu_principal(usuario)

def modificar_cliente(usuario):
    if validar_acceso_funcion(usuario['tipo_usuario'], 'modificar_cliente'):
        print("tiene acceso")
        print("""MODIFICAR ID CLIENTE""".center(50))
        print("""====================================""".center(50))
        id_cliente_modificar = int(input("""
        ------------------------------------------------
        Ingrese la cedula del cliente que desea modificar: 
        ------------------------------------------------
        """))
        for cliente in db_usuarios:
            if id_cliente_modificar == cliente["id"]:
                cliente["id"] = int(input("Ingrese el nuevo id"))
                print("pelicula modificada correctamente")
            else:
                continue
            # print(db_usuarios)
    else:
        print("Acceso denegado")
        imprimir_menu_principal(usuario)

def eliminar_cliente(usuario):
    if validar_acceso_funcion(usuario['tipo_usuario'], 'eliminar_cliente'):
        print("tiene acceso")
        print("""ELIMINAR UN CLIENTE""".center(50))
        print("""====================================""".center(50))
        id_cliente_eliminar = int(input("""
        ------------------------------------------------
        Ingrese la cedula del cliente que desea eliminar: 
        ------------------------------------------------
        """))
        for cliente in db_usuarios:
            if id_cliente_eliminar == cliente["id"]:
                db_usuarios.remove(cliente)
                print("El cliente fue removido correctamente")
            else:
                continue
    else:
        print("Acceso denegado")
        # imprimir_menu_principal(usuario)

def consulta_cliente(usuario):
    if validar_acceso_funcion(usuario['tipo_usuario'], 'consulta_cliente'):
        print("tiene acceso")
        opc_llenar_lista = 1
        lista_busqueda = []
        print("CONSULTAR LA LISTA DE CLIENTES".center(50))
        print("""=======================""".center(50))
        while opc_llenar_lista == 1:
            cedula = int(input("Ingrese la cedula del cliente: "))
            lista_busqueda.append(cedula)
            # print(lista_busqueda)
            opc_llenar_lista = int(input("""
            "---------------------------"
            1. incertar una nueva cedula
            2. Salir y consultar
            "---------------------------"
            """.center(50)))
        print("---------------------------")
        print("LISTA DE CLIENTES CONSULTADOS")
        for id_buscado in lista_busqueda:
            for cliente in db_usuarios:
                if id_buscado in cliente.values():
                    print("___________________________")
                    print(f"""Cedula    : {cliente['id']}""")
                    print(f"""Titulo: {cliente['nombre']}""")
                    print(f"""Estado: {cliente['estado']}""")
                    print("___________________________")
                        
                else:
                    continue
    else:
        print("Acceso denegado")
    
    imprimir_menu_principal(usuario)