import pika
import uuid

class RabbitMQClient:
    def __init__(self):
        self.__host = 'localhost'
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue_name = ""
        self.__corr_id = None
        self.__response = None
        self.__connection = None
        self.__channel = self.__create_channel()

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

        result = channel.queue_declare(
            queue="",
            exclusive=True
        )
        self.__queue_name = result.method.queue

        channel.basic_consume(
            queue=self.__queue_name,
            on_message_callback=self.callBackMessage,
            auto_ack=True
        )

        return channel

    def callBackMessage(self, ch, method, props, body):
        if self.__corr_id == props.correlation_id:
            self.__response = body
        
    def start(self, message):
        self.__response = None
        self.__corr_id = str(uuid.uuid4())
        self.__channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.__queue_name,
                correlation_id=self.__corr_id
            ),
            body=message)
        self.__connection.process_data_events(time_limit=None)
        return str(self.__response, 'utf-8')