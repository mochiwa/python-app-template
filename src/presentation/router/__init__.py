from fastapi import Depends

from infrastructure.Container import Container


def depends(key):
    return Depends(lambda: Container().get_service(key))


from .project_router import router as project_router