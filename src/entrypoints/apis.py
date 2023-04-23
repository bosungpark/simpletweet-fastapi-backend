import uvicorn
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
    timelines1 = services.subscribe_timeline_using_rdbm(user_id=user_id)
    timelines2 = services.subscribe_timeline_using_redis(user_id=user_id)
    print(timelines1)
    print()
    print(timelines2)
    # assert timelines1 == timelines2
    return {"message": "OK", "status_code": status.HTTP_200_OK, "timelines": timelines1}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
