from fastapi import FastAPI
from ctypes import CDLL, c_int
from pydantic import BaseModel

lib = CDLL('libcalc.so')

app = FastAPI()


class Operation(BaseModel):
    type: str
    a: int
    b: int


def perform_operation(operation_type: str, a: int, b: int):
    if operation_type == "add":
        return lib.add(c_int(a), c_int(b))
    elif operation_type == "sub":
        return lib.sub(c_int(a), c_int(b))
    elif operation_type == "mul":
        return lib.mul(c_int(a), c_int(b))


@app.post("/calc")
async def calc(operation: Operation):
    result = perform_operation(operation.type, operation.a, operation.b)
    return {"result": result}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
