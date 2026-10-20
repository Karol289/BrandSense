import os
import time
import pika

rabbitmq_host = os.getenv("RABBITMQ_HOST", "rabbitmq")
print(f"Connecting to RabbitMQ at {rabbitmq_host}...")

# Wait for RabbitMQ connection
while True:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
        print("Successfully connected to RabbitMQ!")
        connection.close()
        break
    except Exception as e:
        print(f"RabbitMQ not ready yet, retrying in 5s... Error: {e}")
        time.sleep(5)

print("Python Worker running continuously...")
while True:
    time.sleep(3600)