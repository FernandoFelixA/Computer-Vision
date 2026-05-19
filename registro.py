import os
import shutil

def comprobar_permisos(password):
    password_admin = "1234567890"
    if password == password_admin:
        return True
    
def registrar_persona(nombre):
    os.makedirs(f"face-db/{nombre}", exist_ok = True)
    print (f"Carpeta creada para {nombre.capitalize()}")