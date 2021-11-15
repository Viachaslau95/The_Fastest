import shutil
from typing import List
from fastapi import APIRouter, UploadFile, File, Form
from schemas import UploadVideo, GetVideo

video_router = APIRouter()


@video_router.post("/")
async def root(title: str = Form(...), description: str = Form(...), file: UploadFile = File(...)):
    info = UploadVideo(title=title, description=description)
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_name": file.filename, "info": info}


@video_router.post("/img")
async def upload_img(files: List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}', "wb") as buffer:
            shutil.copyfileobj(img.file, buffer)

    return {"file_name": "It's oK"}


@video_router.post("/info")
async def info_set(info: UploadVideo):
    return info


@video_router.get("/video", response_model=GetVideo)
async def get_video():
    user = {'id': 12, 'name': 'Arni'}
    video = {'title': 'Test', 'description': 'Description'}
    return GetVideo(user=user, video=video)


