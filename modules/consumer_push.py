import logging
from kafka import KafkaConsumer
from threading import Thread, Event

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("PushConsumer")


class PushConsumer:
    def __init__(self, broker, topic, group_id):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=broker,
            group_id=group_id,
            auto_offset_reset="earliest",
            enable_auto_commit=True,  # Autocommit ON
            auto_commit_interval_ms=5000 # Interval 5 sec
        )
        self.stop_event = Event()

    def start(self):
        thread = Thread(target=self._consume)
        thread.start()
        return thread

    def _consume(self):
        while not self.stop_event.is_set():
            messages = self.consumer.poll(timeout_ms=100)
            for topic_partition, records in messages.items():
                for record in records:
                    logger.info(f"Push-consumer received: {record.value.decode('utf-8')}")

    def stop(self):
        self.stop_event.set()
        self.consumer.close()
