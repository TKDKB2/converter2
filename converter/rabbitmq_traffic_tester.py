import pika
from datetime import datetime
from settings import RABBITMQ_PASSWORD, RABBITMQ_USERNAME, RABBITMQ_EXCHANGE, RABBITMQ_EXCHANGE_TYPE, RABBITMQ_EXCHANGE_DURABLE, RABBITMQ_HOST, RABBITMQ_QUEUE, RABBITMQ_QUEUE_DURABLE, ROUTING_KEY


credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials))
channel = connection.channel()

try:
    channel.exchange_declare(exchange=RABBITMQ_EXCHANGE, exchange_type=RABBITMQ_EXCHANGE_TYPE, durable=RABBITMQ_EXCHANGE_DURABLE)
    print("Exchange 'test' successfully declared.")
except Exception as e:
    print("Failed to declare exchange 'test':", e)

try:
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=RABBITMQ_QUEUE_DURABLE)
    print("Queue 'test' successfully declared.")
except Exception as e:
    print("Failed to declare queue 'test':", e)

try:
    channel.queue_bind(exchange=RABBITMQ_EXCHANGE, queue=RABBITMQ_QUEUE, routing_key=ROUTING_KEY)
    print("Queue 'test' successfully bound to exchange 'test' with routing key 'a'.")
except Exception as e:
    print("Failed to bind queue 'test' to exchange 'test':", e)

messages = ['{"path": "/test_folder/sample-5s.mp4", "flags": [], "output": ""}', '{"path": "/test_folder/sample-10s.mp4", "flags": [], "output": ""}', '{"path": "/test_folder/sample-15s.mp4", "flags": [], "output": ""}', '{"path": "/test_folder/sample-20s.mp4", "flags": [], "output": ""}', '{"path": "/test_folder/sample-30s.mp4", "flags": [], "output": ""}']

for message in messages:
    channel.basic_publish(exchange=RABBITMQ_EXCHANGE, routing_key=ROUTING_KEY, body=message)
    print("message sent", datetime.now())
    # print(" [x] Sent message:", message)

connection.close()
