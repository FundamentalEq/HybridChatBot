from globalValues import *
import string
characters = {}
mylines = []
with open("../data/cornell_movie-dialogs_corpus/movie_lines.txt","r") as f :
    for line in f :
        temp = line
        line = line.split("+++$+++")

        # extract number
        lineId = int(line[0].strip().lower()[1:])
        mylines.append((lineId,temp))

        # extract movieId
        movieId = line[2].strip().lower()
        if movieId not in characters : characters[movieId] = {}

        # extract characters
        character = line[3].strip().lower()
        if(len(character) > 0) : characters[movieId][character] = True

mylines = sorted(mylines)

f2 = open("../data/parsed.txt","w")
buf = []
for line in mylines :
    line = line[1]
    line = line.split("+++$+++")

    # extract movieId
    movieId = line[2].strip().lower()

    # extract characters
    character = line[3].strip().lower()

    # extract utterance
    utterance = line[4].strip().lower()
    utterance = filter(lambda x: x in string.printable, utterance)
    utterance = utterance.replace(character,selfname)

    # check for othername
    for othercharacter in characters[movieId] :
        if othercharacter != character :
            utterance = utterance.replace(othercharacter,othername)

    buf.append(utterance)
    if len(buf) > 2e6 :
        f2.write(seprator.join(buf))
        buf = []


if len(buf) > 0 : f2.write(seprator.join(buf))
f2.close()
