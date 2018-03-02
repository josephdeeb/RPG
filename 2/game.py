import grid
import sqlite3 as sql

things = 0

def makeID():
    things += 1
    return things

class databaseWrapper:

    def __init__(self, fileName):
        self.fileName = fileName
        self.connected = False
        self.db = None
        self.cur = None

    def openDB(self):
        try:
            self.db = sql.connect(fileName)
            self.cur = db.cursor()
            self.connected = True
        except lite.Error, e:
            self.connected = False

    def closeDB(self):
        if self.db:
            self.db.close()

    def createTable(self, name, fields):
        if self.connected:
            # MAY NEED TO USE WITH STATEMENT
            # ALSO MAY NEED TO INITIALIZE CURSOR (Dunno how it works yet)




class Account:
    def __init__(self, userName, characters = None):
        self.userName = userName
        self.character = character

    def setCharacter(self, thing):
        self.character = thing

class IOWrapper:
    def __init__(self):
        pass

    def input(self):
        return "input() NOT DEFINED FOR IOWrapper"

    def output(self):
        return "output() NOT DEFINED FOR IOWrapper

class terminalInput(IOWrapper):
    def __init__(self):
        pass

    def input(self):
        return input()

    def output(self, string):
        print(string)

preconstructed = {
    "floor": Thing("floor", " ", pathable=True),
    "wall": Thing("wall", "#", pathable=False)
}

map = Map("fuck", 10, 10)
print(map)

map.fillArea(0, 9, 0, 9, preconstructed["floor"])
map.fillArea(0, 9, 0, 0, preconstructed["wall"])
map.fillArea(0, 9, 9, 9, preconstructed["wall"])
map.fillArea(0, 0, 0, 9, preconstructed["wall"])
map.fillArea(9, 9, 0, 9, preconstructed["wall"])
print(map)

while True:
    stuff = input()
