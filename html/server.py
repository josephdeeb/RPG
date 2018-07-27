import asyncio
import json
import websockets
import time

USERS = set()
BEINGS = dict()
ENTITIES = dict()
NEW_BULLETS = dict()
BULLETS = dict()

class Bullet:
    def __init__(self, x, y, velocityX, velocityY, size):
        self.x = x
        self.y = y
        self.velocityX = velocityX
        self.velocityY = velocityY
        self.size = size

    def updatePosition(self):


# Sending packets, we need:
#   Sequence number of packet we are responding to for each client
#   Newly created entities
#   For each being that has changed:
#       If the being has changed in view of the client, then send necessary movements for client to interpolate
#       Otherwise, ignore that being and don't send any data regarding it

def inputProcessing():


def getStateJSON():
    return json.dumps({'beings': BEINGS, 'new_bullets': NEW_BULLETS})

async def register(websocket):
    USERS.add(websocket)

async def inputHandler(websocket, path):
    await register(websocket)
    try:
        await websocket.send(getStateJSON())
        async for message in websocket:
            await inputProcessing(message)
