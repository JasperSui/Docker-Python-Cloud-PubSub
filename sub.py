import os, uuid, time, json, random, datetime
from google.cloud import pubsub_v1
from google.api_core.exceptions import AlreadyExists

CHANNEL_MAP = {
    22: "Cartoon",
    23: "YoYo TV",
    52: "News"
}

project_id = os.environ.get('GCP_PROJECT_ID') # Google Project Id
topic_id = "channel" # Topic Id
topic_path = f"projects/{project_id}/topics/{topic_id}"
container_name = os.environ.get('HOSTNAME')
sub = f"sub-{container_name}-{uuid.uuid4().hex}"
sub_path = f"projects/{project_id}/subscriptions/{sub}"
subscriber = pubsub_v1.SubscriberClient()

# 新建一個 Subscription
try:
    subscriber.create_subscription(name=sub_path, topic=topic_path)
except AlreadyExists:
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
          f' [WARNING] Subscription already exists, sub_path: {sub_path}')

def callback(message):
    data = json.loads(message.data.decode())
    if type := data.get('type'):
        if type == 'show_channel_info':
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                  f" [INFO] Message received, the channel is {CHANNEL_MAP.get(data.get('id'))}")
    message.ack()

future = subscriber.subscribe(sub_path, callback)