from abc import ABC, abstractmethod
import PySimpleGUI as sg #cria a interface grafica 
# Projeto criado pelo Paulo Victor e Brenda Garcia 

#Classe abstrata que define o metodo abstrato 
class Portaria (ABC):
    @abstractmethod
    def entrar(self, nome):
        pass

#São subclasses 
class Aluno(Portaria):
    def entrar(self, nome):
        return f" {nome} tem relação com a instituição Fatec como Aluno "
    
class Professor (Portaria):
        def entrar (self, nome):
            return f"{nome} tem relação com a instituição Fatec como Professor"
        
class Coordenador (Portaria):
        def entrar (self, nome):
            return f"{nome} tem relaçãoa com a instituição Fatec como Coordenador"
        
class Diretor (Portaria):
        def entrar (self, nome):
            return f"{nome} tem relação com a instituição Fatec como Diretor"
        
class Administrativo (Portaria):
        def entrar (self, nome):
            return f"{nome} tem relação com a instituição Fatec como Administrador "
        
        
#Class factory method 
class Portariarelaçao:
        def criar_usuario(self, tipo_pessoa,nome):
            if tipo_pessoa== "Aluno":
                return Aluno()
            elif tipo_pessoa == "Professor":
                return Professor()
            elif tipo_pessoa == "Coordenador" :
                 return Coordenador()
            elif tipo_pessoa == "Diretor":
                return Diretor()
            elif tipo_pessoa == "Administrativo" :
                return Administrativo()
            else:
               sg.Popup(f"{nome} não tem relação com a instituição Fatec") # Exibe mensagem na interface#caso nao tenha nenhua dessas opções esta sera a mensagem a vim ser

sg.theme('Reddit') #tema

layout = [[sg.Text('Digite seu nome:'), sg.InputText(size=(20,1)),],
          [sg.Text('Digite a relação: '), sg.InputText(size=(20,1))],
          [sg.Button('Verificar'), sg.Button('Cancelar')]] # Botão para Verificar a entrada e Botão para cancelar a operação

window = sg.Window('Tela de Login portaria', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break
    if event == 'Verificar': #Ele verifica se o usuário clicou no botão 'verifica' na interface gráfica.
        nome = values[0] #obtém o valor digitado no primeiro campo de entrada, que foi nomeado como "Digite seu nome" no layout, e atribui esse valor à variável 
        relacao = values[1] # faz o mesmo para o segundo campo de entrada, que foi nomeado como "Digite a relação" no layout, atribuindo o valor digitado à variável relacao.
        pessoa = Portariarelaçao().criar_usuario(relacao, nome) #Cria uma instância da classe Portariarelação para obter uma instância da classe específica baseada na relação inserida
        sg.Popup(pessoa.entrar(nome)) # Exibe o resultado em uma janela de diálogo (popup) usando a função sg.Popup

window.close()