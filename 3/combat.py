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

def combat(sideOne, sideTwo):


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
