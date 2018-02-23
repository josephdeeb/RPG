
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
        if len(self.things[y][x]) > 0:
            return self.things[y][x][-1].getAttribute("char")
        return " "

    def __str__(self):
        returned = ""
        for y in range(len(self.things)):
            for x in range(len(self.things[y])):
                returned += self.getChar(x, y)
            returned += "\n"
        return returned

    def fillArea(self, x1, x2, y1, y2, thing):
        for y in range(abs(y2 - y1)):
            for x in range(abs(x2 - x1)):
                self.addThing(thing, x, y)

    #FINISH THIS
    def validate(self, x, y):
        for i in range(len(self.things[y][x])):
            self.things[y][x][i]


class Thing:
    def __init__(self, name, char, pathable = True):
        self.attributes = {
            "char": char,
            "name": name,
            "pathable": pathable
        }

    def getAttribute(self, string):
        return self.attributes[string]

map = Map("fuck", 10, 10)
map.addThing(Thing("wall", "@"), 0, 0)
map.addThing(Thing("wall", "@"), 0, 1)
map.addThing(Thing("floor", "#"), 0, 1)
print(map)

map.fillArea(0, 5, 0, 5, Thing("floor", "#"))
print(map)
