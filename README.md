# Prototipo_Evento
Repositorio para el prototipo basado en eventos

## Requisitos
Instancia de RabbitMQ, para desarrollo se utilizó un container:

docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

## Arquitectura
<b>UI Service:</b> interfaz envia mensajes al broker<br/>
<b>Broker:</b> cola de en RabbitMQ<br/>
<b>Char Count Service:</b> cuenta los caracteres que tiene el mensaje<br/>
<b>Word Count Service:</b> cuenta las palabras que tiene el mensaje<br/>
