import things

class Action(Descriptable):
    """

    """
    def __init__(self, name, desc):
        self.name = name
        Descriptable.__init__(desc)


class Location(IDAble, Descriptable):
    """
    Variables:
        ID, name, desc: ID, name, and description
        inventory:      Inventory of all things in the location
        states:         Possible locations that this location can become (Forest has a burnt state, cave has a collapsed state, etc.)
        exits:          All possible exits
        locationSet:    All sub-locations within this location
    """
    def __init__(self, ID, name, desc, inventory = Inventory(), states = {}, exits = {}, superLocation = None, locationSet = None):
        IDAble.__init__(ID)
        self.name = name
        Descriptable.__init__(desc)
        self.inventory = inventory
        self.states = states
        self.exits = exits
        self.locationSet = locationSet
        self.superLocation = superLocation

    def changeState(self, Action):

    """

    """
    def getDesc(self):




class World:
    def __init__(self, name, height = 0, width = 0) :
        self.name = name
        self.locations = [[0 for x in range(width)] for y in range(height)] #Verify this works



study = Location(0, "Study", "")


"""
    TEST:
        Study with a button on the desk underneath some papers.  Clearing the papers reveals a button, then hitting the button opens a doorway to a dark hallway.

    Location with a desk in its inventory, the desk has a button in ITS inventory with status "not visible".  Action of clearing the papers makes the button visible.
"""
