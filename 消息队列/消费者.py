#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()


channel.queue_declare(queue='hello')
def callback(ch,method,properties,body):
    print("-->",ch,method,properties)
    print("[x] Received %r" %body)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack = True)

print('[*] waiting fro messages. to exit press CTRL+C')
channel.start_consuming()