{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Speech to SQL\n",
    "\n",
    "## Table of Contents\n",
    "-[Project Description](#project-description)\n",
    "-[Process](#process)\n",
    "-[Installations](#installations)\n",
    "-[Use of codes](# codes)\n",
    "\n",
    "\n",
    "### <a name=\"project-description\"></a>Project Description\n",
    "Convert speech to sql statements using NLP and python.\n",
    "The project has different approaches.\n",
    "We are trying to implement the paper attached in this repository.\n",
    "We want to convert speech to sql statements and based on these statements we should be able to retrieve data from the databases.\n",
    "I am unable to complete the last phase where i have to convert NER to sql.\n",
    "\n",
    "### <a name=\"process\"></a>Process\n",
    "The following are the steps to be followed:\n",
    "1) Recognize speech.\n",
    "2) Convert speech to text.\n",
    "3) Tokenize.\n",
    "4) Remove stop words.\n",
    "5) Part of Speech tagging(POS).\n",
    "6) Named entity recognition(NER).\n",
    "7) Join the phases to form sql statement.\n",
    "\n",
    "\n",
    "### <a name=\"installations\"></a>Installations\n",
    "The following packages need to be installed\n",
    "1) NLTK\n",
    "2) SPEECH RECOGNITION\n",
    "3) Python3\n",
    "\n",
    "\n",
    "### <a name=\"codes\"></a>Use of codes\n",
    "\n",
    "The codes are simple to execute.\n",
    "1) The code for speech recognition is provided in `Speech2Text.py`\n",
    "2) For removing stop words `stpwrds.py`\n",
    "3) For NER in `NER.py`\n",
    "4) A code to convert nl to sql is in `last.py`\n",
    "4) A single code for Tokenizating,removing stop words,POS,Chunking and NER is in the file `NLP.py`\n",
    "5) Full combined code from speech recognition to NER is in `newall.py`"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
