import speech_recognition as sr
import os
while True:
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("just to check...")
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            print(text)
            if(text=="stop"):
                break
            else:
                if text=="open youtube":
                    os.startfile('Speech.bat')
                    print(" ")
        except:
            print(" ")
