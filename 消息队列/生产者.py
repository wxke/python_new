#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import pika

connect = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connect.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='Hello world'
)

print(" [x] Sent 'Hello World'")

connect.close()