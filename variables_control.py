

EMPLEADO = 'empleado'
CLIENTE = 'cliente'

MENU = [
    # {
    #     # Le agregue un nuemro a cada opcion para que nos sirva como informacion al usuario
    #     'opcion': '1.   Consultas',
    #     # de que numero debe tecler para ejecutar la operacion deseada
    #     'funcion': 'consultar_peliculas',
    #     'perfiles':  [EMPLEADO, CLIENTE]
    # },
    # {
    #     # 'opcion': '2.   Alquilar'  Teniamos un error en el nombre de la funcion tanto en opcion
    #     'opcion': '2.  alquilar_peliculas',
    #     # como en funcion, por eso denegaba el acceso a la funcion dos
    #     'funcion': 'alquilar_peliculas',
    #     'perfiles':  [EMPLEADO]
    # },
    # {
    #     'opcion': '3.   Registrar Clientes',
    #     'funcion': 'registrar_clientes',
    #     'perfiles':  [EMPLEADO]
    # },
    # {
    #     'opcion': '4.   Registrar Peliculas',
    #     'funcion': 'registrar_peliculas',
    #     'perfiles':  [EMPLEADO]
    # },
# ----------------------------------------------
    {
        'opcion': '5.   Mostrar_listado_peliculas', #funcionando
        'funcion': 'Mostrar_listado_peliculas',
        'perfiles':  [EMPLEADO, CLIENTE]
    },
        {
        'opcion': '6.   Ingresar_nueva_pelicula',  #funcionando
        'funcion': 'Ingresar_nueva_pelicula',
        'perfiles':  [EMPLEADO]
    },
    
    {
        'opcion': '8.   Consulta_pelicula',
        'funcion': 'Consulta_pelicula',
        'perfiles':  [EMPLEADO, CLIENTE]
    },
    {
        'opcion': '9.  modificar_pelicula',
        'funcion': 'modificar_pelicula',
        'perfiles':  [EMPLEADO]
    },
        {
        'opcion': '10.  eliminar_pelicula',
        'funcion': 'eliminar_pelicula',
        'perfiles':  [EMPLEADO]
    },
# ----------------------------------------------   
    {
        'opcion': '11.  Mostrar_listado_clientes',
        'funcion': 'mostrar_listado_clientes',
        'perfiles':  [EMPLEADO]
    },
    {
        'opcion': '12.  Ingresar_nuevo_cliente',
        'funcion': 'ingresar_nuevo_cliente',
        'perfiles':  [EMPLEADO]
    },
    {
        'opcion': '13.  Consulta_cliente',
        'funcion': 'consulta_cliente',
        'perfiles':  [EMPLEADO]
    },
        {
        'opcion': '14.  Modificar_cliente',
        'funcion': 'modificar_cliente',
        'perfiles':  [EMPLEADO]
    },
    {
        'opcion': '15.  Eliminar_cliente',
        'funcion': 'eliminar_cliente',
        'perfiles':  [EMPLEADO]
    },
# ----------------------------------------------
    {
        'opcion': '16.  mostrar_listado_registros',
        'funcion': 'mostrar_listado_registros',
        'perfiles':  [EMPLEADO]
    },
    {
        'opcion': '17.  Alquilar pelicula',
        'funcion': 'ingresar_nuevo_regitro',
        'perfiles':  [EMPLEADO]
    },
            {
        'opcion': '18.  Consulta_registro',
        'funcion': 'consulta_registro',
        'perfiles':  [EMPLEADO]
    },
        {
        'opcion': '19.  Modificar_registro',
        'funcion': 'modificar_registro',
        'perfiles':  [EMPLEADO]
    },
            {
        'opcion': '20.  Eliminar_registro',
        'funcion': 'eliminar_registro',
        'perfiles':  [EMPLEADO]
    },
# ----------------------------------------------
    {
        'opcion': '21.  Mostrar_listado_facturas',
        'funcion': 'mostrar_listado_facturas',
        'perfiles':  [EMPLEADO]
    },
    {
        'opcion': '22.   ingresar_nueva_factura',
        'funcion': 'ingresar_nuevo_regitro',
        'perfiles':  [EMPLEADO]
    },
            {
        'opcion': '23.  consulta_factura',
        'funcion': 'consulta_factura',
        'perfiles':  [EMPLEADO]
    },
        {
        'opcion': '24.  modificar_factura',
        'funcion': 'modificar_registro',
        'perfiles':  [EMPLEADO]
    },
            {
        'opcion': '25.  eliminar_factura',
        'funcion': 'eliminar_factura',
        'perfiles':  [EMPLEADO]
    },
# ----------------------------------------------
]

