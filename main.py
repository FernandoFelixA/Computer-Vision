import os

from deepface import DeepFace
import cv2 as cv
from camara import iniciar_camara, leer_frame, mostrar_frame, liberar_camara, cargar_imagen, guardar_foto
from reconocimiento import identificar_persona
from hogar import  activar_modo,agregar_perfil, eliminar_perfil
from registro import *

while True:
    print("----- SISTEMA DE RECONOCIMIENTO FACIAL PARA HOGARES INTELIGENTES -----\n")
    print("¡Hola! Prepárate para iniciar el reconocimiento facial.")
    print("1. Activar cámara \n2. Cargar imagen \n3. Registrar nuevo miembro \n4. Eliminar un miembro existente \n5. Salir \n")

    while True:
        opcion = input("Seleccione una opción: ")
        if opcion in ["1", "2", "3", "4", "5"]:
            break
        print("Por favor, seleccione una opción válida.\n")

    if opcion == "1":
        cap = iniciar_camara()

        while True:
            ret, frame = leer_frame(cap)

            mostrar_frame(frame)

            tecla = cv.waitKey(1)

            if tecla == ord('f') or tecla == ord('F'):
                nombre = identificar_persona(frame)
                if nombre:
                    activar_modo(nombre)
                elif nombre == None:
                    print("Acceso denegado")

            if tecla == ord('q') or tecla == ord('Q'):
                liberar_camara(cap)
                break

    elif opcion == "2":
        foto = cargar_imagen()
        if foto is not None:
            nombre = identificar_persona(foto)
            if nombre:
                activar_modo(nombre)
            else:
                print("Acceso denegado.")

    elif opcion == "3":
        comprobacion = comprobar_permisos(input("Ingrese la contraseña del administrador: "))
        
        if comprobacion:
            nombre = input("Ingresa el nombre del nuevo miembro: ").lower()
            registrar_persona(nombre)

            cap = iniciar_camara()

            while True:
                ret, frame = leer_frame(cap)

                mostrar_frame(frame)

                tecla = cv.waitKey(1)

                if tecla == ord('f') or tecla == ord('F'):
                    contador = len(os.listdir(f"face-db/{nombre}")) + 1
                    guardar_foto(frame, nombre, contador)
                    contador += 1
                    datos_deepface = DeepFace.analyze(img_path = (f"face-db/{nombre}/foto1.jpg"), actions = ['gender', 'age'])
                    genero = datos_deepface[0]['dominant_gender']
                    edad = datos_deepface[0]['age']

                if tecla == ord('q') or tecla == ord('Q'):
                    liberar_camara(cap)
                    break
            
            if edad < 15:
                agregar_perfil(nombre, " modo-infantil", "colorida", "22", "encendido", genero, edad)
                print(f"¡Hola {nombre.capitalize()}, qué alegría verte! Activando el modo infantil.")
            else:
                configuracion = input(f"¡Hola {nombre.capitalize()}, ¿deseas configurar tu perfil? (s/n) ")
                if configuracion == "s":
                    musica = input("Dime cuál es tu género musical o artista favorito: ")
                    iluminacion = input("¿Cómo prefieres la iluminación? ")
                    temperatura = input("¿Qué temperatura (°C) te parece agradable? ")
                    televisor = input("¿Quieres tu televisor encendido o apagado al llegar? ")
                    agregar_perfil(nombre, musica, iluminacion, temperatura, televisor, genero, edad)

                else:
                    agregar_perfil(nombre, "N/A" , "N/A", "N/A", "N/A", genero, edad)
                    print("¡Entendido! Puedes realizar la configuración más adelante. ¡Te doy la bienvenida!")
        else:
            print("Contraseña incorrecta. Intenta nuevamente.")

    if opcion == "4":
        comprobacion = comprobar_permisos(input("Ingrese la contraseña del administrador: "))
        
        if comprobacion:
            nombre = input("Ingresa el nombre del miembro: ").lower()
            eliminar_perfil(nombre)
        else:
            print("Contraseña incorrecta. Intenta nuevamente.")

    elif opcion == "5":
        print("\nSaliendo del programa. ¡Vuelve cuando quieras!\n")
        break

    if opcion != "5":
        continuar = input("\n¿Deseas volver al menú principal? (s/n): \n").lower()
        if continuar != "s":
            print("\nSaliendo del programa. ¡Vuelve cuando quieras!\n")
            break