import pika, sys, os

class RabbitMQServer:
    def __init__(self) -> None:
        self.__host = 'localhost'
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "rpc_queue"
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

        channel.queue_declare(
            queue=self.__queue
            )       

        return channel

    

    def on_request(self, ch, method, props, body):
        
        message = str(body, 'utf-8')

        if message == "show_room":
            message = "chatworld.sala.novela;chatworld.sala.anime"
        
        ch.basic_publish(
            exchange="",
            routing_key=props.reply_to,
            properties=pika.BasicProperties(
                correlation_id = props.correlation_id
            ),
            body=message
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def consume(self):
        self.__channel.basic_qos(
            prefetch_count=1
            )
        self.__channel.basic_consume(
            queue=self.__queue, 
            on_message_callback=self.on_request
            )
        print(" [x] Awaiting RPC requests")
        self.__channel.start_consuming()

if __name__ == '__main__':
    try:
        rabbitmq_server = RabbitMQServer()
        rabbitmq_server.consume()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)