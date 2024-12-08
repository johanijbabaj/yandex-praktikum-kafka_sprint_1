# Kafka Producer and Consumer Project

## Overview
This project demonstrates the implementation of Kafka producers and consumers for processing order data. It includes error handling, logging, and configurable message count for producers and consumers.

## Classes

### 1. Order
A class responsible for generating random order data. Each order includes fields such as `id`, `number`, `date`, `status`, `items`, `charges`, and more. Converts data to JSON format for Kafka.

### 2. Producer
Handles message production and sending data to Kafka topics. Key responsibilities:
- Connects to a Kafka cluster.
- Serializes messages (orders) to JSON format.
- Sends messages to a specified Kafka topic with retry logic and error handling.

### 3. PushConsumer
A Kafka consumer class designed to continuously poll messages from a specified topic. Key features:
- Subscribes to a Kafka topic and processes messages in real time.
- Includes automatic offset management to ensure message processing consistency.
- Logs each consumed message and handles errors gracefully.

### 4. PullConsumer
Another Kafka consumer class that fetches messages manually in batches. Key features:
- Provides more control over when and how messages are fetched.
- Allows batch processing for performance optimization.
- Includes logging and error handling for robust processing.

## How to Run the Project

### Prerequisites
1. Start Kafka Services: Use the provided docker-compose.yml file to start a Kafka cluster:
   ```bash 
    docker-compose up -d
   ```
2. Install required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Steps to Run
1. Start Kafka and create the necessary topic using:
   ```bash
   docker exec -it kafka-0 /opt/bitnami/kafka/bin/kafka-topics.sh --create --topic my-topic --partitions 3 --replication-factor 2 --bootstrap-server kafka-0:9092
   ```

2. Verify the topic creation:
   ```bash
   docker exec -it kafka-0 /opt/bitnami/kafka/bin/kafka-topics.sh --list --bootstrap-server kafka-0:9092
   ```

3. Run the producer script to send messages and proceeding it:
   ```bash
   python3 main.py
   ```

### Testing the Project
1. Verify that messages are being produced:
   - Check logs in the producer script for confirmation.

2. Consume messages:
   - Run one of the consumer scripts and observe the processed messages in the logs.

3. Alternatively, use the Kafka console consumer to check messages:
   ```bash
    docker exec -it kafka-0 /opt/bitnami/kafka/bin/kafka-console-consumer.sh \
    --topic my-topic \
    --bootstrap-server kafka-0:9092 \
    --from-beginning
   ```

## How It Works

### Producer Workflow
- **Message Production**: The producer generates an `Order` object, serializes it into JSON, and sends it to Kafka.
- **Logging**: All operations are logged for monitoring and debugging.

### PushConsumer Workflow
- Subscribes to a Kafka topic and polls messages continuously.
- Processes each message as it is received.
- Automatically commits offsets to ensure message consistency.
- Logs consumed messages for verification.

### PullConsumer Workflow
- Manually fetches messages from a Kafka topic in batches.
- Allows processing of messages in groups for optimized performance.
- Handles errors and logs each batch for transparency with manual commit.

## Additional Notes
- Ensure Kafka is running locally or accessible.
- Use `topic.txt` for Kafka topic creation and description commands.

