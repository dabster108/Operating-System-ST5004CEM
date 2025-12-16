import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()
channel.queue_declare(queue = 'task_queue')

def callback(ch, method, properties, body):
    print("Received :", body.decode())

channel.basic_consume(
    queue = 'task_queue',
    on_message_callback = callback,
    auto_ack = True
)
print("waiting for message")
channel.start_consuming()