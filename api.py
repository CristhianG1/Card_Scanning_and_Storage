from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import main

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
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
