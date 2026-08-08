import time
import random
import json
from kafka import KafkaProducer
AIVEN_SERVICE_URI = "kafka-3f3350c0-rohit4-4d8c.j.aivencloud.com:23387"  
KAFKA_TOPIC = "occupancy_data"                                    
USERNAME = "avnadmin"                                             
PASSWORD = "**********"                                  
CA_FILE_PATH = "ca.pem"


producer = KafkaProducer(
    bootstrap_servers=AIVEN_SERVICE_URI,
    security_protocol="SASL_SSL",
    sasl_mechanism="SCRAM-SHA-256",
    sasl_plain_username=USERNAME,
    sasl_plain_password=PASSWORD,
    ssl_cafile=CA_FILE_PATH,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)
class MyApiDriver:
    def __init__(self):
        pass
    def setup(self):
        pass
    def do_poll(self):
        occupancy_values = [0,1,2]
        fake_data = random.choice(occupancy_values)
        payload = {
                "data":fake_data,
                "timestamp": time.time(),
                "sensor_id": "sensor_1"
                }
        future = producer.send(KAFKA_TOPIC,value=payload)
        record_metadata = future.get(timeout=10)
        print(record_metadata)
        print('fake_data', fake_data)
        pass

interval = 5
driver = MyApiDriver()
while True:
    driver.do_poll()
    time.sleep(interval)

