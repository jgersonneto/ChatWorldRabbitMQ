from Client_RPC import RabbitMQClient
from Publisher import RabbitMQPublisher

class ChatWorld:
    def __init__(self) -> None:
        self.client_rpc = RabbitMQClient()
        self.consumer_topic = RabbitMQPublisher()
    
    def Start(self):

        print("Bem Vindo ao ChatWorld")
        nome = input("Digite seu nome: \n\n")
        sala = input("Digite a sala que deseja conversar OU \n\t digite ""show_room"" para saber quais salas tem: \n\n")

        message = "show_room"        
        response = self.client_rpc.start(message)
        
        sala1, sala2 = response.split(';')
        while sala == 'show_room':
            print(f'Total de salas: 2 \n\t {sala1} \n\t {sala2}')
            sala = input("Digite a sala que deseja conversar OU \n\t digite ""show_room"" para saber quais salas tem: \n\n")
        sendMessage = True
        print(f"sala:  {sala}")

        while sendMessage:
            message = input(f"Digite a mensagem para sala {sala} OU \n\t digite ""sair"" para fechar o app: \n\n")
            
            message = f"{nome} - digitou {message}"
            self.consumer_topic.create_publish(message, sala)

            if message == f"{nome} - digitou sair":
                sendMessage = False
                self.consumer_topic.close_connection()
            



chatWorld = ChatWorld()
chatWorld.Start()