import os
import subprocess

try:
    import pyautogui as pa
except:
    os.system("pip install pyautogui")
    import pyautogui as pa


from Noticias import noticias

from falar import *
import webbrowser

from ouvir import ouvir

#Função que executa os comandos

def executar_comando(C):

    #Falar notícias - ok
    if C == "notícias":
        noticias()

    #Abrir notepad - ok
    elif C == "abrir notepad":
        falar("Abrindo notepad.")
        subprocess.call("notepad.exe")

    # Abrir excel - ok
    elif C == "abrir excel":
        falar("Abrindo Excel 2007.")
        os.system("start excel")

    #Abrir calculadora
    elif C == "abrir calculadora":
        falar("Abrindo calculadora.")
        subprocess.call("calc.exe")
        
    #Abrir spotify - ok
    elif C == "abrir spotify":
        falar("Abrindo Spotify.")
        subprocess.call("spotify.exe")
        
    #Abrir navegador - ok
    elif C == "abrir navegador":
        falar("Abrindo Navegador.")
        os.system("start opera") #coloca o nome do seu navegador

    # Precisa estar na path
    elif C == "abrir discord":
        falar("Abrindo Discord.")
        subprocess.call("discord.exe")

    #abrir youtube OK
    elif C == "abrir youtube":
        falar("Acessando Youtube.")
        webbrowser.open("https://www.youtube.com/")

    #Acessar github - ok
    elif C == "abrir github":
        falar("Acessando Github.")
        webbrowser.open("https://github.com/")

    #Acessar netflix
    elif C == "abrir Netflix" and C == "Abrir Netflix":
        falar("Acessando Netflix")
        webbrowser.open("https://www.netflix.com/")

    # ok
    elif C == "repita comigo":
        falar("Diga algo:")
        repetir = ouvir()
        falar(repetir)

    #modificadores de volume
    
    ##pegar posições com arquivo posicao.py

    elif C == "volume máximo":
        pa.click(1192, 748)
        pa.click(1301, 701)

    elif C == "mudo":
        pa.click(1192, 748)
        pa.click(1073,701)

    elif C == "volume básico":
        pa.click(1192, 748)
        pa.click(1186, 700)

    elif C == "wifi":
        pa.click(1170, 744)
        pa.click(1036, 700)


    #desligar computador -
    elif C == "desligar computador":
        os.system("shutdown -s")


    #Desligar programa - ok
    elif C == "desligar":
        exit_oriana = True
        exit()

    else:
        os.system("cls")
        