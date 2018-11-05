# Speech to SQL


## Table of Contents
- Project Description
- Process
- Installations
- Use of codes
- Problem


### Project Description
Convert speech to sql statements using NLP and python.
The project has different approaches.
We are trying to implement the paper attached in this repository.
We want to convert speech to sql statements and based on these statements we should be able to retrieve data from the databases.
I am unable to complete the last phase where i have to convert NER to sql.


### Process
The following are the steps to be followed:
1) Recognize speech.
2) Convert speech to text.
3) Tokenize.
4) Remove stop words.
5) Part of Speech tagging(POS).
6) Named entity recognition(NER).
7) Join the phases to form sql statement.
 

### Installations
The following packages need to be installed
1) NLTK
2) SPEECH RECOGNITION
3) Python3
    

### Use of codes
    
The codes are simple to execute.
1) The code for speech recognition is provided in `Speech2Text.py`
2) For removing stop words `stpwrds.py`
3) For NER in `NER.py`
4) A code to convert nl to sql is in `last.py`
5) A single code for Tokenizating,removing stop words,POS,Chunking and NER is in the file `NLP.py`
6) Full combined code from speech recognition to NER is in `newall.py`"


### Problem
The problem arises to generate grammar for sentences.
We do no know what the user might say so we need to be able to generate grammar for that sentences automatically by parsing.
We can manually do fit for a few sentences as done in `last.py`