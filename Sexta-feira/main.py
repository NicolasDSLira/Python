__autor__ = "Nicolas dos Santos Lira"


#modulos padrão python

import datetime

#importando funções

from ouvir import *

from falar import falar

from comandos import executar_comando



########################################################

exit_oriana = False


#inicialização (Apresentação)
def inicializacao():
    horario = int(datetime.datetime.now().hour)

    if horario >=0 and horario < 12:
        falar("Bom dia!")

    elif horario >= 12 and horario <18:
        falar("Boa tarde!")

    else:
        falar("Boa noite!")

    falar("Estou em segundo, diga o comando no microfone que executarei o mesmo.")



if __name__ == "__main__":
    inicializacao()
    while not exit_oriana:
        comando = ouvir().lower()
        executar_comando(comando)
    exit_oriana = True