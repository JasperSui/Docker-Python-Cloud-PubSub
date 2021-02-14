import os, time, json, random, datetime
from google.cloud import pubsub_v1
from google.api_core.exceptions import AlreadyExists
project_id = os.environ.get('GCP_PROJECT_ID') # Google Project Id
topic_id = "channel" # Topic Id
topic_path = f"projects/{project_id}/topics/{topic_id}"
publisher = pubsub_v1.PublisherClient()
msg_list = [{"type":"show_channel_info", "id": 22},
            {"type":"show_channel_info", "id": 23},
            {"type":"show_channel_info", "id": 52}]

# 新建一個 Topic
try:
    publisher.create_topic(name=topic_path)
except AlreadyExists:
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
          f" [WARNING] Topic \"{topic_id}\" already exists.")

# 定時每 5 秒 Publish 一個隨機 message 到 channel 這個 Topic
while 1:
    message = json.dumps(random.choice(msg_list)).encode()
    publisher.publish(topic_path, message)
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} [Info] message sent, message: {message}")
    time.sleep(5)