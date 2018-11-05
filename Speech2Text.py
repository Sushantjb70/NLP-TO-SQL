import speech_recognition as sr
import time

def recordAudio():
    recording = sr.Recognizer()  # initialize recognizer


    with sr.Microphone() as source:  #recording.adjust_for_ambient_noise(source)
        print("Say something:")

        audio = recording.listen(source) # listen to the source
    #text = ""
    
    try:
        text = recording.recognize_google(audio) # use recognizer to convert our audio into text part.
        content = print("You said:" + text.lower())
        
    #print("You said: \n" + recording.recognize_google(audio))
#except Exception as e:
#    print(e)


    except sr.UnknownValueError:
        print("Could not understand audio")


    except sr.RequestError as e:
        print("Could not request results: {0}".format(e))
    #return text
       
time.sleep(2)
#speak("say something")
while 1:
    text = recordAudio()
