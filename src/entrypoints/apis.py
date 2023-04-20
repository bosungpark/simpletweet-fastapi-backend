from fastapi import FastAPI
from fastapi.params import Body
from starlette import status

app = FastAPI()


@app.post("/timeline", status_code=status.HTTP_201_CREATED)
async def publish_timeline(data=Body()) -> dict:

    return {"message": "OK","status_code":status.HTTP_201_CREATED}


@app.get("/timeline", status_code=status.HTTP_201_CREATED)
async def subscribe_timeline() -> dict:
    return {"message": "OK", "status_code": status.HTTP_200_OK}
