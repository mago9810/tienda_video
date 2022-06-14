from variables_control import MENU,CLIENTE,EMPLEADO

from variables_control import db_usuarios

def validar_acceso_funcion(perfil, funcion):
    for menu in MENU:
        if funcion in menu['funcion']:
            if perfil in menu['perfiles']:
                return True
            else:
                return False

def validar_credenciales(username: str, clave: str) -> dict:
    """Valida las credenciales de un usuario

    Args:
        usuario (str): 
        clave (str): 

    Returns:
        dict:   Si existe retorna un diccionario con los datos del usuarios
                Si no existe retorna un diccionario vacio
    """

    usu = {}
    for usuario in db_usuarios:
        # get cambia el error por un non y permite que continue el programa
        u = usuario.get('usuario')
        p = usuario.get('contraseña')
        if username == usuario.get('usuario') and clave == usuario.get('contraseña'):
            # Forma 2 de llamar un item de un diccionario
            usu = {
                'id':           usuario['id'],
                'nombre':       usuario['nombre'],
                'correo':       usuario['correo'],
                'edad':         usuario['edad'],
                'direccion':    usuario['direccion'],
                'celular':      usuario['celular'],
                'estado':       usuario['estado'],
                'tipo_usuario': usuario['tipo_usuario']}
    return usu

