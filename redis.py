
import redis

from core.util.json import dumps

class Connection(object):

    def __init__(self, **kwargs):
        self.conn = redis.StrictRedis(
            host = kwargs.get('host'),
            port = kwargs.get('port'),
            )
        self.name = kwargs.get('name')

    def publish(self, name, value, options = dict()):
        self.conn.publish(str(self.name), dumps(dict(
                channel = name,
                data = dict(value),
                ))
            )

    def cancel(self, id):
        pass