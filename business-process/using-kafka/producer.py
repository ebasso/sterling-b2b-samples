import time
import json
import random
import string
from datetime import datetime
from kafka import KafkaProducer

topic = 'sb2b-kfk-inbound'
#topic = 'sb2b-kfk-streams-inbound'
user_ids = list(range(1, 101))
recipient_ids = list(range(1, 101))

def generate_message() -> dict:
    random_user_id = random.choice(user_ids)
    # Copy the recipients array
    recipient_ids_copy = recipient_ids.copy()
    # User can't send message to himself
    recipient_ids_copy.remove(random_user_id)
    random_recipient_id = random.choice(recipient_ids_copy)
    # Generate a random message
    message = ''.join(random.choice(string.ascii_letters) for i in range(32))
    return {
        'user_id': random_user_id,
        'recipient_id': random_recipient_id,
        'message': message
    }


# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['127.0.0.1:29092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    # Infinite loop - runs until you kill the program
    while True:
        # Generate a message
        dummy_message = generate_message()

        # Send it to our 'messages' topic
        print(f'Producing message @ {datetime.now()} | Message = {str(dummy_message)}')

        # To work with Sterling B2B you must setup filename as key
        # The option b is byte
        producer.send(topic, dummy_message, key=b'filename.txt')

        # Sleep for a random number of seconds
        time_to_sleep = random.randint(1, 11)
        time.sleep(time_to_sleep)