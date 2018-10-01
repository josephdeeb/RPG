import asyncio
import json
import websockets
import time
import threading

USERS = dict()
BEINGS = dict()
STEP = 0
NEXT_STEP = 0
STEP_SIZE = 0.016 # in seconds, 16 milliseconds
HEIGHT = 150
WIDTH = 150

"""
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
"""

"""
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocityX = 0
        self.accelerationX = 1
        self.maxVelocityX = 2
        self.velocityY = 0
        self.accelerationY = 1
        self.maxVelocityY = 2
        self.size = 5
        self.inputStep = 0

    def move(self, waitUntil):
        newX = self.x + self.velocityX
        newY = self.y + self.velocityY
        if newX > ((WIDTH - 1) - size):
            newX = (WIDTH - 1) - size
            self.velocityX = 0

        elif newX < 0:
            newX = 0
            self.velocityX = 0

        if newY > ((HEIGHT - 1) - size):
            newY = (HEIGHT - 1) - size
            self.velocityY = 0

        elif newY < 0:
            newY = 0
            self.velocityY = 0

        self.x = newX
        self.y = newY

        return delta

    def handleMessage(self, message):
        # message is a 4-tuple where each element is up, right, down, left, respectively
        # If holding up AND down, do nothing
        if not message[0]:
            if not message[1]:
                if not message[2]:
                    if not message[3]:
                        return

        if message[0] and message[2]:
            pass

        # Else if holding up AND NOT down, go upwards
        elif message[0] and (not message[2]):
            if self.velocityY >= self.maxVelocityY:
                self.velocityY = self.maxVelocityY

            else:
                if self.velocityY + self.accelerationY >= self.maxVelocityY:
                    self.velocityY = self.maxVelocityY

                else:
                    self.velocityY += self.accelerationY

        # Else if (NOT holding up) AND holding down, go down
        elif (not message[0]) and message[2]:
            if self.velocityY <= -self.maxVelocityY:
                self.velocityY = -self.maxVelocityY

            else:
                if self.velocityY - self.accelerationY <= -self.maxVelocityY:
                    self.velocityY = -self.maxVelocityY

                else:
                    self.velocityY -= self.accelerationY

        # If holding right AND left, do nothing
        if message[1] and message[3]:
            pass

        # Else if holding right AND NOT left, go right
        elif message[1] and (not message[3]):
            if self.velocityX >= self.maxVelocityX:
                self.velocityX = self.maxVelocityX

            else:
                if self.velocityX + self.accelerationX >= self.maxVelocityX:
                    self.velocityX = self.maxVelocityX

                else:
                    self.velocityX += self.accelerationX

        # Else if (NOT holding right) AND holding left, go left
        elif (not message[1]) and message[3]:
            if self.velocityX <= -self.maxVelocityX:
                self.velocityX = -self.maxVelocityX

            else:
                if self.velocityX - self.accelerationX <= -self.maxVelocityX:
                    self.velocityX = -self.maxVelocityX

                else:
                    self.velocityX -= self.accelerationX

"""

class MessageQueue:
    def __init__(self):
        self.queue = []

    def push(self, message):
        self.queue.append(message)

    def pop(self):
        return self.queue.pop(0)

    def get(self, index):
        return self.queue[index]

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.messages = MessageQueue()

    def receiveMessage(self, message):
        self.messages.push(message)

    def processMessage(self):
        msg = self.messages.pop()
        if msg ==

def getStateJSON():
    return json.dumps({'users': **USERS})

async def notifyState():
    if USERS:
        message = getStateJSON()
        await asyncio.wait([user.send(message) for user in USERS])

def register(websocket):
    USERS[websocket] = Player(0, 0)
    print('USER JOINED')

def unregister(websocket):
    USERS[websocket] = None
    print('USER LEFT')

async def mainLoop():
    now = time.time()
    await notifyState()
    await asyncio.sleep(time)


async def connection(websocket, path):
    register(websocket)
    try:
        # Whenever a message is received in the websocket...
        async for message in websocket:
            USERS[websocket].receiveMessage(message)

            """
            # If the message is received sooner than when the step is supposed to occur, then wait until STEP
            currentTime = time.time()
            if currentTime < STEP:
                await asyncio.sleep(STEP - currentTime)

            # Now it's time for the step to occur
            player = USERS[webosocket]
            # Handle the message
            player.handleMessage(message)

            # Move the player
            player.move()

            currentTime = time.time()
            delta = NEXT_STEP - currentTime
            # If there's time between now and NEXT_STEP, wait at least that long
            if delta > 0:
                await asyncio.sleep(time.time() - NEXT_STEP)

            # Send game data now that we're at NEXT_STEP, then wait for next message
            await websocket.send(getStateJSON())
"""

    finally:
        unregister(websocket)


class ServerThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        asyncio.get_event_loop().run_until_complete(websockets.serve(connection, 'localhost', 6789))
