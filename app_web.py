from flask import Flask, render_template
import sqlite3

# 1. Creamos la aplicación
app = Flask(__name__)

# 2. Creamos la ruta (la dirección que escribirás en el navegador)
@app.route('/')
def pagina_principal():
    # Conectamos a tu base de datos
    conn = sqlite3.connect('BD_sqlite/students.db')
    conn.row_factory = sqlite3.Row  # Esto permite leer las columnas por nombre
    
    # Le pedimos a SQL que nos dé todo lo de la tabla logs
    # El ORDER BY sirve para que el último que entró salga primero arriba
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs_students ORDER BY hora_entrada DESC")
    datos_tabla = cursor.fetchall()
    
    conn.close()
    
    # Enviamos los datos al HTML (registros es el nombre que usará el HTML)
    return render_template('index.html', registros=datos_tabla)

# 3. Encendemos el servidor
if __name__ == '__main__':
    app.run(debug=True)