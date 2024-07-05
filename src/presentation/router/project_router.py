from fastapi import APIRouter
from presentation.router import depends

router = APIRouter(
    prefix="/project"
)


@router.post(path="/", status_code=200)
def create(payload: dict, service=depends(str)):
    return {
        "operation": "POST",
        "value": service(dict)
    }


@router.put(path="/", status_code=200)
def update(payload: dict):
    return {
        "operation": "PUT"
    }


@router.get(path="/{obj_id}", status_code=200)
def read(obj_id: str, service=depends(str)):
    return {
        "operation": "GET",
        "value": service(obj_id)
    }


@router.delete(path="/{obj_id}", status_code=200)
def delete(obj_id: str):
    return {
        "operation": "DELETE",
        "value": ""
    }


@router.get(path="/error/{code}", status_code=200)
def read(code: str):
    raise RuntimeError(f"A runtime error {code}!")
