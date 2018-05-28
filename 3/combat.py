import random

def roll(amount, sides):
    result = 0
    print("\nRolling {}d{}...".format(amount,sides))
    for i in range(amount):
        rand = random,randint(1, sides)
        print("Roll #{} = {}".format(i, rand))
        result += rand
    print("Total: {}\n".format(result))
    return result


def generateMapLine(bm, width):
    final = "║"
    counter = 2
    allChars = []
    for char in

# taken from https://stackoverflow.com/questions/1541797/how-do-i-check-if-there-are-duplicates-in-a-flat-list?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
def checkDuplicates(theList):
    seen = set()
    for x in range(len(theList)):
        if theList[x] in seen:
            theList[x] = theList[x] + " "
            return True
        seen.add(theList[x])
    return False

def generateInterface(bm, width, height):
    final = "╔" + ("═" * width - 2) + "╗\n"
    final += "║"
    counter = 2
    allChars = []
    maxChars = 0
    for i in range(len(bm.map)):
        allChars.append(bm.getAllChars(i))
        if len(allChars[i]) > maxChars:
            maxChars = len(allChars[i])

    # Figure out ithere are any repeats in allChars...
    for i in

    for i in range(len(bm.map)):
        # if we have exhausted all available space, just stop printing the map.
        if counter >= width:
            final += "║"
            break
        # Otherwise, we have more space, add a space and then the appropriate char for the map
        final += " " + allChars........



#79 max width


"""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║                                                                             ║
║ É 2                                                                         ║
║ É 1  _   _   Ú   Ü   _   _                                                  ║
║                                                                             ║
║                                                                             ║
║                                                                             ║
║                                                                             ║
║                                                                             ║
║                                                                             ║
║ What would you like to do?                                                  ║
╚═════════════════════════════════════════════════════════════════════════════╝
"""



interface = """
╔════════════════════════════╗
║ {0} {1} {2} {3} {4}                  ║
║  0   1   2   3   4         ║
║ {0}:{5}                        ║
║ {1}:{6}                        ║
║                            ║
║                            ║
║                            ║
║ What would you like to do? ║
╚════════════════════════════╝
"""

class IOAbstract:
    def getInput(self):
        return False

    def output(self, string):
        return False

class IOCommandLine(IOAbstract):
    def getInput(self):
        string = input()

    def output(self, string):
        print(string)

class BattleHandler:
    def __init__(self, BattleMap, IO):
        self.BattleMap = BattleMap
        self.IO = IO

    def mainLoop(self):
        battleGoing = True
        while battleGoing:


class BattleMapBucket:
    def __init__(self, bucket=[], maxSize=4):
        self.bucket = bucket
        self.maxSize = maxSize

    def getSize(self):
        return len(self.bucket)

    def add(self, id):
        if len(self.bucket) >= self.maxSize:
            return False

        self.bucket.append(id)
        return True

    def remove(self, id):
        self.bucket.remove(id)

    def contains(self, id):
        if id in self.bucket:
            return True

        return False

    def getElement(self, n):
        if len(self.bucket) < n:
            return self.bucket[n]

        return False

    def getAllElements(self):
        return list(self.bucket)

    def isEmpty(self):
        if len(self.bucket) > 0:
            return False

        return True

    def __len__(self):
        return len(self.bucket)

class BattleMap:
    def __init__(self, combattants, size=6):
        self.combattants = combattants
        self.map = [BattleMapBucket() for x in range(size)]

    def getMaxSize(self):
        maxSize = 0
        for thing in self.map:
            if thing.getSize() > maxSize:
                maxSize = thing.getSize()

        return maxSize

    def getChar(self, location, n=-1):
        if n = -1:
            if location > len(self.map) or location < 0:
                return False

            if self.map[location].isEmpty():
                return " "

            return retrieveCombattant(self, self.map[location].getElement(0)).char

        else:
            char = retrieveCombattant(self.map[location].getElement(n)).char

    def getAllChars(self, location, numbered=False):
        if location > len(self.map) or location < 0:
            return False

        if self.map[location].isEmpty():
            return [" "]

        if numbered == False:
            return [retrieveCombattant(x).char for x in self.map[location].getAllElements()]

        else:
            returned = []
            seen = set()
            for x in self.map[location].getAllements():
                char = retrieveCombattant(x).char
                if char

    def move(self, id, amount):
        combattant = self.retrieveCombattant(id)
        position = combattant.location
        newPos = position + amount
        if newPos >= len(self.map):
            newPos = len(self.map) - 1

        elif newPos < 0:
            newPos = 0

        if self.map[newPos].add(id) == True:
            self.map[position].remove(id)
            combattant.location = newPos
            return True

        else:
            return False

    def retrieveCombattant(self, id):
        return self.combattants[id]

    def getDistance(self, id1, id2):
        return -(self.retrieveCombattant(id1).location - self.retrieveCombattant(id2).location)


class CombattantAbstract:
    def __init__(self, location=0, char, name, ID):
        self.location = location
        self.char = char
        self.ID = ID

    def takeDamage(self, damage):
        return False

    def getDamage(self):
        return False

class SimpleCombattant(CombattantAbstract):
    def __init__(self, health=5, damage=1, location=0, char, name, ID):
        self.health = health
        self.damage = damage
        super().__init__(location, char, ID)

    def takeDamage(self, damage):
        newHealth = self.health - damage
        if newHewlth < 0:
            self.health = 0

        self.health = newHealth

    def getDamage(self):
        return self.damage


class DMG_TYPE:
    PIERCE = 1
    SLASH = 2
    CRUSH = 3

class Combatter:
    def __init__(self, health=100, mana=100, pierceDef=0, slashDef=0, crushDef=0, pierceBonus=0, slashBonus=0, crushBonus=0):
        self.health = health
        self.mana = mana
        self.pierceDef = pierceDef
        self.slashDef = slashDef
        self.crushDef = crushDef
        self.pierceBonus = pierceBonus
        self.slashBonus = slashBonus
        self.crushBonus = crushBonus
        self.defenses = {DMG_TYPE.PIERCE : pierceDef, DMG_TYPE.SLASH : slashDef, DMG_TYPE.CRUSH : crushDef}

    def takeDamage(self, roll, type):
        defense = self.defenses[type]
        damage = int(round(roll * defense))
        self.health = self.health - damage
