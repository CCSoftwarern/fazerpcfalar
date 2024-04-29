# Obtenha a lista de vozes disponíveis e selecione uma
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")
for voice in voices:
    print(voice.id)