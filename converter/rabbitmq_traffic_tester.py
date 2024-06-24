import pika
from datetime import datetime

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
channel = connection.channel()

try:
    channel.exchange_declare(exchange='test', exchange_type='direct', durable=True)
    print("Exchange 'test' successfully declared.")
except Exception as e:
    print("Failed to declare exchange 'test':", e)

try:
    channel.queue_declare(queue='test', durable=True)
    print("Queue 'test' successfully declared.")
except Exception as e:
    print("Failed to declare queue 'test':", e)

try:
    channel.queue_bind(exchange='test', queue='test', routing_key='a')
    print("Queue 'test' successfully bound to exchange 'test' with routing key 'a'.")
except Exception as e:
    print("Failed to bind queue 'test' to exchange 'test':", e)

messages = ['{"path": "/test_folder/sample-5s.mp4", "flags": [], "output": ""}', '{"path": "/test_folder/sample-10s.mp4", "flags": [], "output": ""}', '{"path": "/test_folder/sample-15s.mp4", "flags": [], "output": ""}', '{"path": "/test_folder/sample-20s.mp4", "flags": [], "output": ""}', '{"path": "/test_folder/sample-30s.mp4", "flags": [], "output": ""}']

for message in messages:
    channel.basic_publish(exchange='test', routing_key='a', body=message)
    print("message sent", datetime.now())
    # print(" [x] Sent message:", message)

connection.close()
