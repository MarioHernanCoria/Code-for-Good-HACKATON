import mysql.connector
from mysql.connector import Error

from fastapi import FastAPI
app = FastAPI()

@app.post("/test")
def loguear(name: str='world',password: str ='contraseña'):
  return {f'testeando {name}, {password}'} 

conn = None
cursor = None

def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='python_mysql',
                                       user='root',
                                       password='SecurePass1!')
        if conn.is_connected():
            print('Connected to MySQL database')
            cursor = conn.cursor()
            return conn, cursor
    except Error as e:
        print(e)

def log_user(user,password,tipo):
    '''LOG IN EN LA PAGINA'''
    try:
        if tipo == 'usuario':
            conn ,cursor= connect()
            data = cursor.fetchall(f'''
            SELECT * FROM USUARIO 
            WHERE Usuario = {user} AND Contrasena = {password}
            ''')
            close_conn()
            return data
        if tipo == 'organizacion':
            conn ,cursor= connect()
            data = cursor.fetchall(f'''
            SELECT * FROM ORGANIZACION 
            WHERE RazonSocial = {user} AND Contrasena = {password}
            ''')
            close_conn()
            return data
    except:
        close_conn()
        return 'FAIL'

def registrar_usuario(nombre,apellido,pais,pronombres,mail,contraseña,username,edad):
    '''CARGA EN LA BASE DE DATOS UN NUEVO USUARIO CON TODOS SUS DATOS'''
    try:
        conn ,cursor= connect()
        cursor.execute(f'''INSERT INTO USUARIO Values({nombre},{apellido},{pais},{pronombres},{mail},{contraseña},{username},{edad})
        IF (SELECT * FROM USUARIO WHERE Email = {mail} or {username} = Usuario) = NULL''')
        close_conn()
        return 'OK'
    except:
        close_conn()
        return 'FAIL'

def registrar_organizacion(nombre,pais,ciudad,mail,contraseña):
    '''CARGA EN LA BASE DE DATOS UNA NUEVA ORGANIZACION CON TODOS SUS DATOS'''
    try:
        conn ,cursor= connect()
        cursor.execute(f'''INSERT INTO ORGANIZACION Values({nombre},{pais},{ciudad},{mail},{contraseña})
        IF (SELECT * FROM ORGANIZACION WHERE Email = {mail} or {nombre} = RazonSocial) = NULL''')
        close_conn()
        return 'OK'
    except:
        close_conn()
        return 'FAIL'

def get_tickets(tipo='User',limit=50):
    '''TRAE DE LA BASE DE DATOS TODOS LAS CONSULTAS. POR DEFECTO TOMA LAS DE LOS USUARIOS NORMALES, PERO TAMBIEN PUEDE TRAER LAS DE LAS ORGANIZACIONES'''
    try:
        if tipo == 'User':
            conn ,cursor= connect()
            data = cursor.fetchall(f'''
                SELECT * FROM ConsultasUser ORDER BY Fecha DESC''')
        if tipo == 'org':
            conn ,cursor= connect()
            data = cursor.fetchall(f'''
                SELECT * FROM ConsultasOrg ORDER BY Fecha DESC''')
        close_conn()
        return data
    except:
        close_conn()
        return 'FAIL'


def set_tickets(AutorID, Contenido, Tipo, Respondido, Fecha):
    '''CARGA EN LA BASE DE DATOS UNA CONSULTA CON TODOS SUS DATOS'''
    try:
        conn ,cursor= connect()
        cursor.execute(f'''INSERT INTO ConsultasUser Values({AutorID},{Contenido},{Tipo},{Respondido},{Fecha})''')
        close_conn()
        return 'OK'
    except:
        close_conn()
        return 'FAIL'

def get_events(limit=50):
    '''TRAE DE LA BASE DE DATOS TODOS LOS EVENTOS QUE AUN NO HAYAN PASADO'''
    try:
        conn ,cursor= connect()
        data = cursor.fetchall(f'''
                SELECT * FROM EVENTOS WHERE Fecha > CURRENT_DATE ORDER BY Fecha DESC LIMIT {limit}''')
        close_conn()
        return data
    except:
        close_conn()
        return 'FAIL'

def get_orgsXpais(pais, limit=50):
    '''TRAE DE LA BASE DE DATOS TODAS LAS ORGANIZACIONES DE UN PAIS PASADO POR PARAMETRO'''
    try:
        conn ,cursor= connect()
        data = cursor.fetchall(f'''
                SELECT * FROM ORGANIZACION WHERE Pais = {pais} LIMIT {limit}''')
        close_conn()
        return data
    except:
        close_conn()
        return 'FAIL'

def set_evento(orgId, fecha, ubicacion, nombre, desc):
    '''CARGA UN EVENTO CON SUS DATOS EN LA BASE DE DATOS'''
    try:
        conn ,cursor= connect()
        cursor.execute(f'''INSERT INTO ConsultasUser Values({orgId},{fecha},{ubicacion},{nombre},{desc})''')
        close_conn()
        return 'OK'
    except:
        close_conn()
        return 'FAIL'

def close_conn():
    cursor.close()
    conn.close()

