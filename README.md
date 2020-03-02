# Prototipo_Evento
Repositorio para el prototipo basado en eventos

## Requisitos
Instancia de RabbitMQ, para desarrollo se utilizó un container:

docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

## Arquitectura
UI Service: interfaz envia mensajes al broker
Broker: cola de en RabbitMQ
Char Count Service: cuenta los caracteres que tiene el mensaje
Word Count Service: cuenta las palabras que tiene el mensaje
