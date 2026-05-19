import os
import json
import shutil

def cargar_perfiles():
    if os.path.exists("face-db/perfiles.json"):
        with open("face-db/perfiles.json", "r") as archivo:
            return json.load(archivo)
    else:
        return {
    "fernando": {"musica": "rock", "iluminacion": "cálida", "temperatura": 25, "televisor": "apagado", "genero": "Man"},
    "emilia": {"musica": "Imagine Dragons", "iluminacion": "brillante", "temperatura": 21, "televisor": "encendido", "genero" : "Woman"}
            }

perfiles = cargar_perfiles()

def activar_modo(nombre):
    if nombre in perfiles:
        if perfiles[nombre]["genero"] == "Man":
            print(f"\n¡Bienvenido a casa {nombre.capitalize()}!, iniciando reproducción de música de {perfiles[nombre]["musica"]}, ajustando la iluminación a {perfiles[nombre]["iluminacion"]} y la temperatura a {perfiles[nombre]["temperatura"]}°C. Televisor {perfiles[nombre]["televisor"]}.")
        else:
            print(f"\n¡Bienvenida a casa {nombre.capitalize()}!, iniciando reproducción de música de {perfiles[nombre]["musica"]}, ajustando la iluminación a {perfiles[nombre]["iluminacion"]} y la temperatura a {perfiles[nombre]["temperatura"]}°C. Televisor {perfiles[nombre]["televisor"]}.")


def agregar_perfil(nombre, musica, iluminacion, temperatura, televisor, genero, edad):
    perfiles[nombre] = {
        "musica" : musica,
        "iluminacion" : iluminacion,
        "temperatura" : temperatura,
        "televisor" : televisor,
        "genero" : genero,
        "edad" : edad
    }
    with open("face-db/perfiles.json", "w", encoding="utf-8") as archivo:
        json.dump(perfiles, archivo, indent=2, ensure_ascii=False)
        print(f"Perfil de {nombre.capitalize()} creado exitosamente.")

def eliminar_perfil(nombre):
    if nombre in perfiles:
        shutil.rmtree(f"face-db/{nombre}")
        del perfiles[nombre]
        with open("face-db/perfiles.json", "w", encoding="utf-8") as archivo:
            json.dump(perfiles, archivo, indent=2, ensure_ascii=False)
        print(f"Perfil de {nombre.capitalize()} eliminado.")
        for archivo in os.listdir("face-db"):
            if archivo.endswith(".pkl"):
                os.remove(f"face-db/{archivo}")
    else:
        print("El miembro no existe.")