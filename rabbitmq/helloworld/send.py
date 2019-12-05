#!/usr/bin/python
#coding:utf-8

import pika
import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

body = 'Hello World!' + " " +str(datetime.datetime.now())
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=body)
print(" [x] Sent 'Hello World!'")

connection.close()