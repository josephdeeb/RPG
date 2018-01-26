class Description:
    """
    We need to have the description object represent various descriptions depending upon player status, items, etc.
    """
    def __init__(self, desc):
        self.desc = desc

    """
    This will be the function that determines what description to use.
    """
    def getDesc(self):
        return desc


class Location:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

class World:
    def __init__(self, name, height = , width) :
        self.name = name
        self.locations = [[]]
