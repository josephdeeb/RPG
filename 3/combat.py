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

class BattleMapBucket:
    def __init__(self, bucket=[], maxSize=5):
        self.bucket = bucket
        self.maxSize = maxSize

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

class BattleMap:
    def __init__(self, combattants, size=6):
        self.combattants = combattants
        self.map = [BattleMapBucket() for x in range(size)]

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
        

class Combattant:
    def __init__(self, location=0, char, name, ID):
        self.location = location
        self.char = char
        self.ID = ID

    def takeDamage(self, damage):
        return False

    def getDamage(self):
        return False

class SimpleCombattant(Combattant):
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
