## Welcome to HybridBot

You can download it from this [link](https://github.com/FundamentalEq/Seq2seqchatBot). It is an hybrid of two types of bot, First one is IRIS ChatBot and Second one is Seq2Seq chatbot.


### Usage

Follow following steps to use it:    
Setting up IRIS ChatBot  
Download [Cornell Dataset](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html) and rename it to cornell_movie-dialogs_corpus than just run
```python
  bash prepare.sh
```
Setting up Seq2Seq ChatBot  
Download dependencies which are just Python 2.7 and Pytorch 0.12 than run two command one after another  
```python
  python preprocess.py
```
This script will create file `dialogue_corpus.txt` in `./data` directory.
```python
  python train.py
```
The hyperparameters of model are defined in configuration file `config.json`.You can change according to your need.  
In my local environment(GTX1060), training model need about four hours.  

To Run final bot
```python
  python finalBot.py
```

## Reference
- [PyTorch documentation](http://pytorch.org/docs/0.1.12/)
- [seq2seq-translation](https://github.com/spro/practical-pytorch/tree/master/seq2seq-translation)
- [tensorflow_chatbot](https://github.com/llSourcell/tensorflow_chatbot)
- [Cornell Movie Dialogs Corpus](https://github.com/suriyadeepan/datasets/tree/master/seq2seq/cornell_movie_corpus)
- [Blog about seq2seq](http://suriyadeepan.github.io/2016-06-28-easy-seq2seq/)
- [IRIS paper](https://www.semanticscholar.org/paper/IRIS-a-Chat-oriented-Dialogue-System-based-on-the-Banchs-Li/9528fa09fbd918618dbd1bac72fe8c24f5574400)
- [Seq2Seq paper](https://arxiv.org/pdf/1506.05869.pdf)
