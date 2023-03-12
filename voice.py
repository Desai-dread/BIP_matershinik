import pyttsx3		#pip install pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 130)				#скорость речи

tts = pyttsx3.init()

voices = tts.getProperty('voices')


# Попробовать установить предпочтительный голос
for voice in voices:
    if voice.name == 'Artemiy':
        tts.setProperty('voice', voice.id)

def speaker(text):
	'''Озвучка текста'''
	engine.say(text)
	engine.runAndWait()