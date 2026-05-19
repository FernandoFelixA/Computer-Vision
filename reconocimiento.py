from deepface import DeepFace
import os

def identificar_persona(frame):
    try:
        resultado = DeepFace.find(img_path=frame, db_path="face-db/")
        if len(resultado[0]) > 0:
            ruta = resultado[0]["identity"][0]
            nombre = os.path.basename(os.path.dirname(ruta))
            return nombre
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
