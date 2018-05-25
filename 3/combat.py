import random

class CombatQueue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, action):
        self.queue.append(action)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return None

class CombatAction:
    def __init__(self, actor, target, action):
        self.actor = actor
        self.target = target
        self.action = action

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
        for x in range(len(self.map)):
            if self.map[x].contains(id):
                self.map[x].remove(id)
                newX = x + amount
                if newX >= len(self.map):
                    self.map[len(self.map)-1].add(id)
                    return True
                if newX < 0:
                    self.map[0].add(id)
                    return True
                self.map[newX].add(id)
                return True
        return False

    def retrieveCombattant(self, id):
        return self.combattants[id]

class Combattant:
    def __init__(self, hp=5, damage=1, char, name, id):
        self.hp = hp
        self.damage = damage
        self.char = char
        self.id = id

    def takeDamage(self, damage):
        newhp = self.hp - damage
        if newhp < 0:
            self.hp = 0
        else:
            self.hp = newhp

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
