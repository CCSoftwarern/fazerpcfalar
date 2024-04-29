
import datetime
import pyttsx3

num = int(input("Digite 1 para iniciar, 2 para encerrar: "))

while num == 1 :
    texto = input("Digite o texto para a fala: ")
    voz = int(input("Digite 0 para Português e 1 para Inglês 0: "))
    horario = datetime.datetime.now()
    ver_horario = horario.strftime("%m_%d_%Y_%H_%M_%S")
    juntar = ver_horario+".mp3"
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('age', 25)
    engine.setProperty('rate', 180)
    engine.setProperty('voice', voices[voz].id)
    engine.say(texto)
    engine.save_to_file(texto, juntar)
    engine.runAndWait()
    print("Arquivo gerado: ",juntar)
print("Programa terminado")