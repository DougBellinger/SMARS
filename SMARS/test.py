from twisted.internet import task
from twisted.internet import reactor, protocol, endpoints
from twisted.protocols import basic
import time

i = 0  


def tick():
    global i
    i = i + 1
    if (i >= 100):
        i = 0
        print(time.time())


l = task.LoopingCall(tick) 
print(time.time())
l.start(0.01)
 

class PubProtocol(basic.LineReceiver):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.clients.add(self)

    def connectionLost(self, reason):
        self.factory.clients.remove(self)

    def lineReceived(self, line):
        for c in self.factory.clients:
            source = u"<{}> ".format(self.transport.getHost()).encode("ascii")
            print(line)
            c.sendLine(source + line)


class PubFactory(protocol.Factory):
    def __init__(self):
        self.clients = set()

    def buildProtocol(self, addr):
        return PubProtocol(self)


endpoints.serverFromString(reactor, "tcp:1025").listen(PubFactory())

reactor.run()
