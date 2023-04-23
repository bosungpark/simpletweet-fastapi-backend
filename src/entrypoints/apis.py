import uvicorn as uvicorn
from fastapi import FastAPI
from starlette import status

from src.service_layer import services

app = FastAPI()


@app.post("/timeline", status_code=status.HTTP_201_CREATED)
def publish_timeline(user_id) -> dict:
    services.publish_timeline(user_id=user_id)
    return {"message": "OK","status_code":status.HTTP_201_CREATED}


@app.get("/timeline", status_code=status.HTTP_201_CREATED)
def subscribe_timeline(user_id) -> dict:
    timelines = services.subscribe_timeline(user_id=user_id)
    return {"message": "OK", "status_code": status.HTTP_200_OK, "timelines": timelines}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
