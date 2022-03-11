import pika
import conf


class Errors:
    unprocessable_entity = -3
    invalid_request = -1
    database_not_avalable = -2


def send_execute(queue, body, exchange=''):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=conf.rbt_host, port=conf.rbt_port))
        channel = connection.channel()
        channel.queue_declare(queue=queue)
    except:
        return -2
    channel.basic_publish(exchange='', routing_key=queue, body=body)
    connection.close()
    return 0


from . import send
