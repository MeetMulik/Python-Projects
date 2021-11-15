from gtts import gTTS
import os


file = open('speech.txt')
text = file.read()
language = 'en'


audio = gTTS(text=text, lang=language, slow=False)

audio.save("audio.wav")
os.system("audio.wav")
