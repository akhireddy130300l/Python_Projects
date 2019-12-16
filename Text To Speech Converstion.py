from gtts import gTTS
import os
f=open("Speech.txt")
x=f.read()
language='en'
audio=gTTS(text=x,lang=language,slow=False)
audio.save("Speech.wav")
os.system("Speech.wav")
