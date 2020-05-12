import nltk
from nltk.tokenize import sent_tokenize,word_tokenize

doc1=open("doc1.txt","r")
text1=doc1.readlines()
doc2=open("doc2.txt","r")
text2=doc2.readlines()

# convert list to strings
str1=''.join(text1)
str2=''.join(text2)

# old method for getting each sentence
sent_text1_old=str1.split('.')
sent_text2_old=str2.split('.')

# nltk smart method of getting the sentences
sentences_text1 = sent_tokenize(str1)
sentences_text2 = sent_tokenize(str2)


def checkMatching(text1,text2):
    matching_sentences=[]
    for x in text1:
        for y in text2:
            if x == y:
                matching_sentences.append(x)
    return matching_sentences

old_text_matching = checkMatching(sent_text1_old,sent_text2_old)

nltk_text_matching = checkMatching(sentences_text1,sentences_text2)

print("Matched text old sentence splitting: ")
print(old_text_matching)
print("--------------------------------")
print("Matched text nltk sentence splitting: ")
print(nltk_text_matching)
print("!!!!!! done !!!!!!")
