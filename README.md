# Chat com RabbitMQ


Bem-vindo ao nosso sistema de chat baseado em Python, que utiliza RabbitMQ para comunicação assíncrona, RPC para gerenciamento de salas e Tópicos para direcionamento eficiente de mensagens. Este readme fornecerá insights sobre o projeto e orientará você na configuração e utilização do sistema.

### Visão Geral

Desenvolvemos este sistema de chat para proporcionar uma solução escalável e eficiente para salas de chat em Python, aproveitando o poder do RabbitMQ para comunicação assíncrona, RPC para gerenciamento de salas e Tópicos para direcionamento seletivo de mensagens.

### Configuração

#### Pré-requisitos:

* Certifique-se de ter o RabbitMQ instalado e em execução.
* Instale as dependências do projeto com **pip install**

#### Inicialização do Sistema:

Execute o **servidor RPC** do chat no Terminal com:
~~~python 
python Server_RPC.py
~~~

Execute o **servidor TÓPICO** do chat no Terminal com:
~~~python 
python Consumer1.py
~~~

Execute o **ChatWorld** para começa chat no Terminal com:
~~~python 
python ChatWorld.py
~~~

**A partir daí seguir os passos do chat**

### Como Funciona

RPC para Gerenciamento de Salas
*Listar Salas: Utilize chamadas RPC para obter a lista de salas disponíveis.

Tópicos para Direcionamento de Mensagens
*Cada sala está associada a um Tópico exclusivo.
*As mensagens são direcionadas às salas apropriadas usando Tópicos.

### Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas, propor melhorias ou enviar pull requests.
