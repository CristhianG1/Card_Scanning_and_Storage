from BD_sqlite import init_db
from datetime import datetime
import sqlite3
import insert_values_DB
import leer_carnets

conn = sqlite3.connect("BD_sqlite/students.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

print("Escanea el código o escribe 'exit' para salir.")

while True:
    print("Ingresa el codigo a buscar: ", end="", flush=True)
    busqueda = leer_carnets.leer_codigo()
    print()
    if busqueda.lower() == "exit":
        break

    match busqueda:
        case _ if busqueda[0:2]=="00":
            print("Tipo de identificación: Carnet de biblioteca")
            insert_values_DB.biblioteca_code(busqueda)
        case _ if busqueda[0] in ("1","2"):
            print("Tipo de identificación: Carnet universitario")
            try:
                insert_values_DB.carnet_code(busqueda)
            except Exception as error:
                print(error)    
        case _ if busqueda[0] in ("0","6","7"):
            try:
                print("Tipo de identificación: 72032340")
                insert_values_DB.dni_code(busqueda)
            except Exception as error:
                print(error)
        case _:
            print("Error, codigo no reconocido")
conn.close()

        


    


