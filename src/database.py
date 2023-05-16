import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate(r"C:\Users\aleja\OneDrive\Documentos\.Code\hanged-man-sa2-firebase-adminsdk-b0ie6-95cbc7f745.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

def InsertarPuntuacion(nombre: str, puntos: int, mayorRacha: int) -> None:
    data = {
        u"mayor-racha": mayorRacha,
        u"nombre": nombre,
        u"score": puntos
    }
    doc_ref = db.collection(u"registros-jugadores").add(data)

if __name__ == "__main__":
    InsertarPuntuacion("leon", 5, 5)