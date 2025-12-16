import pika 

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

channel.queue_declare(queue='task_queue')

message = " hello from me "
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message

)
print("Sent:", message)