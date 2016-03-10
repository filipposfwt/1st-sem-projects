#Libraries.
import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn
import nltk.corpus as corpus
import itertools as IT
print ("Please enter two phrases")

phrase1=raw_input("Phrase1:")
phrase2=raw_input("Phrase2:")
#Splitting phrases in words and symbols.
p1=wordpunct_tokenize(phrase1)
p2=wordpunct_tokenize(phrase2)
#Part of speech tagging of the words.
words1=pos_tag(p1)
words2=pos_tag(p2)
set1=[]
set2=[]
#Keeping nouns,verbs and adjectives of each phrase.
for i in range(len(words1)):
    if (words1[i][1]=='NN' or words1[i][1]=='NNS' or  words1[i][1]=='NNP' or words1[i][1]=='NNP' or  words1[i][1]=='NNPS'
     or words1[i][1]=="VB" or  words1[i][1]=='VBD' or  words1[i][1]=='VBG' or  words1[i][1]=='VBN' or  words1[i][1]=='VBP' or  words1[i][1]=='VBZ'
      or words1[i][1]=="JJ" or  words1[i][1]=='JJR' or  words1[i][1]=='JJS'):
        set1.append(words1[i][0])
for i in range(len(words2)):
    if (words2[i][1]=='NN' or words2[i][1]=='NNS' or  words2[i][1]=='NNP' or words2[i][1]=='NNP' or  words2[i][1]=='NNPS'
     or words2[i][1]=="VB" or  words2[i][1]=='VBD' or  words2[i][1]=='VBG' or  words2[i][1]=='VBN' or  words2[i][1]=='VBP' or  words2[i][1]=='VBZ'
      or words2[i][1]=="JJ" or  words2[i][1]=='JJR' or  words2[i][1]=='JJS'):
        set2.append(words2[i][0])
#Finding how close these two phrases are depending on the overall score.Score range is from none to 1.0
for word1, word2 in IT.product(set1, set2):
    wordFromList1 = wn.synsets(word1)[0]
    wordFromList2 = wn.synsets(word2)[0]
    w1 = wordFromList1.name
    w2 = wordFromList2.name
    s = wordFromList1.path_similarity(wordFromList2)
    print '(',word1,',',word2,')','Similarity:',s
