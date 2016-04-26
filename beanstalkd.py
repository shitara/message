
import math
from pystalkd import Beanstalkd

from core.util.json import dumps

class Connection(object):

    def __init__(self, **kwargs):
        self.conn = Beanstalkd.Connection(kwargs.get('host'))

    def publish(self, name, value, options = dict()):
        with self.conn.temporary_use(name):
            self.conn.put(
                dumps(value), delay=max(
                    0, math.ceil(options.get('delay', 0)))
                )

    def cancel(self, id):
        pass
