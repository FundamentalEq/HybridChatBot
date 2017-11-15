# coding=utf8
import json
import random
import torch
import torch.nn as nn
from torch.autograd import Variable
from model_utils import load_vocabulary, build_model, BotAgent
from Iris.ChatBot import IRIS

with open('config.json') as config_file:
    config = json.load(config_file)

BOT_NAME = config['TEST']['BOT_NAME']
ckpt_epoch = config['TEST']['CKPT_EPOCH']

def main():
    vocab = load_vocabulary()
    model = build_model(len(vocab.word2index), load_ckpt=True, ckpt_epoch=ckpt_epoch)
    bot = BotAgent(model, vocab)
 #   IRIS.initialise()
    while True:
        user_input = raw_input('me: ')
        if user_input.strip() == '':
            continue
        Iris_resp = IRIS.main(user_input, 2)
        if Iris_resp != '---$---' and len(Iris_resp.split()) <= 10  :
            print('%s: %s' % ("Iris", Iris_resp))
        else:
            print('%s: %s' % ("Seq", bot.response(user_input)))

if __name__ == '__main__':
    main()
