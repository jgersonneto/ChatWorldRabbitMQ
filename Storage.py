import json
import os

class StorageMessage:
        
    def Write(self, dictionary):

        nome_arquivo = 'C:\\arquivo.json'
        os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)
        dados_exits = self.GetData()
        dados_exits.update(dictionary)
        # Escrever em um arquivo
        with open(nome_arquivo, 'w') as f:
            json.dump(dados_exits, f, indent=2)

        self.Read()


    def Read(self):       

        nome_arquivo = 'C:\\arquivo.json'
        try:
            if os.path.isfile(nome_arquivo):
                # Tentar ler o dicionário do arquivo
                with open(nome_arquivo, 'r') as f:
                    dados_lidos = json.load(f)
                
                print(f"Dados do arquivo: {dados_lidos}")
            else:
                print(f"O arquivo '{nome_arquivo}' não existe.")            

        except json.JSONDecodeError as e:
            # Se ocorrer um erro, o JSON é inválido
            print(f"Erro ao carregar dados do arquivo JSON: {e}")

        return dados_lidos
    
    def GetData(self): 
        nome_arquivo = 'C:\\arquivo.json'
        try:
            if os.path.isfile(nome_arquivo):
                # Tentar ler o dicionário do arquivo
                with open(nome_arquivo, 'r') as f:
                    dados_lidos = json.load(f)
                    return dados_lidos
                
            else:
                return dict()
                        
        except json.JSONDecodeError as e:
            # Se ocorrer um erro, o JSON é inválido
            print(f"Erro ao carregar dados do arquivo JSON: {e}")

        
