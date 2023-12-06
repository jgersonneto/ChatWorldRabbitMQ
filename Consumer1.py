import pika, sys, os
from Storage import StorageMessage
import random

class RabbitMQConsumer:
    def __init__(self, callback) -> None:
        self.__host = 'localhost'
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = ""
        self.__queue_name = ""
        self.__queue_result = None
        self.__exchange = "topic_logs"
        self.__exchange_type = "topic"
        self.__callback = callback
        self.__channel = self.__create_channel()
        self.__count = 0

    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        connection = pika.BlockingConnection(connection_parameters)
        channel = connection.channel()

        self.__queue_result = channel.queue_declare(
            queue=self.__queue,
            #durable=True,
            exclusive=True
        )

        #channel.basic_qos(prefetch_count= 1 )
        self.__create_exchange(channel)

        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=self.__callback
        ) 
        

        return channel
    
    def __create_exchange(self, channel):
        self.__queue_name = self.__queue_result.method.queue
        channel.exchange_declare(exchange= self.__exchange , exchange_type= self.__exchange_type ) 
        listSeverity = ["chatworld.sala.*"]
        for severity in listSeverity:
            channel.queue_bind(exchange=self.__exchange, queue=self.__queue_name, routing_key=severity)

    def start(self):
        print(f'Listen RabbitMQ on port 5672')
        self.__channel.start_consuming()

def CallBackMessage(ch, method, properties, body):
    body_str = str(body, 'utf-8')
    message = f"{method.routing_key}: {body_str}"
    print(f"{message}")
    dictionary = dict()
    key, value = message.split(':')
    valor_aleatorio = random.randint(0, 1000)
    key = key + str(valor_aleatorio)
    dictionary[key] = value
    storage_message = StorageMessage()
    storage_message.Write(dictionary)
    #ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    try:
       rabbitmq_consumer = RabbitMQConsumer(CallBackMessage)
       rabbitmq_consumer.start()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)