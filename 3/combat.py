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

    def add(self, combattant):
        if len(bucket) >= maxSize:
            return False
        bucket.append(combattant)
        return True

class BattleMap:
    def __init__(self, combattants, size=6):
        self.combattants = combattants
        self.size = size
        self.map = [[] for x in range(size)]

class Combattant:
    def __init__(self, hp=5, damage=1, char):
        self.hp = hp
        self.damage = damage
        self.char = char

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
