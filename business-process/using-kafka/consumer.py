import json
from kafka import KafkaConsumer

if __name__ == '__main__':
    # Kafka Consumer
    consumer = KafkaConsumer(
        'sfg-kfk-outbound',
        bootstrap_servers='127.0.0.1:29092',
        auto_offset_reset='latest'
    )
    for message in consumer:
        print(json.loads(message.value))
