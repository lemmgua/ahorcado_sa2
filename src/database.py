import firebase_admin, os
from firebase_admin import credentials
from firebase_admin import db

GOOGLE_APPLICATION_CREDENTIALS = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]

cred = credentials.Certificate(GOOGLE_APPLICATION_CREDENTIALS)
app = firebase_admin.initialize_app(cred)

ref = db.reference("/registros-jugadores")
print(ref.get())
