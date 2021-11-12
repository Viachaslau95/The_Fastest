import shutil
from fastapi import FastAPI, UploadFile, File
from typing import List
app = FastAPI()

@app.post("/movie")
async def root(file: UploadFile = File(...)):
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_name": file.filename}



@app.post("/img")
async def upload_img(files: List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}', "wb") as buffer:
            shutil.copyfileobj(img.file, buffer)

    return {"file_name": "It's oK"}
