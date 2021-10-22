from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from pydantic import BaseSettings
import json, htmpPage

app = FastAPI(title='Web page send JSON') #create app


@app.get("/")
async def root():
    return HTMLResponse(htmpPage.html)

counter = 0
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    global counter
    while True:
        try:
            counter += 1
            print(counter)
            data = await websocket.receive_text()
            print(data)
            test = json.loads(data)
            print(test)
            await websocket.send_json(f"{counter} {data} ")
        except Exception as e:
            print('error:', e)
            break
