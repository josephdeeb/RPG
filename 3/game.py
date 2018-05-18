import world

def splitInput(input):


actions = {
    
}


class DatabaseWrapper:
    def __init__(self, fileName):
        self.fileName = fileName
        self.connected = False
        self.db = None
        self.cur = None

    def openDB(self):
        try:
            self.db = sql.connect(fileName)
            self.cur = db.cursor()
            self.connected = True
        except lite.Error, e:
            self.connected = False

    def closeDB(self):
        if self.db:
            self.db.close()

    def createTable(self, name, fields):
        if self.connected:
            string = ""
            for i in range(len(fields)):
                if i < (len(fields) - 1):
                    string += (fields[i] + ", ")
                else:
                    string += (fields[i])

            self.cur.execute("CREATE TABLE {}({})".format(name, string))
            # MAY NEED TO USE WITH STATEMENT
            # ALSO MAY NEED TO INITIALIZE CURSOR (Dunno how it works yet)

    def insert(self, table, values):
        if self.connected:
            string = ""
            for i in range(len(values)):
                if i < (len(values) - 1):
                    string += (values[i] + ",")
                else:
                    string += (values[i])

            self.cur.execute("INSERT INTO {} VALUES({})".format(table, string))

class Account:
    def __init__(self, userName, character = None):
        self.userName = userName
        self.character = character

    def setCharacter(self, thing):
        self.character = thing

class IOWrapper:
    def __init__(self):
        pass

    def input(self):
        return "input() NOT DEFINED FOR IOWrapper"

    def output(self, msg):
        return "output() NOT DEFINED FOR IOWrapper

"""
class terminalInput(IOWrapper):
    def __init__(self):
        pass

    def input(self):
        returned = input()
        return returned

    def output(self, string):
        print(string)

def getRoomDesc(thing):
    return thing.getRoom().getState().getDesc()
"""
