# kafka_consumer_mahi.py

from kafka import KafkaConsumer
import os
from dotenv import load_dotenv
from utils.utils_logger import logger

load_dotenv()

def main():
    logger.info("START patient check-in consumer...")
    
    # Kafka bootstrap server (from .env or default localhost)
    kafka_bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    
    # Kafka topic to consume from (should match your producer topic)
    kafka_topic = os.getenv("KAFKA_TOPIC", "patient_checkin_topic")
    
    # Create a Kafka consumer
    consumer = KafkaConsumer(
        kafka_topic,
        bootstrap_servers=[kafka_bootstrap_servers],
        auto_offset_reset='earliest',  # start reading at earliest message
        group_id='patient_checkin_group',
        enable_auto_commit=True,
        value_deserializer=lambda x: x.decode('utf-8')
    )
    
    try:
        for message in consumer:
            # message.value contains the string sent by producer
            logger.info(f"Received message: {message.value}")
    except KeyboardInterrupt:
        logger.info("Consumer stopped by user.")
    finally:
        consumer.close()
        logger.info("END patient check-in consumer.")

if __name__ == "__main__":
    main()