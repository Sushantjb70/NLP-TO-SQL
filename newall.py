import nltk
import speech_recognition as sr
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import time


def recordAudio():
    recording = sr.Recognizer()  # initialize recognizer


    with sr.Microphone() as source:  #recording.adjust_for_ambient_noise(source)
        print("Say something:")

        audio = recording.listen(source) # listen to the source
    #text = ""
    
    try:
        text = recording.recognize_google(audio) # use recognizer to convert our audio into text part.
        inpu = text #.lower()
        content = print("You said:" + inpu)
        
    #print("You said: \n" + recording.recognize_google(audio))
#except Exception as e:
#    print(e)


    
       

    
# exampleArray = ['The incredibly intimidating NLP scares people away who are sissies.']

        contentArray = [inpu]


##let the fun begin!##
        #def processLanguage():
        try:
            for item in contentArray:
                #tokenized = nltk.word_tokenize(item)
                #print(tokenized)

                stop_words = set(stopwords.words('english'))
                word_tokens = word_tokenize(item)
                filtered_sentence = [w for w in word_tokens if not w in stop_words]
                filtered_sentence = []
                for w in word_tokens:
                    if w not in stop_words:
                        filtered_sentence.append(w)
                print(word_tokens)
                print(filtered_sentence)


                tagged = nltk.pos_tag(filtered_sentence)
                print(tagged)

                #entities = nltk.chunk.ne_chunk(tagged)
                #print(entities)

                ne_tree = ne_chunk(pos_tag(word_tokenize(inpu)))
                print(ne_tree)

                iob_tagged = tree2conlltags(ne_tree)
                print(iob_tagged)
                ne_tree = conlltags2tree(iob_tagged)
                print(ne_tree)

                #namedEnt = nltk.ne_chunk(tagged)
                ne_tree.draw()
            # break
            # continue
            # time.sleep(1)

        except Exception as e:
            print(str(e))


        #processLanguage()

    except sr.UnknownValueError:
            print("Could not understand audio")


    except sr.RequestError as e:
        print("Could not request results: {0}".format(e))
    #return text
time.sleep(2)
#speak("say something")
while 1:
    text = recordAudio()

