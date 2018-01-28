class Descriptable:
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

class IDAble:
    """
    This object has a unique ID assigned to it by the game
    """
    def __init__(self, ID):
        self.ID = ID

class Item(IDAble, Descriptable):
    def __init__(self, ID, name, desc):
        IDAble.__init__(ID);
        self.name = name
        Descriptable.__init__(desc);

class Inventory:
    def __init__(self, items = []):
        self.items = items

    def addItem(self, item):
        self.items.append(item)

    def delItem(self, index = None, ID = None):
        returned = None
        if index is not None:
            returned = self.items.pop(index)

        elif ID is not None:
            returned = self.items.pop(self.searchItems(ID)[0])

        return returned

    """
    Searches for item by name or ID, returns a list of tuples where each tuple is:
    (Item, Index)
    If searching by name, will return all items matching the name
    If searching by ID, will return only one item
    Returns an empty list if item is not found
    """
    def searchItems(self, ID = None, name = None):
        returned = []
        if ID is not None:
            for i in range(len(items)):
                if isinstance(items[i], IDAble):
                    returned.append((items[i], i))
                    break

        elif name is not None:
            for i in range(len(items)):
                if items[i].name = name:
                    returned.append((items[i], i))

        if not returned:
            returned.append((None, None))

        return returned

class Creature(IDAble, Descriptable):
    def __init__(self, ID, name, desc):
        IDAble.__init__(ID)
        self.name = name
        Descriptable.__init__(desc)
