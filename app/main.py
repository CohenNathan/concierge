from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.mount("/libs", StaticFiles(directory="web/libs"), name="libs")
app.mount("/static", StaticFiles(directory="web/static"), name="static")

@app.get("/")
def index():
    return FileResponse("web/index.html")

@app.get("/avatar.glb")
def get_avatar():
    return FileResponse("web/avatar.glb")
