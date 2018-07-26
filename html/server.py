import asyncio
import json
import websockets
import time

USERS = set()
BEINGS = dict()
ENTITIES = dict()

def getStateJSON():
    return json.dumps({'type': 'beings', **BEINGS}, {'type': 'entities', **ENTITIES})

async def inputHandler(websocket, path):
    await register(websocket)
    try:
        #Send
        await websocket.send(getStateJSON())
        async for message in websocket:
            await inputProcessing(message)
