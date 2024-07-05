from fastapi import FastAPI
from starlette.testclient import TestClient

from bootstrap import init_container
from infrastructure.Container import Container
from script.main import init_app


class AbstractIntegrationTest:
    container: Container
    app: FastAPI
    client: TestClient

    @classmethod
    def setup_class(cls):
        cls.container = init_container()
        cls.app = init_app()
        cls.client = TestClient(cls.app)