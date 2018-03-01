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
        self.things[y][x].append(thing)
        thing.setAttribute("x", x)
        thing.setAttribute("y", y)

    def getThing(self, x, y):
        return self.things[y][x][-1]

    def getChar(self, x, y):
        if len(self.things[y][x]) > 0:
            return self.things[y][x][-1].getAttribute("char")
        return " "

    def pop(self, x, y, ID = None):
        if ID == None:
            return self.things[y][x].pop()
        else:
            for index, thing in enumerate(self.things):
                if thing.ID == ID:
                    return self.things[y][x].pop(index)

    def __str__(self):
        returned = ""
        for y in range(len(self.things)):
            for x in range(len(self.things[y])):
                returned += self.getChar(x, y)
            returned += "\n"
        return returned

    def fillArea(self, x1, x2, y1, y2, thing):
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                self.addThing(thing, x, y)

    # Checks to see if a new object can be added to the location by seeing if there is any unpathable things there
    def checkPathing(self, x, y):
        for i in range(len(self.things[y][x])):
            if self.things[y][x][i].getAttribute("pathable") == False:
                return False
        return True
    
    # Checks to see if there are any objects placed above an unpathable object at the given location
    # Returns True if there are no objects placed above an unpathable object
    # Returns False if there IS at least one object placed above an unpathable object
    def validatePathing(self, x, y):
        previous = False
        for i in range(len(self.things[y][x])):
            if previous:
                return False
            if self.things[y][x][i].getAttribute("pathable") == False:
                previous = True
        return True


class Thing:
    def __init__(self, ID, name, char, pathable = True):
        self.ID = ID
        self.attributes = {
            "char": char,
            "name": name,
            "pathable": pathable,
            "x": None,
            "y": None
        }

    def getID(self):
        return self.ID

    def getAttribute(self, string):
        return self.attributes[string]

    def setAttribute(self, name, change):
        self.attributes[name] = change


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
