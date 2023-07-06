import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('.env')

# Initialize Firebase Admin SDK with credentials from environment variables
cred = credentials.Certificate({
    "type": os.getenv("FIREBASE_TYPE"),
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY"),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
    "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL"),
    "universe_domain": "googleapis.com"
})
firebase_admin.initialize_app(cred)

# Initialize Firestore database
db = firestore.client()

app = FastAPI()

# Data class for Person
class Person(BaseModel):
    name: str
    age: int
    profession: str

# Create a document
@app.post("/persons/{document_id}")
def create_person(document_id: str, person: Person):
    data = person.dict()
    doc_ref = db.collection("persons").document(document_id)
    doc_ref.set(data)
    return {"message": "Person created"}

# Read a document
@app.get("/persons/{document_id}")
def read_person(document_id: str):
    doc_ref = db.collection("persons").document(document_id)
    doc = doc_ref.get()
    if doc.exists:
        return {"data": doc.to_dict()}
    else:
        return {"message": "Person not found"}

# Update a document
@app.put("/persons/{document_id}")
def update_person(document_id: str, person: Person):
    data = person.dict(exclude_unset=True)
    doc_ref = db.collection("persons").document(document_id)
    doc_ref.update(data)
    return {"message": "Person updated"}

# Delete a document
@app.delete("/persons/{document_id}")
def delete_person(document_id: str):
    doc_ref = db.collection("persons").document(document_id)
    doc_ref.delete()
    return {"message": "Person deleted"}
