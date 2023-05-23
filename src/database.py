import firebase_admin, os
from firebase_admin import firestore
from firebase_admin import credentials
from dotenv import load_dotenv

def InsertarPuntuacion(nombre: str, puntos: int, mayorRacha: int) -> None:
    cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS_SA2"))
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    data = {
        u"mayor-racha": mayorRacha,
        u"nombre": nombre,
        u"score": puntos
    }

    db.collection(u"registros-jugadores").add(data)

    firebase_admin.delete_app(firebase_admin.get_app())

def LeerDatos(nombre: str) -> list[dict]:
    load_dotenv()
    cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS_SA2"))
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    doc = db.collection(u"registros-jugadores").where(u"nombre", u"==", nombre)

    firebase_admin.delete_app(firebase_admin.get_app())

    return [x.to_dict() for x in doc.stream()]

if __name__ == "__main__":
    print(LeerDatos("leon"))