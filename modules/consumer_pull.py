import logging
from kafka import KafkaConsumer

logger = logging.getLogger("PullConsumer")

class PullConsumer:
    def __init__(self, broker, topic, group_id):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=broker,
            group_id=group_id,
            auto_offset_reset="earliest"
        )

    def consume_messages(self):
        try:
            for message in self.consumer:
                logger.info(f"Pull-consumer received: {message.value.decode('utf-8')}")
        except Exception as e:
            logger.error(f"Pull consumer error: {e}")
        finally:
            self.consumer.close()