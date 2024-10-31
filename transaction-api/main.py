from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
async def getRoot():
    return Response(content="Hello from FastAPI", media_type="text/plain")
