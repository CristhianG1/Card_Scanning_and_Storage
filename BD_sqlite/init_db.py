import sqlite3

def init_db():
    conn = sqlite3.connect("BD_sqlite/students.db")
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        codigo TEXT PRIMARY KEY,
        dni TEXT NOT NULL UNIQUE,
        codigoBib TEXT NOT NULL UNIQUE,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        carrera TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs_students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo_estudiante TEXT NOT NULL,
        codigo_ingreso TEXT NOT NULL,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        tipeIdentification TEXT NOT NULL,
        carrera TEXT NOT NULL,
        estado TEXT NOT NULL,
        pc_actual TEXT,
        conexion TEXT NOT NULL,
        hora_entrada TEXT NOT NULL,
        hora_salida TEXT,     
        FOREIGN KEY (codigo_estudiante) REFERENCES students(codigo)
    )
    """)

    conn.commit()
    conn.close()

    print("Base de datos y tablas listas.")



if __name__ == "__main__":
    init_db()