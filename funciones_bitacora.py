from multiprocessing.spawn import import_main_path

from datetime import date, datetime,timedelta

from funciones_validar_acceso_menu_principal_py import validar_acceso_funcion

from variables_control import db_usuarios, db_facturas,db_peliculas,lista_alquileres


def consulta_pelicula_registo():   #interno
    opc_llenar_lista = 1
    lista_busqueda = []
    lista_verificada = []
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
                print("id y pelicula iguales")
                # print("___________________________")
                # print(f"""ID    : {pelicula['id']}""")
                # print(f"""Titulo: {pelicula['titulo']}""")
                # print(f"""Estado: {pelicula['estado']}""")
                # print("___________________________")
                lista_verificada.append(id_buscado)
            else:
                continue
    print(lista_verificada)
    return lista_verificada

def consulta_nombre_cliente_alquiler(i):  #interno
    id_cliente = i
    # print(type(id_cliente))
    # print(id_cliente)
    for cliente in db_usuarios:
        # print(cliente)
        if cliente['id'] == id_cliente:
            # print(cliente['id'])
            # print(type(cliente['id']))
            # print(id_cliente)
            # print(type(id_cliente))
            nombre_cliente = cliente['nombre']
            # print(nombre_cliente)
        # else:
        #     nombre_cliente = "perro"
    return nombre_cliente

def consulta_nombre_pelicula_alquiler(j):   #interno
    id_pelicula = j
    id_pelicula = str(id_pelicula)
    # print(type(id_pelicula))
    # print(id_pelicula)
    for pelicula in db_peliculas:
        if pelicula['id'] == id_pelicula:
            # print(type(pelicula['id']))
            # print(type( id_pelicula))
            titulo_peli = pelicula['titulo']
            # print(titulo_peli)

    # print(titulo_peli)
    return titulo_peli

def calculo_id_registro():  #interno
    cant = int(len(lista_alquileres))
    cant += 1
    return cant

def calculo_fechas(): #Interno
    fechas = {
        'fecha prestamo' : '',
        'dias de prestamo': 3,
        'costo alquiler': 3000,
        'fecha retorno':'',
        'dias retraso' : '',
        'multa':'',
        'costo del alquiler': '',
    }
    fecha_alquiler = date(2022,5,10)   #AQUI TENGO QUE INGRESAR LA FUNCION PARA CAPTURAR LA FECHA 
    fecha_hoy = date.today()
    # fecha_retorno = (fecha_alquiler.day + 3)
    td = timedelta(days=3)
    fecha_retorno = fecha_alquiler + td
    diferencia =  (fecha_hoy - fecha_alquiler)
    dias_retraso = diferencia.days - 3
    multa = dias_retraso * 1000    

    fechas['fecha prestamo'] = str(fecha_alquiler)
    fechas['fecha retorno'] = str(fecha_retorno)
    fechas['dias retraso'] = dias_retraso
    fechas['multa'] = multa
    # print(fechas)
    return fechas

def llenar_registro(i,j): #interno
    fechas = calculo_fechas()
    # print(fechas)
    nuevo_regitro={
            'id registro': '',
            'id pelicula': '',
            'titulo': '',
            'cedula': "",
            'nombre': "",
            'costo del alquiler': 3000,
            'fecha_alquiler': "",
            'dias de alquiler': 3,
            'fecha de retorno' : '',
            'Dias de retrazo' : '',
            'Multa': '',
            }   
    nuevo_regitro['id registro'] = calculo_id_registro()
    nuevo_regitro['id pelicula'] = i
    nuevo_regitro['cedula'] = j
    nuevo_regitro['titulo'] = consulta_nombre_pelicula_alquiler(i) 
    nuevo_regitro['nombre'] = consulta_nombre_cliente_alquiler(j)
    nuevo_regitro['fecha_alquiler'] = fechas['fecha prestamo']
    nuevo_regitro['fecha de retorno'] = fechas['fecha retorno']
    nuevo_regitro['Dias de retrazo'] = fechas['dias retraso']
    nuevo_regitro['Multa'] = fechas['multa']

    return nuevo_regitro

