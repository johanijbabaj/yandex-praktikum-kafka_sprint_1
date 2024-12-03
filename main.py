import os
import threading
from modules.producer import Producer
from modules.consumer_pull import PullConsumer
from modules.consumer_push import PushConsumer
from config.logging_config import configure_logging

def main():
    configure_logging()

    broker = "localhost:9094"
    topic = "my-topic"
    pull_group = os.getenv("KAFKA_GROUP_PULL", "pull-group")
    push_group = os.getenv("KAFKA_GROUP_PUSH", "push-group")


    # Инициализация продюсера
    producer = Producer(broker, topic)
    producer_thread = threading.Thread(target=producer.produce_messages, daemon=True)
    producer_thread.start()

    # Инициализация PullConsumer
    pull_consumer = PullConsumer(broker, topic, pull_group)
    pull_consumer_thread = threading.Thread(target=pull_consumer.consume_messages, daemon=True)
    pull_consumer_thread.start()

    # Инициализация PushConsumer
    push_consumer = PushConsumer(broker, topic, push_group)
    push_consumer_thread = threading.Thread(target=push_consumer.start, daemon=True)
    push_consumer_thread.start()

    # Поддержка программы в активном состоянии
    producer_thread.join()
    pull_consumer_thread.join()
    push_consumer_thread.join()

if __name__ == "__main__":
    main()