db_peliculas = [     # Crea una lista de directorios
        {               # Crea un directorio
            'id': '122578',
            'titulo': "Lo que el viento se llevo",
            'director': "Victor Fleming",
            'año': 1939,
            'actores':  ["Vivien Leigh", " Clark Gable"],
            'genero': ["Clasico", "Romance"],
            'descripcion': "es una pelicula de romance enmarcada en la guerra de sececion de estados unidos",
            'estado': 'activo',
            'disponible': True,
            'cantidad': 6
        },
        {
            'id': '134517',
            'titulo': "Harry Potter 1",
            'director': "Steven Spielberg",
            'año': 2001,
            'actores':  ["Rupert Grint ", " Emma Watson", 'Daniel Radcliffe'],
            'genero': ["Clasico", "avenmtura", "fantasia"],
            'descripcion': "Es una pelicula infantil enmarcada en la magia y los amigos",
            'estado': 'activo',
            'disponible': True,
            'cantidad': 5
        },

        {
            'id': '458792',
            'titulo': "Rapidos y furiosos 45",
            'director': "Rob Cohen",
            'año': 2001,
            'actores':  ["Paul Walker ", "Vin Diesel", 'Michelle Rodríguez'],
            'genero': ["Accion"],
            'descripcion': "Es una pelicula de accion con muchos carros, explociones e imagenes subrealistas",
            'estado': 'activo',
            'disponible': True,
            'cantidad': 5
        }
    ]

db_usuarios = [     # Crea una lista de directorios
        {               # Crea un directorio
            'usuario': 'diego',
            'contraseña': 'diego123',
            'id': 79885920,
            'nombre': "Diego Gonzalez",
            'correo': "mago9810@gmail.com",
            'edad': 39,
            'direccion':  'calle 42 12-21',
            'estado_civil': 'casado',
            'celular': ['3112211564', '3103249472'],
            'estado': 'activo',
            'tipo_usuario': 'empleado'
        },
        {
            'usuario': 'paola',
            'contraseña': 'paola123',
            'id': 52435769,
            'nombre': "Paola Bermudez",
            'correo': "paber9810@gmail.com",
            'edad': 35,
            'direccion':  'calle 42 12-21',
            'estado_civil': 'casado',
            'celular': ['3225896335', '310589651'],
            'estado': 'activo',
            'tipo_usuario': 'cliente'
        },
        {
            'usuario': 'jero',
            'contraseña': 'jero123',
            'id': 1013017227,
            'nombre': "Jeronimo Gonzalez",
            'correo': "jero9810@gmail.com",
            'edad': 15,
            'direccion':  'calle 42 12-21',
            'estado_civil': 'soltero',
            'celular': ['3152558978', '3215879875'],
            'estado': 'activo',
            'tipo_usuario': 'cliente'
        },
        {
            'usuario': 'cristo',
            'contraseña': 'cristo123',
            'id': 1019913420,
            'nombre': "Cristobal Gonzalez",
            'correo': "cristo9810@gmail.com",
            'edad': 18,
            'direccion':  'calle 42 12-21',
            'estado_civil': 'soltero',
            'celular': ['3037895254', '3412698271'],
            'estado': 'activo',
            'tipo_usuario': 'cliente'
        },
        {
            'usuario': 'ines',
            'contraseña': 'ines123',
            'id': 41781206,
            'nombre': "Ines Diaz",
            'correo': "ines9810@gmail.com",
            'edad': 70,
            'direccion':  'calle 42 12-21',
            'estado_civil': 'casado',
            'celular': ['3012589874', '3658959858'],
            'estado': 'activo',
            'tipo_usuario': 'cliente'
        },
                {
            'usuario': 'gilberto',
            'contraseña': 'gilberto123',
            'id': 69585698,
            'nombre': "Gilberto Gonzalez",
            'correo': "gilberto9810@gmail.com",
            'edad': 70,
            'direccion':  'calle 42 12-21',
            'estado_civil': 'casado',
            'celular': ['3025589587', '3025878985'],
            'estado': 'activo',
            'tipo_usuario': 'cliente'
        }
    ]

