import os
import datetime
import subprocess

#Compreender audio
try: 
    import speech_recognition as sr
except:
    os.system("pip install SpeechRecognition")
    import speech_recognition as sr

#pegar audio
try:
    import pyaudio
except:
    os.system("pip install pyaudio")
    import pyaudio


# funçõa para ouvir e reconhecer fala
def ouvir():

    os.system("cls")

    #habilita microfone
    microfone = sr.Recognizer()

    #usando microfone
    with sr.Microphone() as source:

        #chama um algoritmo de redução de ruido
        microfone.adjust_for_ambient_noise(source)

        #frase inicial
        print("Ouvindo microfone ..\n")

        #pausa entre as falas
        microfone.pause_threshold = 1

        microfone.dynamic_energy_threshold = 500

        #armazena o que foi dito em uma variável
        audio = microfone.listen(source)
        
        try:
            # Comando ouvido
            print("Processando comando ...\n")

            #passa a variável para o algoritmo reconhecedor dos padrões
            comando = microfone.recognize_google(audio, language='pt-BR')

        #Se não reconhecer o padrão da fala.
        except sr.UnknownValueError:
            print("Comando não entendido!")
            return "None"

        return comando