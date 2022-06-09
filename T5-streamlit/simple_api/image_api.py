import io

from fastapi import FastAPI, File, UploadFile
import numpy as np
from PIL import Image
from starlette.responses import RedirectResponse


app = FastAPI()


def read_imagefile(file) -> Image.Image:
    image = Image.open(io.BytesIO(file))
    return image


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


@app.post("/image_brightness")
async def image_brightness(file: UploadFile = File(...)):
    image = read_imagefile(await file.read()).convert("L")
    x = np.array(image)
    return {"brightness": x.mean()}
