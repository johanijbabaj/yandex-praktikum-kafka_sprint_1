import logging
import os
import random

from kafka import KafkaProducer
from modules.order_generator import Order
from time import sleep

logger = logging.getLogger("Producer")


class Producer:
    def __init__(self, broker, topic):
        self.producer = KafkaProducer(
            bootstrap_servers=broker,
            acks='all',  # Waiting the confirmation from all nodes
            retries=5,
            linger_ms=10,
            batch_size=1024,
        )
        self.topic = topic

    def produce_messages(self, count=100):
        try:
            for i in range(count):
                order = Order()
                message = order.to_json()
                logger.info(f"Produced: {message}")
                self.producer.send(self.topic, message.encode('utf-8'))
                sleep(random.uniform(0, 2))
        except Exception as e:
            logger.error(f"Error producing message: {e}", exc_info=True)
        finally:
            self.producer.close()


if __name__ == "__main__":
    # Testing Producer
    logger = logging.getLogger("Producer")
    producer = Producer("localhost:9094", "my-topic")
    producer.produce_messages()
