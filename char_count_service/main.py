#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='q2')


def callback(ch, method, properties, body):
    message_recieved = body.decode("utf-8")
    print(" [x] Event detected { message: \""+message_recieved+"\" }")
    char_count = str(len(str(message_recieved)))
    #channel.close()

    message = "{message:\""+message_recieved+"\", char_count:"+char_count+"}"
    #print(message)

    # reply with other event
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='q3')

    channel.basic_publish(exchange='', routing_key='q3', body=message)
    print(" [x] Event published " + message)
    connection.close()

channel.basic_consume(
    queue='q2', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
