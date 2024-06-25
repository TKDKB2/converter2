import pika
from settings import RABBITMQ_PASSWORD, RABBITMQ_USERNAME, RABBITMQ_EXCHANGE, RABBITMQ_EXCHANGE_TYPE, RABBITMQ_EXCHANGE_DURABLE, RABBITMQ_HOST, RABBITMQ_QUEUE, RABBITMQ_QUEUE_DURABLE, ROUTING_KEY, RABBITMQ_QUEUE_RESULT, RABBITMQ_QUEUE_RESULT_DURABLE, ROUTING_KEY_RESULT


def send_conversion_success_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    channel.exchange_declare(exchange=RABBITMQ_EXCHANGE, exchange_type=RABBITMQ_EXCHANGE_TYPE, durable=RABBITMQ_EXCHANGE_DURABLE)

    channel.basic_publish(
        exchange=RABBITMQ_EXCHANGE,
        routing_key=ROUTING_KEY_RESULT,
        body=message
    )

    print("Сообщение об успешной конвертации отправлено в отдельную очередь")

    connection.close()
