import insert_values_DB

def procesar_codigo(codigo):
    match codigo:
        case _ if codigo[0:2]=="00":
            try:
                return insert_values_DB.biblioteca_code(codigo)
            except Exception as error:
                return f"Se ha encontrado el siguiente error: {error}"
        case _ if codigo[0] in ("1","2"):
            try:
                return insert_values_DB.carnet_code(codigo)
            except Exception as error:
                return f"Se ha encontrado el siguiente error: {error}"    
        case _ if codigo[0] in ("0","6","7"):
            try:
                return insert_values_DB.dni_code(codigo)
            except Exception as error:
                return f"Se ha encontrado el siguiente error: {error}"
        case _:
            return "Error, codigo no reconocido"


        




