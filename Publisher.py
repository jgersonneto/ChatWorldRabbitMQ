import pika
import random

class RabbitMQPublisher:
    def __init__(self) -> None:
        self.__host = 'localhost'
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__routingkey = ""
        self.__exchange = "topic_logs"
        self.__exchange_type = "topic"
        #self.__delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
        self.__connection = None
        self.__channel = self.__create_channel()
        self.__create_exchange()

    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        self.__connection = pika.BlockingConnection(connection_parameters)
        channel = self.__connection.channel()

        return channel
    
    def __create_exchange(self):
        self.__channel.exchange_declare(exchange= self.__exchange , exchange_type= self.__exchange_type )

    def create_publish(self, message, sala):
        
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=sala,
            body=message,
            #properties=pika.BasicProperties(
            #    delivery_mode=self.__delivery_mode
            #)
        )
        print("mensagem enviada")
        
    def close_connection(self):
        self.__connection.close()