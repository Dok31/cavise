from fastapi import FastAPI
from ctypes import CDLL, c_int
from pydantic import BaseModel


lib = CDLL('libcalc.so')

app = FastAPI()


class Numbers(BaseModel):
    a: int
    b: int


@app.post('/calc')
async def calsc(numbers: Numbers):
    result = lib.add(c_int(numbers.a), c_int(numbers.b))
    return {'result': result}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
