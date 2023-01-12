import os 

class sexta:
    def __init__(self, comando: str):
        self.comando = comando

    def executar_Comando(self):
        if "Abrir Opera" in self.comando:
            os.system("start Opera.exe")
        
        if "Abrir Excel" in self.comando:
            os.system("start Excel.exe")

        if "Abrir cmd" in self.comando:
            os.system("start cmd.exe") 