lista_alquileres = [

    {
        'id registro': 1,
        'id pelicula': '122578',
        'titulo': "Lo que el viento se llevo",
        'cedula': 79885920,
        'nombre': "Diego Gonzalez",
        'costo del alquiler': 3000,
        'fecha_alquiler': "2022,5,1",
        'dias de alquiler': 3,
        'fecha de retorno' : '2022,5,4',
        'Dias de retrazo' : '',
        'Multa': '',
    },

    {
        'id registro': 2,
        'id pelicula': '122578',
        'titulo': "Lo que el viento se llevo",
        'cedula': 52435769,
        'nombre': "Paola Bermudez",
        'costo del alquiler': 3000,
        'fecha_alquiler': "2022,5,3",
        'dias de alquiler': 3,
        'fecha de retorno' : '2022,5,6',
        'Dias de retrazo' : '',
        'Multa': '',
    },
    {
        'id registro': 3,
        'id pelicula': '122578',
        'titulo': "Lo que el viento se llevo",
        'cedula': 1013017227,
        'nombre': "Jeronimo Gonzalez",
        'costo del alquiler': 3000,
        'fecha_alquiler': "2022,5,4",
        'dias de alquiler': 3,
        'fecha de retorno' : '2022,5,7',
        'Dias de retrazo' : '',
        'Multa': '',
       },
    {
        'id registro': 4,
        'id pelicula': '122578',
        'titulo': "Lo que el viento se llevo",
        'cedula':  41781206,
        'nombre': "Ines Diaz",
        'costo del alquiler': 3000,
        'fecha_alquiler': "2022,5,6",
        'dias de alquiler': 3,
        'fecha de retorno' : '2022,5,9',
        'Dias de retrazo' : '',
        'Multa': '',
        },
    {
        'id registro': 5,
        'id pelicula': '122578',
        'titulo': "Lo que el viento se llevo",
        'cedula': 69585698,
        'nombre': "Gilberto Gonzalez",
        'costo del alquiler': 3000,
        'fecha_alquiler': "2022,5,8",
        'dias de alquiler': 3,
        'fecha de retorno' : '2022,5,11',
        'Dias de retrazo' : '',
        'Multa': '',
        },

    ]

db_facturas = [     # Crea una lista de directorios
        {        
            'No fact': '1',
            'id_cleinte': '52435769',
            'id peliculas alquiladas': ["122578",'134517'],
            'cant. peliculas alquiladas': 2,
            'costo un itario': 3000,
            'costo total': 6000,
        },
            {
            'No fact': '2',
            'id_cleinte': '79885920',
            'id peliculas alquiladas': ['458792','134517'],
            'cant. peliculas alquiladas': 2,
            'costo un itario': 3000,
            'costo total': 6000,
            },
            {
            'No fact': '3',
            'id_cleinte': '1013017227',
            'id peliculas alquiladas': ['458792','134517'],
            'cant. peliculas alquiladas': 2,
            'costo un itario': 3000,
            'costo total': 6000
            }
        ]

