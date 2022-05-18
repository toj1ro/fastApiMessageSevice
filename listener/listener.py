import time

from kafka import KafkaConsumer
import requests


def listener():
    consumer = KafkaConsumer('messages', bootstrap_servers='broker:9092',
                             auto_offset_reset='earliest', group_id='consumer_group')
    for msg in consumer:
        message = msg.value.decode('utf-8')
        if 'govno' in message.lower():
            r = requests.post('http://web:8000/api/v1/message_confirmation',
                              json={"message_id": msg.key.decode('utf-8'), "success": False})
            print(r.json())
        else:
            r = requests.post('http://web:8000/api/v1/message_confirmation',
                              json={"message_id": msg.key.decode('utf-8'), "success": True})
            print(r.json())


if __name__ == '__main__':
    while True:
        try:
            listener()
        except:
            time.sleep(5)
            print('error')
