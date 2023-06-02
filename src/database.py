from os import getenv
from firebase_admin import firestore, initialize_app, get_app, delete_app
from firebase_admin import credentials
from google.cloud.firestore_v1.base_query import FieldFilter
from dotenv import load_dotenv

def InsertarPuntuacion(nombre: str, puntos: int, mayorRacha: int) -> None:
    cred = credentials.Certificate(getenv("GOOGLE_APPLICATION_CREDENTIALS_SA2"))
    initialize_app(cred)
    db = firestore.client()

    data = {
        u"mayor-racha": mayorRacha,
        u"nombre": nombre,
        u"score": puntos
    }

    db.collection(u"registros-jugadores").add(data)

    delete_app(get_app())

def LeerDatos(nombre: str) -> list[dict]:
    load_dotenv()
    cred = credentials.Certificate(getenv("GOOGLE_APPLICATION_CREDENTIALS_SA2"))
    initialize_app(cred)
    db = firestore.client()

    doc = db.collection(u"registros-jugadores").where(filter=FieldFilter("nombre", "==", nombre))

    delete_app(get_app())

    return [x.to_dict() for x in doc.stream()]

def PuntuacionMasAlta() -> dict:
    load_dotenv()
    cred = credentials.Certificate(getenv("GOOGLE_APPLICATION_CREDENTIALS_SA2"))
    initialize_app(cred)
    db = firestore.client()

    doc = db.collection(u"registros-jugadores").order_by("score", direction=firestore.Query.DESCENDING).limit(1)
    
    data = doc.get()[0]

    delete_app(get_app())

    return {
        "nombre": data.get("nombre"),
        "score": data.get("score")
        }

if __name__ == "__main__":
    print(PuntuacionMasAlta())