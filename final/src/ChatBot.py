import sys
import re
import json
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import response
import string
import globalValues
class ChatBot(object):
    def __init__(self,search_object):
        self.username = 'username' # name of user we are currently talking too
        self.selfname = 'iris' # name of IR Bot
        self.vocabulary = {} # dictionary for storing new vocabulary other than we have
        self.history_count={} # dictionary for storing count of top words in history
        self.history_dialogue=[] # queue for history dialogues keeping maximum 50 diaglogues
        self.index = {} # dictionary for storing index
        self.dialogue = {} # dictionary for storing each dialogue in list of strings
        self.load_index() # load index into the memory
        self.load_dialogue() # load dialogue into the memory
        self.search_object=search_object # storing object to call get Response function
        self.ps = PorterStemmer()
        self.stopWords = set(stopwords.words('english'))
    def load_index(self):
        self.index = json.loads(open("../data/invertedindex.txt").read())
        print("Inverted-Index loaded successfully")

    def load_dialogue(self):
        self.dialogue = json.loads(open("../data/dialogues.txt").read())
        print("Dialogues loaded successfully")

    def pp(self,who):
        if who==0:
            print 'IRIS: ',
        elif who==1:
            print self.username+': ',
    def initialise(self):
        self.pp(0)
        print "Hello I'm IRIS... What's your name?"
        self.pp(1)
        a=raw_input()
        a=a.translate(None, string.punctuation)
        a=a.split();
        self.username=a[len(a)-1].lower()
        self.pp(0)
        print 'Hey '+self.username+' what do you wanna talk about ?'
    def vocabulary_handler(self,new_word):
        self.pp(0)
        print "Sorry user didn't got what you meant by "+new_word
        self.pp(1)
        a=raw_input()
        a=a.lower()
        a=a.translate(None, string.punctuation)
        a=a.split()
        self.vocabulary[new_word]=a
    def main(self,userinput,mode):
        while 1:
            if mode==1:
                self.pp(1)
            flago = False
            if mode==2:
                a=userinput
            else:
                a=raw_input()
            a=a.translate(None, string.punctuation)
            a=a.lower()
            if mode==1:
                if a=="ttyl":
                    break
            #a=a.replace(self.username,globalValues.selfname)
            #a=a.replace(self.selfname,globalValues.othername)
            a=a.replace(self.username,'')
            a=a.replace(self.selfname,'')
            a=a.split()
            if mode==2:
                if len(a)<4:
                    flago = True
            self.history_dialogue.insert(0,a)
            if mode==1:
                for i in a:
                    if i not in self.stopWords:
                        j = self.ps.stem(i)
                        if j not in self.index and i not in self.vocabulary:
                            #print i
                            self.vocabulary_handler(i)

                for j in a:
                    #print j.type
                    if type(j)!=type(a):
                        if j not in self.stopWords:
                            if i in self.vocabulary:
                                for k in self.vocabulary[i]:
                                    a.append(k)

            b=a
            cou=0
            for key in sorted(self.history_count,key=self.history_count.get,reverse=True):
                if self.history_count[key]>1:
                    if key not in b:
                        b.append(key)
                cou+=1
                if cou==3:
                    break
            #print b
            dgn=search_object.getResponse(b,mode)
            resp=self.dialogue[int(dgn)+1]
            resp=resp.replace(globalValues.selfname,self.selfname)
            resp=resp.replace(globalValues.othername,self.username)
            if mode==1:
                self.pp(0)
                print resp
            for i in a:
                if i not in self.history_count:
                    self.history_count[i] = 1
                else:
                    self.history_count[i] += 1
            if len(self.history_dialogue)==3:
                last_dialogue = self.history_dialogue.pop()
                for i in last_dialogue:
                        self.history_count[i] -= 1
            if mode==2:
                if flago is not True:
                    return resp
                else:
                    return '---$---'
if __name__ =='__main__':
    search_object = response.Response()
    IRIS = ChatBot(search_object)
    IRIS.initialise()
    IRIS.main("did you change your hair",1)
    del search_object
    del IRIS
    #print "yahoo"
