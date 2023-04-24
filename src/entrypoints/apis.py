import datetime
import logging

import uvicorn
from fastapi import FastAPI
from starlette import status

from src.service_layer import services

app = FastAPI()

logger = logging.getLogger(__name__)


@app.post("/timeline", status_code=status.HTTP_201_CREATED)
def publish_timeline(user_id) -> dict:
    services.publish_timeline(user_id=user_id)
    return {"message": "OK","status_code":status.HTTP_201_CREATED}


@app.get("/timeline", status_code=status.HTTP_200_OK)
def subscribe_timeline(user_id) -> dict:
    time1 = datetime.datetime.now()
    services.subscribe_timeline_using_rdbm(user_id=user_id)
    time2 = datetime.datetime.now()
    services.subscribe_timeline_using_redis(user_id=user_id)
    time3 = datetime.datetime.now()

    logging.error(f"RDBM:{time2 - time1}!")
    logging.error(f"REDIS:{time3 - time2}!")
    return {"message": "OK", "status_code": status.HTTP_200_OK}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
