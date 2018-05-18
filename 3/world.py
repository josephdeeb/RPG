class State:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def getDesc(self):
        return self.desc

defaultExits = {
    "north": None,
    "east": None,
    "south": None,
    "west": None,
    "up": None,
    "down": None
}

class Room:
    def __init__(self, initState, states = {"init": initState}, exits = dict(defaultExits), things = []):
        self.state = initState
        self.states = states
        self.exits = exits
        self.things = things

    def getState(self):
        return self.state

class Thing:
    def __init__(self, ID, name, room = None):
        self.ID = ID
        self.attributes = {
            "name": name,
            "takeable": False,
            "pushable": False,

        }
        self.room = room

    def getID(self):
        return self.ID

    def getAttribute(self, string):
        return self.attributes[string]

    def setAttribute(self, name, change):
        self.attributes[name] = change

    def getRoom(self):
        return self.room
