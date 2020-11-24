import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0))],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0))],
            [sg.Button('Enviar Dados')]
        ]
        # Janela
        Janela = sg.Window("Dados do Usuário").layout(layout)
        
        # Extrair
        self.button, self.values = Janela.read()
        
    def Iniciar(self):
        print(self.values)
        
tela = TelaPython()
tela.Iniciar()