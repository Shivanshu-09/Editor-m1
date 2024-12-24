from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Repil(BaseModel):
    lang: str
    repil_name: str


@app.post('/repil')
def read_root(repil: Repil):
    # create a folder with repil name
    # push default lang code to the repil folder
    

    return {"Hello": "world"}

