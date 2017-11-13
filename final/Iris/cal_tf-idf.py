#Pre - calculate tf-idf vectors for each document
import json
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from math import log10
from globalValues import *

stopWords = set(stopwords.words('english'))

# Load index
print "Loading Index......."
invertedIndex = json.loads(open("../data/invertedindex.txt").read())
print "Index loaded"

# Load dialogues
print "Loading dialogues......"
dialogues = json.loads(open("../data/dialogues.txt").read())
print "Dialogues loaded"

def get_tf_idf_vec(dialogueId, dial):
    """
    Using invertedIndex return
    tf-idf vector for given document
    """
    vector = {}
    for word in dial :
        tf = 1 + log10(float(invertedIndex[word][dialogueId]))
        idf = log10(float(totaldialogues)/float(len(invertedIndex[word])))
        vector[word] = tf*idf
    return vector

# Compute tf-idf vectors
print "Computing tf-idf"
ps = PorterStemmer()

Tf_idf_vectors = []

for i in range(len(dialogues)) :
    line = dialogues[i]
    line = line.replace(othername,'')
    line = line.replace(selfname,'')

    line = word_tokenize(line)
    dial = {}
    for word in line :
        word = ps.stem(word)
        if word not in stopWords :
            # this is word we would like to index
            dial[word] = True
    Tf_idf_vectors.append(get_tf_idf_vec(str(i),dial))
    print(i)

# Write to file
print "Dumping to file"
ff = open("../data/tf_idf_vectors.txt", "w")
ff.write(json.dumps(Tf_idf_vectors))
ff.close()
