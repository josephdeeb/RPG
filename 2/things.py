class Enum:
    pass

class State:
    def __init__(self, name, transitions, char):
        # String
        self.name = name
        # Dict where keys are action Strings, values are a 2tuple with (amount, stateName to go to)
        # If amount is negative, it means less than or equal to (amount)
        self.transitions = transitions
        # Char
        self.char = char

class Thing:
    def __init__(self, name, states, currentState, attributes):
        # String
        self.name = name
        # Dictionary
        self.states = states
        # MAKE SURE currentState IS IN states beforehand!!!
        self.currentState = currentState
        # Dict of attributes this thing has
        self.attributes = attributes

    def isCharable(self):
        return self.currentState.char != None10

    def getChar(self):
        return self.currentState.char

    def getName(self):
        return self.currentState.name

    def changeState(self, name):
        self.currentState = states[name]

    def update(self, action, amount = 0):

        """
        if action in self.currentState.transitions.keys():
            transition = self.currentState.transitions[action]
            if amount >= transition[0]:
                changeState(transition[1])
        """

defaultAttributes = {
    "Health": 0,
    "Mana": 0,
    "Armor": 0,
}

dungeonFloorTransitions = {
    "ATTR_HEALTH": {"STATE_NORMAL": ("<=0", "STATE_BROKEN"), "STATE_BROKEN": (">=0", "STATE_NORMAL")},
}


"""
dungeonFloorTransitions = {
    # if dungeonFloor has attribute named HEALTH, if dungeonFloor is in state NORMAL, if HEALTH is less than or equal to 10, change state to BROKEN
    "ATTR_HEALTH": {"STATE_NORMAL": (-10, "STATE_BROKEN")},
    "HEALED": {"STATE_"}
}
"""

"""
dungeonFloorNotBrokenTransitions = {
    "HEALTH": (-10, "BROKEN")
}

dungeonFloorBrokenTransitions = {
    "REPAIR": (0, "NOTBROKEN")
}
"""
