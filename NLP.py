import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import time

#exampleArray = ['The incredibly intimidating NLP scares people away who are sissies.']

contentArray = ['show sales from Delhi']
##let the fun begin!##
def processLanguage():
    try:
        for item in contentArray:
            tokenized = nltk.word_tokenize(item)
            
            stop_words = set(stopwords.words('english'))
            word_tokens = word_tokenize(item)
            filtered_sentence = [w for w in word_tokens if not w in stop_words]
            filtered_sentence = []
            for w in word_tokens:
                if w not in stop_words:
                    filtered_sentence.append(w)

            #print(word_tokens)
            print(filtered_sentence)
            
            tagged = nltk.pos_tag(filtered_sentence)
            print(tagged)
            
            ne_tree = ne_chunk(tagged)
            print(ne_tree)

            iob_tagged = tree2conlltags(ne_tree)
            print (iob_tagged)
            ne_tree = conlltags2tree(iob_tagged)
            print (ne_tree)

            namedEnt = nltk.ne_chunk(tagged)
            namedEnt.draw()
            #break
            #continue
            #time.sleep(1)


 



    except Exception as e:
        print (str(e))


processLanguage()
