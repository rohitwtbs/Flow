import json
import os
import logging
from kafka import KafkaConsumer

# 1. Logging Setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# 2. Configuration (Matches your Aiven setup)
AIVEN_SERVICE_URI = "kafka-3f3350c0-rohit4-4d8c.j.aivencloud.com:23387"
KAFKA_TOPIC = "occupancy_data"
USERNAME = "avnadmin"
PASSWORD = "**************"
CA_FILE_PATH = os.path.abspath("ca.pem")


GROUP_ID = "occupancy-consumer-group-1"

logging.info("Connecting consumer to Aiven Kafka...")

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=AIVEN_SERVICE_URI,
    security_protocol="SASL_SSL",
    sasl_mechanism="SCRAM-SHA-256",
    sasl_plain_username=USERNAME,
    sasl_plain_password=PASSWORD,
    ssl_cafile=CA_FILE_PATH,
    api_version=(2, 5, 0),
    group_id=GROUP_ID,
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
)

logging.info(f"Consumer started! Waiting for messages on topic '{KAFKA_TOPIC}'...")


try:
    for message in consumer:
        data = message.value
        
        logging.info(
            f"Received -> Sensor: {data.get('sensor_id')} | "
            f"Occupancy: {data.get('data')} | "
            f"Partition: {message.partition} | Offset: {message.offset}"
        )
except KeyboardInterrupt:
    logging.info("Consumer stopped by user.")
finally:
    consumer.close()
    logging.info("Consumer connection closed.")
