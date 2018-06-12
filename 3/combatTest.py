import combat as cb

wizard = cb.SimpleCombattant("A", "Wizard", 1, 3, 2, 0)
wizard2 = cb.SimpleCombattant("A", "Wizard", 2, 3, 2, 0)
warrior = cb.SimpleCombattant("B", "Warrior", 3, 5, 1, 3)
wizard3 = cb.SimpleCombattant("A", "Wizard", 4, 3, 2, 1)
bm = cb.BattleMap()

combattants = [wizard, wizard2, warrior, wizard3]

for x in range(len(combattants)):
    bm.addCombattant(combattants[x])


print(bm.getAllChars(0))
print(bm.getAllChars(1))
print(bm.getAllChars(2))
print(bm.getAllChars(3))
print(bm.getAllChars(4))
print(cb.generateInterface(bm, 79, 10))
