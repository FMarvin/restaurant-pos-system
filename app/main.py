from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from .database import engine, Base
from .routers import orders, tables
from .websocket_manager import manager

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Restaurant POS")
app.include_router(orders.router)
app.include_router(tables.router)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)

app.mount("/", StaticFiles(directory="app/static", html=True), name="static")
