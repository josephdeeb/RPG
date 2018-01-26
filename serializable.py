def start(str):
    return "<" + str + ">"

def close(str):
    return "</" + str + ">"

primitives = (int, float, bool, str)

class Serializable:
    def __init__(self):
        pass

    def serialize(self, level):
        string = ("\t" * level) + start(self.__class__.__name__) + "\n"
        level += 1
        attr = vars(self)
        if isinstance(attr, dict):
            for key, value in attr.items():
                if isinstance(value, primitives):
                    string += ("\t" * level) + start(key + " type=\"" + value.__class__.__name__ + "\"") + str(value) + close(key) + "\n"
                elif isinstance(value, Serializable):
                    string += value.serialize(level)
        string += ("\t" * (level - 1)) + close(self.__class__.__name__) + "\n"
        level -= 1
        return string



def loadSerializable():
    


class Race(Serializable):
    def __init__(self, name):
        super().__init__()
        self.name = name

class Person(Serializable):
    def __init__(self, name, age, race):
        super().__init__()
        self.name = name
        self.age = age
        self.race = race

white = Race("white")

joe = Person("joe", 19, white)

print(joe.serialize(0))
