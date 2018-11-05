from nltk import word_tokenize, pos_tag, ne_chunk

sentence = "show sales for Sandiego"

print(ne_chunk(pos_tag(word_tokenize(sentence))))
"""
(S
  (PERSON Mark/NNP)
  and/CC
  (PERSON John/NNP)
  are/VBP
  working/VBG
  at/IN
  (ORGANIZATION Google/NNP)
  ./.)
"""
