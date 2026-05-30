import firebase_admin
from firebase_admin import credentials

print("INITIALIZING FIREBASE")

cred = credentials.Certificate(
    'app/core/firebase/firebase_admin.json'
)

firebase_admin.initialize_app(cred)

print("FIREBASE INITIALIZED")