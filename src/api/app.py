from fastapi import FastAPI
from main import process_document

app = FastAPI(title="Intelligent Document Processing API")

@app.post("/process/")
def process(file_path: str):
    return process_document(file_path)