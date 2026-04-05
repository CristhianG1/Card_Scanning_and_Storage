from BD_sqlite import init_db
from datetime import datetime
import sqlite3
import time

conn = sqlite3.connect("BD_sqlite/students.db", check_same_thread=False)
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

#INSERTAR LOGS CON CARNET UNIVERSITARIO
def carnet_code(codigo):
    cursor.execute("""
    SELECT * FROM students WHERE codigo = ? """, (codigo,)
    )
    resultado = cursor.fetchone()
    if resultado == None:
        return "No se ha encontrado el Carnet Universitario solicitado"
    else:
        cursor.execute("SELECT * FROM logs_students WHERE codigo_estudiante = ? AND hora_salida IS NULL"
        ,(resultado[0],))
        
        busqueda = cursor.fetchone()
        if busqueda is None:
            cursor.execute("""
                INSERT INTO logs_students 
                (codigo_estudiante, codigo_ingreso, tipeIdentification, nombre, apellido, carrera, hora_entrada, estado, conexion)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (resultado[0], resultado[0], "Carnet universitario", resultado[3], resultado[4], resultado[5], datetime.now().isoformat(), "Registrado", "Offline")
            )
            conn.commit()
            return "Entrada registrada"
        else:
            cursor.execute("""
                UPDATE logs_students SET hora_salida = ? WHERE codigo_estudiante = ? AND hora_salida IS NULL""",
                (datetime.now().isoformat(), resultado[0])
            )
            conn.commit()
            return "Se ha registrado la salida"

#INSERTAR LOGS CON DNI
def dni_code(codigo):
    cursor.execute("""
    SELECT * FROM students WHERE dni = ? """, (codigo,)
    )
    resultado = cursor.fetchone()
    if resultado == None:
        return "No se ha encontrado el DNI solicitado"
    else:
        cursor.execute("SELECT * FROM logs_students WHERE codigo_estudiante = ? AND hora_salida IS NULL"
        ,(resultado[0],))
        
        busqueda = cursor.fetchone()
        if busqueda is None:
            cursor.execute("""
                INSERT INTO logs_students 
                (codigo_estudiante, codigo_ingreso, tipeIdentification, nombre, apellido, carrera, hora_entrada, estado, conexion)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (resultado[0], resultado[1], "DNI", resultado[3], resultado[4], resultado[5], datetime.now().isoformat(), "Registrado", "Offline")
            )
            conn.commit()
            return "Entrada registrada"
        else:
            cursor.execute("""
                UPDATE logs_students SET hora_salida = ? WHERE codigo_estudiante = ? AND hora_salida IS NULL""",
                (datetime.now().isoformat(), resultado[0])
            )
            conn.commit()
            return "Se ha registrado la salida"

#INSERTAR LOGS CON CARNET BIBLIOTECA
def biblioteca_code(codigo):
    cursor.execute("""
    SELECT * FROM students WHERE codigoBib = ? """, (codigo,)
    )
    resultado = cursor.fetchone()
    if resultado == None:
        return "No se ha encontrado el Codigo de Biblioteca solicitado"
    else:
        cursor.execute("SELECT * FROM logs_students WHERE codigo_estudiante = ? AND hora_salida IS NULL"
        ,(resultado[0],))
        
        busqueda = cursor.fetchone()
        if busqueda is None:
            cursor.execute("""
                INSERT INTO logs_students 
                (codigo_estudiante, codigo_ingreso, tipeIdentification, nombre, apellido, carrera, hora_entrada, estado, conexion)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (resultado[0], resultado[2], "Carnet Biblioteca", resultado[3], resultado[4], resultado[5], datetime.now().isoformat(), "Registrado", "Offline")
            )
            conn.commit()
            return "Entrada registrada"
        else:
            cursor.execute("""
                UPDATE logs_students SET hora_salida = ? WHERE codigo_estudiante = ? AND hora_salida IS NULL""",
                (datetime.now().isoformat(), resultado[0])
            )
            conn.commit()
            return "Se ha registrado la salida"


        