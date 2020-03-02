import pika
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm

# Create your views here.

def index(request):
    #form = PostForm()
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if(form.is_valid()):
            message = form.cleaned_data['message']
            publish_event(message)

    form = PostForm()
    return render(request, 'myapp/home.html', {'form': form})


def publish_event(message):
    send2q1(message)
    send2q2(message)
    print(" [x] Event published { message: \"" + message + "\" }")


def send2q1(message):
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='q1')

    channel.basic_publish(exchange='', routing_key='q1', body=message)
    #print(" [x] Sent " + message)
    connection.close()

def send2q2(message):
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='q2')

    channel.basic_publish(exchange='', routing_key='q2', body=message)
    #print(" [x] Sent " + message)
    connection.close()

def responses(request):
    message1 = str(readMessage())
    message2 = str(readMessage())
    return HttpResponse(message1+"<br/>"+message2)

def readMessage():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='q3')
    method_frame, header_frame, body = channel.basic_get(queue = 'q3') 

    if method_frame != None:       
        if method_frame.NAME == 'Basic.GetEmpty':
            connection.close()
            return ''
        else:            
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
            connection.close() 
            return body.decode("utf-8")
    else:
        return '';
