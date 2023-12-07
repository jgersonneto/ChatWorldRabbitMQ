# Chat com RabbitMQ


  Bem-vindo ao nosso sistema de chat baseado em Python, que utiliza RabbitMQ para comunicação assíncrona, RPC para gerenciamento de salas e Tópicos para direcionamento eficiente de mensagens. Este readme fornecerá insights sobre o projeto e orientará você na configuração e utilização do sistema.

### Visão Geral

  Desenvolvemos este sistema de chat para proporcionar uma solução escalável e eficiente para salas de chat em Python, aproveitando o poder do RabbitMQ para comunicação assíncrona, RPC para gerenciamento de salas e Tópicos para direcionamento seletivo de mensagens.

### Configuração

Desenvolvemos este sistema de chat para proporcionar uma solução escalável e eficiente para salas de chat em Python, aproveitando o poder do RabbitMQ para comunicação assíncrona, RPC para gerenciamento de salas e Tópicos para direcionamento seletivo de mensagens.


#### -----> No Terminal <---------

###### Primeiro passo - rodar o servidor RPC

~~~python 
python Server_RPC.py
~~~

###### Segundo passo - rodar o servidor Tópico

~~~python 
python Consumer1.py
~~~


###### Terceiro passo - rodar o ChatWorld

~~~python 
python ChatWorld.py
~~~


###### A partir daí seguir os passos do chat


