import os
import cv2 as cv

def iniciar_camara():
    cap = cv.VideoCapture(0)
    return cap

def leer_frame(cap):
    ret, frame = cap.read()
    return ret, frame

def mostrar_frame(frame):
    cv.imshow("Ventana", frame)

def guardar_foto(frame, nombre, contador):
    ruta = f"face-db/{nombre}/foto{contador}.jpg"
    cv.imwrite(ruta, frame)
    print("Foto guardada")

def liberar_camara(cap):
    cap.release()
    cv.destroyAllWindows()

def cargar_imagen():
    print("Puedes arrastar la fotografía de la persona a esta ventana o escribir la ruta completa: ")
    print("Ejemplo: C:/Users/PC/Downloads/foto.jpg")
    ruta = input("Ruta: ").strip().strip('"')

    frame =cv.imread(ruta)
    if frame is None:
        print("No se encontró la imagen, verifica la ruta.")
        return None
    return frame