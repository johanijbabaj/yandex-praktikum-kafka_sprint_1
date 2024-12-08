import os
import threading
from dotenv import load_dotenv
from modules.producer import Producer
from modules.consumer_pull import PullConsumer
from modules.consumer_push import PushConsumer
from config.logging_config import configure_logging


def main():
    configure_logging()

    load_dotenv()
    broker = os.getenv("KAFKA_BROKER", "localhost:9090")
    topic = os.getenv("KAFKA_TOPIC", "my-topic")
    pull_group = os.getenv("KAFKA_GROUP_PULL", "pull-group")
    push_group = os.getenv("KAFKA_GROUP_PUSH", "push-group")

    # Initialize the producer instance
    producer = Producer(broker, topic)

    # Start the producer in a separate thread for asynchronous message production
    producer_thread = threading.Thread(target=producer.produce_messages, daemon=True)
    producer_thread.start()

    # Initialize the PullConsumer instance
    pull_consumer = PullConsumer(broker, topic, pull_group)

    # Start the PullConsumer in a separate thread for manual batch message consumption
    pull_consumer_thread = threading.Thread(target=pull_consumer.consume_messages, daemon=True)
    pull_consumer_thread.start()

    # Initialize the PushConsumer instance
    push_consumer = PushConsumer(broker, topic, push_group)

    # Start the PushConsumer in a separate thread for continuous message consumption
    push_consumer_thread = threading.Thread(target=push_consumer.start, daemon=True)
    push_consumer_thread.start()

    # Keep the main program running until all threads complete execution
    producer_thread.join()
    pull_consumer_thread.join()
    push_consumer_thread.join()


if __name__ == "__main__":
    main()
