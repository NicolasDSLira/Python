from tkinter import *
from tkinter import ttk


#Declarando classe
class Calculadora:

    def __init__(self, root):

        #Iniciando variáveis globais da classe
        self.primeiro_numero = StringVar()
        self.segundo_numero = StringVar()
        self.operacao = StringVar()
        self.resultado = StringVar()

        #Definindo título da página
        root.title("Calculadora")

        #Declarando style
        s = ttk.Style()

        #configurando estilo da tela
        s.configure('Tela.TFrame', background='grey11', foreground='white')

        #configurando estilo da label resultado
        s.configure('Resultdo.TLabel', background='grey11', foreground='white')

        #Declarando o frame tela
        tela = ttk.Frame(root, width=100, height=500, style='Tela.TFrame', padding=10)
        tela.grid(column=0, row=0, sticky=(N, W, E, S))

        #Declarando o frame corpo
        corpo = ttk.Frame(root, padding="20")
        corpo.grid(column=0, row=1, sticky=(N, W, E, S))

        #Configurando grid
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)   
       
        #Declarando textos da página
        ttk.Label(tela, textvariable=self.resultado, style='Resultdo.TLabel').grid(column=4, row=0, sticky=W)

        ttk.Label(corpo, text="Primeiro número: ", padding=10).grid(column=1, row=1)
        
        ttk.Label(corpo, text="Segundo número: ", padding=10).grid(column=1, row=3)
        
        #Declarando RadioButtons
        som = ttk.Radiobutton(corpo, text='Somar', variable=self.operacao, value=1)
        som.grid(column=1, row=2, sticky=(N, W, E, S))

        sub = ttk.Radiobutton(corpo, text='Subtrair', variable=self.operacao, value=2)
        sub.grid(column=2, row=2, sticky=(N, W, E, S))

        mult = ttk.Radiobutton(corpo, text='Multiplicar', variable=self.operacao, value=3)
        mult.grid(column=3, row=2, sticky=(N, W, E, S))

        div = ttk.Radiobutton(corpo, text='Dividir', variable=self.operacao, value=4)
        div.grid(column=4, row=2, sticky=(N, W, E, S))


        #Declarando Inputs
        primeira_entrada = ttk.Entry(corpo, width=20, textvariable=self.primeiro_numero)
        primeira_entrada.grid(column=2, row=1, sticky=(W, E))

        segunda_entrada = ttk.Entry(corpo, width=20, textvariable=self.segundo_numero)
        segunda_entrada.grid(column=2, row=3)

        #Declarando botton
        ttk.Button(corpo, text="Calcular", command=self.calcular).grid(column=4, row=4 , sticky=W)

    
        for child in tela.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        #Dando focu na primeira input
        primeira_entrada.focus()

        #Quando clicar no botão, retorna a função calcular
        root.bind("<Return>", self.calcular)
        
    #Declarando função calcular
    def calcular(self, *args):

        try:
            #Atribuindo variável local com valores do formulário, e convertendo os mesmos
            primeiro_valor = float(self.primeiro_numero.get())

            segundo_valor = float(self.segundo_numero.get())

            value_operacao = int(self.operacao.get())

            #Realizando condições com base nas escolhas de operação
            if value_operacao == 1:
                self.resultado.set(primeiro_valor + segundo_valor)

            elif value_operacao == 2:
                self.resultado.set(primeiro_valor - segundo_valor)

            elif value_operacao == 3:
                self.resultado.set(primeiro_valor * segundo_valor)

            elif value_operacao == 4:
                self.resultado.set(primeiro_valor / segundo_valor)

        except ValueError:
            pass

#Iniciando tela
root = Tk()

#Chamando classe
Calculadora(root)

#Deixando a tela em loop
root.mainloop()