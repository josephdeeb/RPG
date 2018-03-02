import grid

things = 0

def makeID():
    things += 1
    return things

class IOWrapper:
    def __init__(self):
        pass
    
    def input(self):
        return "input() NOT DEFINED FOR IOWrapper"
    
    def output(self):
        return "output() NOT DEFINED FOR IOWrapper
