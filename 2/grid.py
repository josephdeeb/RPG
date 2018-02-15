import things

class Grid:
    def __init__(self, x, y):
        self.grid = [[' ' for i in range(x)] for j in range(y)]

    def setChar(self, x, y, char):
        self.grid[x][y] = char

class Map:
    def __init__(self, name, x, y):
        self.name = name
        self.things = [[list() for i in range(x)] for j in range(y)]

    def addThing(self, thing, x, y):
        self.things[x][y].append(thing)
