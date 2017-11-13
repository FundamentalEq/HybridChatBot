import json
import numpy as np
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from math import log10
from globalValues import *


class Response(object):

    def __init__(self):
        self.stopWords = set(stopwords.words('english'))
        self.PS = PorterStemmer()

        # Load tf-idf vectors
        print "Loading Tf-idf vectors"
        self.Tf_idf_vectors = json.loads(open("../data/tf_idf_vectors.txt").read())
        self.invertedIndex = json.loads(open("../data/invertedindex.txt").read())
        print "Tf-idf vectors loaded"

    def get_query_vec(self,query):
        """
        Return tf-idf vector
        for our query
        """
        parsedQuery = []
        for word in query:
            word = self.PS.stem(word)
            if word not in self.stopWords:
                parsedQuery.append(word)

        Cnt = {}
        for word in parsedQuery:
            Cnt[word] = Cnt.get(word, 0.0) + 1.0

        query_vec = {}
        for word in parsedQuery:
            query_vec[word] = 1 + log10(Cnt[word])
        return query_vec

    def cosine_sim(self,vecA, vecB):
        """
        Return cosine similarity
        score between vecA and vecB
        """
        union = list(set().union(vecA.keys(), vecB.keys()))
        A = []
        for word in union :
            if word in vecA :
                A.append(vecA[word])
            else : A.append(0)

        B = []
        for word in union :
            if word in vecB :
                B.append(vecB[word])
            else : B.append(0)

        dot_product = np.dot(A, B)
        norm_a = np.linalg.norm(A)
        norm_b = np.linalg.norm(B)
        return dot_product / (norm_a * norm_b)

    def getResponse(self,tokens,mode):
        """
        Given a tokenised dialog
        return next dialog
        """
        res, maxScore = -1, -1
        query_vec = self.get_query_vec(tokens)

        candidates = {}
        for word in query_vec :
            if word not in self.invertedIndex :
                continue
            for dialogId in self.invertedIndex[word] :
                candidates[dialogId] = True
        for dialogId in candidates :
            score = self.cosine_sim(query_vec, self.Tf_idf_vectors[int(dialogId)])
            if score > maxScore:
                maxScore = score
                res = dialogId
        if mode==2:
            if maxScore>0.90:
                return res
            else:
                return '---$---'
        else:
            return res
