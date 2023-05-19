from src.bootstrap.main import bootstrap
from fastapi.testclient import TestClient

app = bootstrap()
test_client = TestClient(app)
