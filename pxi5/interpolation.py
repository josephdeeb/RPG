import time

class Message:
    def __init__(self, contents, step):
        self.contents = contents
        self.step = step

class Client:
    def __init__(self, name, server):
        self.name = name
        self.server = server
        self.history = {}
        self.location = tuple(0, 0)

    def sendMessage(self, content):
        step = time.time()
        self.server.receiveMessage(Message(content, step)

    def receieveMessage(self, msg):
        if self.history{msg.step} == msg.step:
            # Our history regarding that moment in time is correct with what the server said it should be
            self.history{msg.step} = None

        else:
            # Our history regarding that moment in time is INCORRECT with what the server said it should be
            # As a result, our position must be changed so that all our inputs from that time onward occured as if this WERE our position

class Server:
    def __init__(self, name):
        self.name = name
        # List of clients, where each client reference goes to a 2-tuple of (x, y), which is the server position of the client.
        self.clients = list()

    def register(self, client):
        self.clients += [client]
        print("{} registered to {}".format(client.name, self.name))

    def unregister(self, client):
        self.clients.remove(client)

    def receiveMessage(self, msg):