def mostrar_listado_registros(usuario):
    if validar_acceso_funcion(usuario['tipo_usuario'], 'mostrar_listado_registros'):
        print("tiene acceso")
        print()
        print("MOSTRAR LA LISTA ALQUILERES".center(50))
        print("""===============================""".center(50))
        print()
        print("------------")
        print("LISTADO DE ALQUILERES")
        print("------------")
        for alquiler in lista_alquileres:  #este recorre la cantidad cajones
            for clave, valor in alquiler.items():
                print(clave," : ", valor)
            print("_____________________________________________________________________________________")
        print()
    else:
        print("Acceso denegado")
        # imprimir_menu_principal(usuario)

def ingresar_nuevo_regitro(usuario):
    registro = {
            'Id_cliente': '',
            'Id Pelicula': '',
        }
    registro['Id_cliente'] = int(input('Ingrese el id del cliente: '))
    registro['Id Pelicula'] = consulta_pelicula_registo()

    id_cliente = registro['Id_cliente']

    for i in registro['Id Pelicula']:

        registro_nuevo = llenar_registro(i,id_cliente)
        lista_alquileres.append(registro_nuevo)

    print(lista_alquileres)

def consulta_registro(usuario):
    if validar_acceso_funcion(usuario['tipo_usuario'], 'consulta_registro'):
        print("tiene acceso")
        opc_llenar_lista = 1
        lista_busqueda = []
        print("CONSULTAR LA LISTA DE REGISTROS".center(50))
        print("""=======================""".center(50))
        while opc_llenar_lista == 1:
            registro = int((input("Ingrese el id del registro: ")))
            lista_busqueda.append(registro)
            opc_llenar_lista = int(input("""
            "---------------------------"
            1. incertar un nuevo id registro
            2. Salir y consultar
            "---------------------------"
            """.center(50)))
        print("---------------------------")
        print("LISTA DE REGISTROS CONSULTADOS")
        for id_buscado in lista_busqueda:
            for registro in lista_alquileres:
                if id_buscado in registro.values():
                    print("___________________________")
                    print(f"""id registro'   : {registro['id registro']}""")
                    print(f"""id pelicula: {registro['id pelicula']}""")
                    print(f"""titulo: {registro['titulo']}""")                  
                    print(f"""cedula: {registro['cedula']}""")
                    print(f"""nombre: {registro['nombre']}""")
                    print(f"""fecha_alquiler: {registro['fecha_alquiler']}""")
                    print(f"""fecha de retorno: {registro['fecha de retorno']}""")            
                    print(f"""Dias de retrazo: {registro['Dias de retrazo']}""")
                    print(f"""'Multa': {registro['Multa']}""")


                    print("___________________________")
                else:
                    continue
    # Variar el ID de una pelicula
    else:
        print("Acceso denegado")
        # imprimir_menu_principal(usuario)

def modificar_registro(usuario):
    if validar_acceso_funcion(usuario['tipo_usuario'], 'modificar_registro'):
        print("tiene acceso")

        print("""MODIFICAR ID ALQUILER""".center(50))
        print("""====================================""".center(50))
        id_registro_modificar = int(input("""
        ------------------------------------------------
        Ingrese la cedula del cliente que desea modificar: 
        ------------------------------------------------
        """))
        for registro in lista_alquileres:
            if id_registro_modificar == registro['id registro']:
                registro['id registro'] = int(input("Ingrese el nuevo id"))
                print("pelicula modificada correctamente")
            else:
                continue
    else:
        print("Acceso denegado")
        # imprimir_menu_principal(usuario)

def eliminar_registro(usuario):
    if validar_acceso_funcion(usuario['tipo_usuario'], 'eliminar_registro'):
        print("tiene acceso")
        print("""ELIMINAR REGISTRO DE UN ALQUILER""".center(50))
        print("""====================================""".center(50))
        id_registro_eliminar = int(input("""
        ------------------------------------------------
        Ingrese el Id de registro que desea eliminar: 
        ------------------------------------------------
        """))
        for registro in lista_alquileres:
            if id_registro_eliminar == registro['id registro']:
                lista_alquileres.remove(registro)
                print("El registro fue removido correctamente")
            else:
                continue
    else:
        print("Acceso denegado")
        # imprimir_menu_principal(usuario)
