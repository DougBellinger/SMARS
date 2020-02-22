from twisted.internet import task
from twisted.internet import reactor, protocol, endpoints
from twisted.protocols import basic
import time
import motors
import json
import logging 
logging.basicConfig(level=logging.DEBUG)
if __debug__:
    import sys
    sys.path.append(r'/usr/lib/cgi-bin')
    sys.path.append(r'/home/pi/SMARS')
    import pydevd  # @UnresolvedImport
    pydevd.settrace('192.168.2.63') # replace IP with address
                                # of Eclipse host machine



logger = logging.getLogger(__name__)
i = 0
ticks = 0
guard_timer = 100 #   
def tick():
    global i, guard_timer, ticks
    if (guard_timer > 0): 
        guard_timer = guard_timer - 1
        if (guard_timer == 0):
            logger.debug('Guard Timer fired')
            m.stop()
            
    i = i + 1
    if (i >= 100):
        i = 0
        ticks = ticks + 1


l = task.LoopingCall(tick) 
logger.info("Starting Timer")
l.start(0.01)
 
class Command(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)
        
class PubProtocol(basic.LineReceiver):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.clients.add(self)

    def connectionLost(self, reason):
        self.factory.clients.remove(self)

    def lineReceived(self, line):
        global guard_timer, m
        for c in self.factory.clients:
            source = u"<{}> ".format(self.transport.getHost()).encode("ascii")
            logger.info("Received command: %s", line)
            try:
                command = Command(line.decode('utf-8'))
                commands = { 
                    "F" : m.fwd 
                    }
                for attr, value in command.__dict__.items():
                    function = commands.get(attr)
                    if (function != None):
                        fValue = float(value);
                        guard_timer = function(fValue)
                        logger.info("Function %s(%f) returned %d", attr, fValue, guard_timer)
                    else:
                        logger.info("Unknown command %s(%d)", attr, value)
            except:
                logger.exception("Failed to parse command")
            c.sendLine(source + line)


class PubFactory(protocol.Factory):
    def __init__(self):
        self.clients = set()

    def buildProtocol(self, addr):
        return PubProtocol(self)

try:
    endpoints.serverFromString(reactor, "tcp:1025").listen(PubFactory())
    m = motors.Motors()
    reactor.run() #@UndefinedVariable
except:
    logger.exception("Unhandled exception");
    m.end()
