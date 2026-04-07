from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import main
from insert_values_DB import cursor

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/escanear")
async def escanear(datos: dict):
    codigo = datos["codigo"]
    respuesta = main.procesar_codigo(codigo)
    return {"mensaje": respuesta}

@app.get("/logs")
async def obtener_logs():
    # Filtra donde la fecha de hora_entrada sea igual a hoy
    cursor.execute("""
        SELECT codigo_ingreso, nombre, apellido, carrera, 
               hora_entrada, hora_salida, estado, conexion
        FROM logs_students
        WHERE DATE(hora_entrada) = DATE('now', 'localtime')
        ORDER BY hora_entrada DESC
    """)
    resultados = cursor.fetchall()
    return {"logs": resultados}
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
