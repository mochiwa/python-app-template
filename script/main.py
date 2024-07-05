import uvicorn
from fastapi import FastAPI

from presentation.router import project_router
from bootstrap import init_container


def init_app():
    app = FastAPI()
    app.include_router(project_router)
    return app


if __name__ == '__main__':
    init_container()
    uvicorn.run(init_app, host="0.0.0.0", port=8000, reload=False)
