from fastapi import FastAPI, Depends
import pandas as pd
import pickle
from pydantic import BaseModel
from starlette.responses import RedirectResponse


app = FastAPI()
state = {}


@app.on_event("startup")
async def load_model():
    with open("model.pkl", "rb") as f:
        state["model"] = pickle.load(f)


class BostonData(BaseModel):
    CRIM: float
    ZN: float
    INDUS: float
    CHAS: float
    NOX: float
    RM: float
    AGE: float
    DIS: float
    RAD: float
    TAX: float
    PTRATIO: float
    B: float
    LSTAT: float


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


@app.post("/boston_prediction")
async def boston_prediction(boston_X: BostonData = Depends()):
    X = pd.DataFrame(
        {
            "CRIM": [boston_X.CRIM],
            "ZN": [boston_X.ZN],
            "INDUS": [boston_X.INDUS],
            "CHAS": [boston_X.CHAS],
            "NOX": [boston_X.NOX],
            "RM": [boston_X.RM],
            "AGE": [boston_X.AGE],
            "DIS": [boston_X.DIS],
            "RAD": [boston_X.RAD],
            "TAX": [boston_X.TAX],
            "PTRATIO": [boston_X.PTRATIO],
            "B": [boston_X.B],
            "LSTAT": [boston_X.LSTAT],
        }
    )

    pred = state["model"].predict(X)

    return {"price": pred[0]}
