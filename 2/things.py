class Enum:
    pass

class State:
    def __init__(self, name, transitions, char):
        # String
        self.name = name
        # Dict where keys are action Strings, values are a 2tuple with (amount, State)
        self.transitions = transitions
        # Char
        self.char = char

class Thing:
    def __init__(self, name, states, currentState):
        # String
        self.name = name
        # Dictionary
        self.states = states
        # MAKE SURE currentState IS IN states beforehand!!!
        self.currentState = currentState

    def isCharable(self):
        return currentState.char != None

    def getChar(self):
        return currentState.char

    def update(self, action, thing, amount = None):
        if action in self.currentState.transitions.keys():
            transition = self.currentState.transitions[action]
            if



dftransitions = {
    "DAMAGE": Transition()
}

things = [
    Thing("Dungeon Floor", ),
    Thing("Dungeon Wall", '#')
]
