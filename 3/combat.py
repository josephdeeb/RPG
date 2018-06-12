import random

"""
Bugs that will probably arise:
    When checking duplicates in battleMap and changing temp chars, the map printing function is not prepared to deal with any two digit duplicate count

"""


"""
def roll(amount, sides):
    result = 0
    print("\nRolling {}d{}...".format(amount,sides))
    for i in range(amount):
        rand = random,randint(1, sides)
        print("Roll #{} = {}".format(i, rand))
        result += rand
    print("Total: {}\n".format(result))
    return result
"""

# taken from https://stackoverflow.com/questions/1541797/how-do-i-check-if-there-are-duplicates-in-a-flat-list?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# FIX THIS:
# THIS WON'T CONSISTENTLY KEEP CHARACTERS AS 1 OR 2, ETC.
# FIXED IN BATTLEMAP AS changeTempCharDuplicates(), THIS FUNCTION IS NOW DEFUNCT
def checkDuplicates(theList):
    seen = set()
    count = {x: -1 for x in theList}

    for x in range(len(theList)):
        if theList[x] == " " or theList[x] == "_":
            pass
        else:
            count[theList[x]] += 1
            if theList[x] in seen:
                theList[x] = theList[x] + " " + str(count[theList[x]])

        seen.add(theList[x])

    return theList


def generateInterface(bm, width, height):
    final = "╔" + ("═" * (width - 2)) + "╗\n"
    counter = 2
    maxChars = 0
    offset = 0
    # Figure out ithere are any repeats in allChars...
    merged = []
    bm.changeTempCharDuplicates()
    for x in range(len(bm.map)):
        merged += bm.getAllChars(x, True)[::-1] #the [::-1] puts it in reverse so it's bottom aligned
        merged += ["_"]
    print(merged)
    #merged = checkDuplicates(merged)
    #print(merged)

    # For each row in map:
    for x in range(bm.getFullMaxSize()+1): #+1 accounts for extra space for the underscore
        final += "║ "
        # For each column in the map:
        for i in range(len(bm.map)):
            char = merged[(i*(bm.getFullMaxSize()+1)) + x] #+1 accounts for extra space for the underscore
            if len(char) > 1:
                final += char

            else:
                final += (" " + char + " ")

        final += " ║\n"

    return final



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

"""

class BattleMapBucket:
    def __init__(self, maxSize=4, bucket=False):
        self.maxSize = maxSize
        if bucket == False:
            self.bucket = []
        else:
            self.bucket = bucket

    def getSize(self):
        return len(self.bucket)

    def getMaxSize(self):
        return self.maxSize

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

    def isFull(self):
        if len(self.bucket) >= self.maxSize:
            return True

        return False

    def __len__(self):
        return len(self.bucket)


class BattleMap:
    def __init__(self, combattants={}, size=6):
        self.combattants = combattants
        self.map = [BattleMapBucket() for x in range(size)]

    def changeTempCharDuplicates(self):
        seen = set()
        count = {y.char: -1 for x, y in self.combattants.items()}
        for key, value in self.combattants.items():
            count[value.char] += 1
            #If the character has been seen before:
            if value.char in seen:
                # Set the tempChar of the combattant to be it + its count
                value.tempChar = value.char + " " + str(count[value.char])
            # Character has not been seen before
            else:
                value.tempChar = value.char
                seen.add(value.char)

    def addCombattant(self, combattant):
        if self.map[combattant.location].isFull():
            return False
        else:
            if self.map[combattant.location].add(combattant.ID) == False:
                print("ERROR: Cannot add combattant to given BattleMapBucket")
                return False
            else:
                self.combattants[combattant.ID] = combattant
                return True


    def getMaxSize(self):
        maxSize = 0

        for thing in self.map:
            if thing.getSize() > maxSize:
                maxSize = thing.getSize()

        return maxSize

    def getFullMaxSize(self):
        maxSize = 0
        for thing in self.map:
            if thing.getMaxSize() > maxSize:
                maxSize = thing.getMaxSize()

        return maxSize

    def getChar(self, location, n=-1):
        if location > len(self.map) or location < 0:
            return False

        if self.map[location].isEmpty():
            return " "

        else:
            if self.map[location].getElement(n) == -1:
                return " "

            else:
                return self.retrieveCombattant(self.map[location].getElement(n)).char


    def getAllChars(self, location, temp=False):
        if location > len(self.map) or location < 0:
            return False

        returned = []
        allElements = self.map[location].getAllElements()

        if temp == False:
            for x in range(len(allElements)):
                if allElements[x] == -1:
                    returned += " "

                else:
                    returned += self.retrieveCombattant(allElements[x]).char

            newLen = self.map[location].getMaxSize() - len(returned)
            if newLen > 0:
                for x in range(newLen):
                    returned.append(" ")

        else:
            for x in range(len(allElements)):
                if allElements[x] == -1:
                    returned += " "

                else:
                    returned += [self.retrieveCombattant(allElements[x]).tempChar]
                    print(returned)

            newLen = self.map[location].getMaxSize() - len(returned)
            if newLen > 0:
                for x in range(newLen):
                    returned.append(" ")

        return returned


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
    def __init__(self, char, name, ID, location=0):
        self.char = char
        self.name = name
        self.ID = ID
        self.location = location
        self.tempChar = char

    def takeDamage(self, damage):
        return False

    def getDamage(self):
        return False


class SimpleCombattant(CombattantAbstract):
    def __init__(self, char, name, ID, health=5, damage=1, location=0):
        self.health = health
        self.damage = damage
        super().__init__(char, name, ID, location)

    def takeDamage(self, damage):
        newHealth = self.health - damage
        if newHewlth < 0:
            self.health = 0

        self.health = newHealth

    def getDamage(self):
        return self.damage

"""

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

"""
