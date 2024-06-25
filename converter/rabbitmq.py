import pika
from converter_main import main_worker
from settings import RABBITMQ_PASSWORD, RABBITMQ_USERNAME, RABBITMQ_EXCHANGE, RABBITMQ_EXCHANGE_TYPE, RABBITMQ_EXCHANGE_DURABLE, RABBITMQ_HOST, RABBITMQ_QUEUE, RABBITMQ_QUEUE_DURABLE, ROUTING_KEY, RABBITMQ_QUEUE_RESULT, RABBITMQ_QUEUE_RESULT_DURABLE, ROUTING_KEY_RESULT

def callback(ch, method, properties, body):
    message = body.decode('utf-8')
    try:
        main_worker(message)
    except Exception as e:
        print("Error")


def consume_messages():
    credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange=RABBITMQ_EXCHANGE, exchange_type=RABBITMQ_EXCHANGE_TYPE, durable=RABBITMQ_EXCHANGE_DURABLE)
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=RABBITMQ_QUEUE_DURABLE)
    channel.queue_bind(exchange=RABBITMQ_EXCHANGE, queue=RABBITMQ_QUEUE, routing_key=ROUTING_KEY)

    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')

    success_connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    success_channel = success_connection.channel()
    success_channel.exchange_declare(exchange=RABBITMQ_EXCHANGE, exchange_type=RABBITMQ_EXCHANGE_TYPE, durable=RABBITMQ_EXCHANGE_DURABLE)
    success_channel.queue_declare(queue=RABBITMQ_QUEUE_RESULT, durable=RABBITMQ_QUEUE_RESULT_DURABLE)
    success_channel.queue_bind(exchange=RABBITMQ_EXCHANGE, queue=RABBITMQ_QUEUE_RESULT, routing_key=ROUTING_KEY_RESULT)

    channel.start_consuming()



