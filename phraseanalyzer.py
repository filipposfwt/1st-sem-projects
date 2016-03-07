import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.tag import pos_tag
print ("Please enter two phrases")
phrase1=raw_input("Phrase1:")
phrase2=raw_input("Phrase2:")
p1=wordpunct_tokenize(phrase1)
p2=wordpunct_tokenize(phrase2)
words1=pos_tag(p1)
words2=pos_tag(p2)
print words1,words2
phrase1=[]
phrase2=[]
for i in range(len(words1)):
    if words1[i][1]=='NN':
        phrase1[i]=words[i][0]
print phrase[0]
