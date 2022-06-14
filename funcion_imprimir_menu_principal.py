from funciones_peliculas import consulta_pelicula,mostrar_listado_peliculas,ingresar_nueva_pelicula, modificar_pelicula,eliminar_pelicula
from funciones_clientes import consulta_cliente, mostrar_listado_clientes, modificar_cliente,ingresar_nuevo_cliente,eliminar_cliente
from funciones_facturas import mostrar_listado_facturas,ingresar_nueva_factura,consulta_factura,modificar_factura,eliminar_factura
from funciones_bitacora import consulta_registro, mostrar_listado_registros,ingresar_nuevo_regitro,modificar_registro,eliminar_registro
from variables_control import MENU



def imprimir_menu_principal(usuario) -> None:
    """Imprime el menu principal segun el perfil de usuario

    Args:
        perfil_usuario (str): recibe el pefil del usuario
    """

    item = 1
    print("============================================================")
    print("""    
          MENU PRINCIPAL
          """)
    for opcion in MENU:
        perfiles = opcion['perfiles']
        if usuario['tipo_usuario'] in perfiles:
            # print(f"{item}. {opcion['opcion']}")  ___ Retire del codigo la variable estatica "item" para que nos dijera la opcion a marcar
            print(f"{opcion['opcion']}")
            # item+=1                                # y pudiera entrar a al menu correcto
    print("============================================================")
    opcion = input("\nIndique la operacion de desea realizar: ")
    if opcion == '1':
        pass
    # elif opcion == '2':
    #     alquilar_peliculas(usuario)
    # elif opcion == '3':
    #     registrar_clientes(usuario)

#--------------------------------------------------------------------
    elif opcion == '5':
        mostrar_listado_peliculas(usuario) #Funcionando

    elif opcion == '6':
        ingresar_nueva_pelicula(usuario)#Funcionando

    elif opcion == '8':
        consulta_pelicula(usuario)#Funcionando

    elif opcion == '9':
        modificar_pelicula(usuario)#Funcionando

    elif opcion == '10':
        eliminar_pelicula(usuario)#Funcionando

#--------------------------------------------------------------------

    elif opcion == '11':
        mostrar_listado_clientes(usuario)#Funcionando    

    elif opcion == '12':
        ingresar_nuevo_cliente(usuario)#Funcionando    

    elif opcion == '13':
        consulta_cliente(usuario)#Funcionando    

    elif opcion == '14':
        modificar_cliente(usuario)#Funcionando  

    elif opcion == '15':
        eliminar_cliente(usuario)#Funcionando  

#--------------------------------------------------------------------

    elif opcion == '16':
        mostrar_listado_registros(usuario)#Funcionando    #ok

    elif opcion == '17':
        ingresar_nuevo_regitro(usuario)#Funcionando    

    elif opcion == '18':
        consulta_registro(usuario)#Funcionando    #consulta_registro(usuario)

    elif opcion == '19':
        modificar_registro(usuario)#Funcionando    

    elif opcion == '20':
       eliminar_registro(usuario)#Funcionando    
#--------------------------------------------------------------------


    elif opcion == '21':
        mostrar_listado_facturas(usuario)#Funcionando    #ok

    elif opcion == '22':
        ingresar_nueva_factura(usuario)#Funcionando    

    elif opcion == '23':
        consulta_factura(usuario)#Funcionando    

    elif opcion == '24':
        modificar_factura(usuario)#Funcionando    

    elif opcion == '25':
         eliminar_factura(usuario)#Funcionando        

    else:
        print("Opcion no valida")