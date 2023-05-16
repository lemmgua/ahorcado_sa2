import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

def InsertarPuntuacion(nombre: str, puntos: int, mayorRacha: int) -> any:
    cred = credentials.Certificate(r"C:\Users\aleja\OneDrive\Documentos\.Code\hanged-man-sa2-firebase-adminsdk-b0ie6-95cbc7f745.json")
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    data = {
        u"mayor-racha": mayorRacha,
        u"nombre": nombre,
        u"score": puntos
    }

    return db.collection(u"registros-jugadores").add(data)

def LeerDatos(nombre: str) -> list[dict]:
    cred = credentials.Certificate(r"C:\Users\aleja\OneDrive\Documentos\.Code\hanged-man-sa2-firebase-adminsdk-b0ie6-95cbc7f745.json")
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    doc = db.collection(u"registros-jugadores").where(u"nombre", u"==", nombre)

    return [x.to_dict() for x in doc.stream()]

if __name__ == "__main__":
    print(LeerDatos("leon"))