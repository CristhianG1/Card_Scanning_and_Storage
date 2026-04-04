from BD_sqlite import init_db
from datetime import datetime
import sqlite3
import time

conn = sqlite3.connect("BD_sqlite/students.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

#INSERTAR LOGS CON CARNET UNIVERSITARIO
def carnet_code(codigo):
    cursor.execute("""
    SELECT * FROM students WHERE codigo = ? """, (codigo,)
    )
    resultado = cursor.fetchone()
    if resultado == None:
        print("No se ha encontrado el Carnet Universitario solicitado")
        return
    else:
        cursor.execute("SELECT * FROM logs_students WHERE codigo_estudiante = ? AND hora_salida IS NULL"
        ,(resultado[0],))
        
        busqueda = cursor.fetchone()
        if busqueda is None:
            cursor.execute("""
                INSERT INTO logs_students 
                (codigo_estudiante, tipeIdentification, nombre, apellido, carrera, hora_entrada)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (resultado[0], "Carnet universitario", resultado[3], resultado[4], resultado[5], datetime.now().isoformat())
            )
            conn.commit()
        else:
            cursor.execute("""
                UPDATE logs_students SET hora_salida = ? WHERE codigo_estudiante = ? AND hora_salida IS NULL""",
                (datetime.now().isoformat(), resultado[0])
            )
            conn.commit()
            print("Se ha registrado la salida")

#INSERTAR LOGS CON DNI
def dni_code(codigo):
    cursor.execute("""
    SELECT * FROM students WHERE dni = ? """, (codigo,)
    )
    resultado = cursor.fetchone()
    if resultado == None:
        print("No se ha encontrado el DNI solicitado")
        return
    else:
        cursor.execute("SELECT * FROM logs_students WHERE codigo_estudiante = ? AND hora_salida IS NULL"
        ,(resultado[0],))
        
        busqueda = cursor.fetchone()
        if busqueda is None:
            cursor.execute("""
                INSERT INTO logs_students 
                (codigo_estudiante, tipeIdentification, nombre, apellido, carrera, hora_entrada)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (resultado[0], "DNI", resultado[3], resultado[4], resultado[5], datetime.now().isoformat())
            )
            conn.commit()
        else:
            cursor.execute("""
                UPDATE logs_students SET hora_salida = ? WHERE codigo_estudiante = ? AND hora_salida IS NULL""",
                (datetime.now().isoformat(), resultado[0])
            )
            conn.commit()
            print("Se ha registrado la salida")

#INSERTAR LOGS CON CARNET BIBLIOTECA
def biblioteca_code(codigo):
    cursor.execute("""
    SELECT * FROM students WHERE codigoBib = ? """, (codigo,)
    )
    resultado = cursor.fetchone()
    if resultado == None:
        print("No se ha encontrado el Codigo de Biblioteca solicitado")
        return
    else:
        cursor.execute("SELECT * FROM logs_students WHERE codigo_estudiante = ? AND hora_salida IS NULL"
        ,(resultado[0],))
        
        busqueda = cursor.fetchone()
        if busqueda is None:
            cursor.execute("""
                INSERT INTO logs_students 
                (codigo_estudiante, tipeIdentification, nombre, apellido, carrera, hora_entrada)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (resultado[0], "Carnet Biblioteca", resultado[3], resultado[4], resultado[5], datetime.now().isoformat())
            )
            conn.commit()
        else:
            cursor.execute("""
                UPDATE logs_students SET hora_salida = ? WHERE codigo_estudiante = ? AND hora_salida IS NULL""",
                (datetime.now().isoformat(), resultado[0])
            )
            conn.commit()
            print("Se ha registrado la salida")


        