import pika
from converter_main import main_worker

def callback(ch, method, properties, body):
    message = body.decode('utf-8')
    main_worker(message)


def consume_messages():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange='test', exchange_type='direct', durable=True)
    channel.queue_declare(queue='test', durable=True)
    channel.queue_bind(exchange='test', queue='test', routing_key='a')

    channel.basic_consume(queue='test', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')

    channel.start_consuming()
