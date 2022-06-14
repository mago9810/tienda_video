
from multiprocessing.spawn import import_main_path

from funciones_validar_acceso_menu_principal_py import validar_acceso_funcion
from variables_control import db_usuarios, db_facturas,db_peliculas

def mostrar_listado_facturas(usuario):

    if validar_acceso_funcion(usuario['tipo_usuario'], 'mostrar_listado_facturas'):
        print("tiene acceso")
        print()
        print("MOSTRAR LA LISTA DE FACTURAS".center(50))
        print("""===============================""".center(50))
        print()
        print("------------")
        print("LISTADO DE FACTURAS")
        print("------------")
        for factura in db_facturas:  #este recorre la cantidad cajones
            for clave, valor in factura.items():
                print(clave," : ", valor)
            print("_____________________________________________________________________________________")
        print()


    else:
        print("Acceso denegado")
        # imprimir_menu_principal(usuario)

def ingresar_nueva_factura(usuario):
    opc = 1
    while opc == 1:
        print("INGRESAR UNA NUEVA FACTURA".center(50))
        print("""=======================""".center(50))
        # Crea un directorio
        nueva_factura={
            'No fact': '',
            'id_cleinte': '',
            'id peliculas alquiladas': ["",""],
            'cant. peliculas alquiladas': "",
            'costo un itario':"",
            'costo total': "",
        }                
        nueva_factura['No fact'] = input("Ingrese el numero de la factura: ")
        nueva_factura['id_cleinte'] = input("Ingrese el id del cliente: ")
        nueva_factura['id peliculas alquiladas'] = int(input("Ingrese el id de la pelicula: "))
        nueva_factura['cant. peliculas alquiladas'] = input("cantidad de peliculas ingresadas: ")
        nueva_factura['costo un itario'] = input("precio unitario: ")
        nueva_factura['costo total'] = int(input("costo total: "))
        print(nueva_factura)

        db_facturas.append(nueva_factura)
        #
        # print(id(db_facturas))
        print(db_facturas)
        opc = int(input("""
        "---------------------------"
        1. incertar una nueva factura
        2. Salir y consultar
        # "---------------------------"
                 """))

def consulta_factura(usuario):
    opc_llenar_lista = 1
    lista_busqueda = []
    print("CONSULTAR LA LISTA DE FACTURAS".center(50))
    print("""=======================""".center(50))
    while opc_llenar_lista == 1:
        Id_factura = (input("Ingrese el Id de una factura: "))
        lista_busqueda.append( Id_factura)
        # print(lista_busqueda)
        opc_llenar_lista = int(input("""
        "---------------------------"
        1. incertar un nuevo id de factura
        2. Salir y consultar
        "---------------------------"
        """.center(50)))
    print("---------------------------")
    print("LISTA DE FACTURAS CONSULTADAS")
    for id_buscado in lista_busqueda:
        for factura in db_facturas:
            if id_buscado in factura.values():
                print("___________________________")
                print(f"""No fact    : {factura['No fact']}""")
                print(f"""id_cleinte: {factura['id_cleinte']}""")
                print(f"""id peliculas alquiladas: {factura['id peliculas alquiladas']}""")
                print(f"""cant. peliculas alquiladas    : {factura['cant. peliculas alquiladas']}""")
                print(f"""costo un itario: {factura['costo un itario']}""")
                print(f"""costo total: {factura['costo total']}""")
                print("___________________________")
                    
            else:
                continue

def modificar_factura(usuario):
    print("""MODIFICAR ID FACTURA""".center(50))
    print("""====================================""".center(50))
    id_factura_modificar = (input("""
    ------------------------------------------------
    Ingrese el Id de la factura que desea modificar: 
    ------------------------------------------------
    """))
    for factura in db_facturas:
        if id_factura_modificar == factura['No fact']:
            factura['No fact'] = input("Ingrese el nuevo id")
            print("pelicula modificada correctamente")
        else:
            continue

def eliminar_factura(usuario):
    print("""ELIMINAR UNA FACTURA""".center(50))
    print("""====================================""".center(50))
    id_factura_eliminar = (input("""
    ------------------------------------------------
    Ingrese el Id de la factura que desea eliminar: 
    ------------------------------------------------
    """))
    for factura in db_facturas:
        if id_factura_eliminar == factura['No fact']:
            db_facturas.remove(factura)
            print("El cliente fue removido correctamente")
        else:
            continue
