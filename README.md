## About This Project

It's a simple project that demos Google Cloud Pub/Sub service with Docker and Python.

The only publisher will send a message that includes channel information to the topic every 5 seconds.
And the rest of the subscribers will receive it and print the result.

## Getting Started

```sh
docker-compose up -d
```

## Demo

The left-hand tab is publisher, the middle one is subscriber 1, the right-hand tab is subscriber 2.

![img](https://i.imgur.com/xwz7gQX.gif)

## Reference

[用 Python + Docker 實作簡易 Cloud Pub/Sub Service](https://jaspersui.github.io/2021/02/14/python-cloud-pubsub/)