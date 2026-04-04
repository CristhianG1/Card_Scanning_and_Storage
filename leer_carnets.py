import msvcrt
import time

def leer_codigo(timeout=0.4):
    codigo = ""
    ultima_tecla = None

    while True:
        if msvcrt.kbhit():
            tecla = msvcrt.getwch()
            if tecla == "\x1b":
                return "exit"
            if tecla in ("\r", "\n"):
                if codigo:
                    return codigo
            elif tecla == "\b":
                codigo = codigo[:-1]
            else:
                codigo += tecla
                print(tecla, end="", flush=True)
            ultima_tecla = time.time()
        else:
            if codigo and ultima_tecla and time.time() - ultima_tecla >= timeout:
                return codigo
            time.sleep(0.01)