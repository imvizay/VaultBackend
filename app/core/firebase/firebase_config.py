import firebase_admin
from firebase_admin import credentials
import os

print("INITIALIZING FIREBASE")

firebase_path = os.getenv(
    "FIREBASE_CREDENTIAL_PATH",
    "app/core/firebase/firebase_admin.json"
)

cred = credentials.Certificate(firebase_path)

firebase_admin.initialize_app(cred)

print("FIREBASE INITIALIZED")