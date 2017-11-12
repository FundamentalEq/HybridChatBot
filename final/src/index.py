import json
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

from globalValues import *

stopWords = set(stopwords.words('english'))

dialogues = []
index = {}
with open("../data/parsed.txt") as f :
    i = 0
    ps = PorterStemmer()

    for line in f :
        dialogues.append(line)

        line = line.replace(othername,'')
        line = line.replace(selfname,'')

        line = word_tokenize(line)

        for word in line :
            word = ps.stem(word)
            if word not in stopWords :
                # this is word we would like to index
                if word not in index : index[word] = {}
                if i not in index[word] : index[word][i] = 0
                index[word][i] += 1

        i += 1
        print(i)

# dump the dialogues as json dump
d = open("../data/dialogues.txt","w")
d.write(json.dumps(dialogues))
d.close()

# dump the invertedindex as json dump
invertedindex = open("../data/invertedindex.txt","w")
invertedindex.write(json.dumps(index))
invertedindex.close()
