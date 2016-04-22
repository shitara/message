
import math
from pystalkd import Beanstalkd

from core.util.json import dumps

class Connection(object):

    def __init__(self, host):
        self.conn = Connection(host)

    def publish(self, name, value, delay = 0):
        with self.conn.temporary_use(name):
            self.conn.put(
                dumps(values), delay=max(
                    0, math.ceil(delay))
                )

    def cancel(self, id):
        pass
