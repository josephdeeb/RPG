
class Grid:
    def __init__(self, x, y):
        self.grid = [[' ' for i in range(x)] for j in range(y)]

    def setChar(self, x, y, char):
        self.grid[x][y] = char


class Map:
    def __init__(self, name, x, y):
        self.name = name
        self.things = [[[] for i in range(x)] for j in range(y)]
        self.x = x
        self.y = y

    def addThing(self, thing, x, y):
        self.things[x][y].append(thing)

    def getChar(self, x, y):
        return self.things[y][x][-1].getAttribute("char")

    def __str__(self):
        returned = ""
        for y in range(len(self.things)):
            for x in range(len(self.things[y])):
                returned += self.getChar(x, y)
            returned += "\n"
        return returned

class Thing:
    def __init__(self, name, char):
        self.attributes = {"char": char, "name": name}

    def getAttribute(self, string):
        return self.attributes[string]

map = Map("fuck", 10, 10)
map.addThing(Thing("wall", "@"), 0, 0)
map.addThing(Thing("wall", "@"), 0, 1)
print(map)
