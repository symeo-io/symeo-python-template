import uvicorn
from fastapi import FastAPI

from src.bootstrap.router import api_router


# Run with uvicorn & gunicorn
# uvicorn src.main:bootstrap
def bootstrap() -> FastAPI:
    app = FastAPI(title="Your API")
    app.include_router(api_router, prefix="/api/v1")
    return app


# Run with Poetry
def main():
    app = bootstrap()
    uvicorn.run(app=app, port=9999)


# Run with IDE
if __name__ == "__main__":
    main()
