import os

try:
    import pyttsx3
except:
    os.system("pip install pyttsx3")
    import pyttsx3




#função de falar

def falar(audio):

    maquina = pyttsx3.init()

    voices = maquina.getProperty("voices")

    maquina.setProperty("voice", voices[0].id)

    maquina.setProperty("rate", 200)

    maquina.say(audio)

    maquina.runAndWait()