from pox.core import core
import datetime

class HostProperties (object):

    def __init__(self):
        self.log = core.getLogger()
        self.reachableThroughPorts = []
        self._knownIPsTimeout = {}
        self.lastMile = False

    def addUniquePort(self, port):
        if port not in self.reachableThroughPorts:
            self.reachableThroughPorts.append(port)

    def addUniqueIP(self, ipAddress):
        self._updateIPsTimeout(ipAddress)
        if ipAddress not in self._knownIPsTimeout:
            self._knownIPsTimeout[ipAddress] = datetime.datetime.now()

    def isIPKnown(self, ipAddress):
        self._updateIPsTimeout(ipAddress)
        return ipAddress in self._knownIPsTimeout

    def _updateIPsTimeout(self, ipAddress):
        if ipAddress in self._knownIPsTimeout:
            now = datetime.datetime.now()
            if (now - self.knownIPsTimeout[ipAddress]).seconds >= 1:
                del self.knownIPsTimeout[ipAddress]
