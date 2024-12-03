import os
import logging
from kafka import KafkaProducer
from time import sleep

logger = logging.getLogger("Producer")


class Producer:
    def __init__(self, broker, topic):
        self.producer = KafkaProducer(bootstrap_servers=broker)
        self.topic = topic

    def produce_messages(self, count=10):
        try:
            for i in range(count):
                message = f"Message {i}"
                self.producer.send(self.topic, message.encode("utf-8"))
                logger.info(f"Produced: {message}")
                sleep(1)
        except Exception as e:
            logger.error(f"Producer error: {e}")
        finally:
            self.producer.close()
