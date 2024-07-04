from concurrent.futures import ThreadPoolExecutor
from settings import THREADS_NUMBER
from rabbitmq import consume_messages
from time import time

print(time())
num_threads = THREADS_NUMBER
executor = ThreadPoolExecutor(max_workers=THREADS_NUMBER)

for _ in range(num_threads):
    executor.submit(consume_messages)


