import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
# word tokenizing
data = "Mars is approximately half the diameter of Earth."
print(word_tokenize(data))

# sentence tokenizing
data = "Mars is a cold desert world. It is half the size of Earth. "
print(sent_tokenize(data))

######## doc operations #####
print("------ doc operations -------")
file_docs = []

with open ('doc1.txt') as f:
    tokens = sent_tokenize(f.read())
    for line in tokens:
        file_docs.append(line)

print("Number of documents:",len(file_docs))

gen_docs = [[w.lower() for w in word_tokenize(text)] 
            for text in file_docs]

print(gen_docs)

################################

import gensim
import numpy as np

print("------ corpora -------")
dictionary = gensim.corpora.Dictionary(gen_docs)
print(dictionary.token2id)

# corpus is the collection of words (documents)
# get the words in the sentences and their usage frequency
print("------ corpus -------")
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


print("------ Term frequency -------")
# words that occur more frequently
# removes the ones that occur more freq
tf_idf = gensim.models.TfidfModel(corpus)
for doc in tf_idf[corpus]:
    print([[dictionary[id], np.around(freq, decimals=2)] for id, freq in doc])

print("------ Similarity -------")
 # similarity checkup
sims = gensim.similarities.Similarity('work/',tf_idf[corpus],
                                        num_features=len(dictionary))

file2_docs = []

with open ('doc1.txt') as f:
    tokens = sent_tokenize(f.read())
    for line in tokens:
        file2_docs.append(line)

print("Number of documents:",len(file2_docs))  
for line in file2_docs:
    query_doc = [w.lower() for w in word_tokenize(line)]
    query_doc_bow = dictionary.doc2bow(query_doc) #update an existing dictionary and create bag of words

# perform a similarity query against the corpus
query_doc_tf_idf = tf_idf[query_doc_bow]
# print(document_number, document_similarity)
print('Comparing Result:', sims[query_doc_tf_idf]) 


sum_of_sims =(np.sum(sims[query_doc_tf_idf], dtype=np.float32))
print(sum_of_sims)
percentage_of_similarity = round(float((sum_of_sims / len(file_docs)) * 100))
print(f'Average similarity float: {float(sum_of_sims / len(file_docs))}')
print(f'Average similarity percentage: {float(sum_of_sims / len(file_docs)) * 100}')
print(f'Average similarity rounded percentage: {percentage_of_similarity}')

