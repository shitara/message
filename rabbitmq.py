
from pika import (
    BlockingConnection, ConnectionParameters
    )

from core.util.json import dumps

class Connection(object):

    def __init__(self, host):
        self.conn = BlockingConnection(
            ConnectionParameters(host = host)
            )
        self.channel = self.conn.channel()

    def publish(self, name, value):
        self.channel.queue_declare(queue = str(name))
        self.channel.basic_publish(
            exchange = '',
            routing_key = str(name),
            body = dumps(value),
            )

    def cancel(self, id):
        pass
