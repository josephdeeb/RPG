class Enum:

class Requirement:
    def __init__(self, name, amount):
        # Name of the thing being polled for requirement
        # String
        self.name = name
        # Amount required of the thing being polled for requirement
        # Integer
        self.amount = amount

class Transition:
    def __init__(self, action, requirement, state):
        # String
        self.action = action
        # Requirement
        self.requirement = requirement
        # State which the transition takes you to
        # State
        self.state = state

class State:
    def __init__(self, name, transitions, char):
        # String
        self.name = name
        # Dict where keys are action Strings, values are transitions
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

    def update(self, action, thing):
        if

dftransitions = {
    "FORCE": Transition()
}

things = [
    Thing("Dungeon Floor", ),
    Thing("Dungeon Wall", '#'),
    Thing("Wooden Rope Bridge", '=')
]
