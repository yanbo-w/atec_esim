# -*- coding: utf-8 -*-
import os
import sys
import codecs

open_file = sys.argv[1]
save_file = sys.argv[2]
print(open_file)
print(save_file)

raw_samples = []
with codecs.open(open_file, 'r', encoding='utf-8') as f:
  for line in f:
    line = line.strip()
    lines = line.split('\t')
    raw_samples.append(lines[1:])

import jieba

token_sample = []

words_table = {}

with codecs.open('vocab.txt', 'r', encoding='utf-8') as f:
  for line in f:
    line = line.strip()
    words_table[line] = len(words_table)

# jieba.suggest_freq('花呗', True)
jieba.load_userdict('my_dict.txt')
# jieba.add_word('花呗','借呗','蚂蚁花呗','蚂蚁借呗')

for sample in raw_samples:
  # print('-------------')
  token_list1 = []
  token_list2 = []
  raw_list1 = jieba.lcut(sample[0], cut_all=False, HMM=False)
  raw_list2 = jieba.lcut(sample[1], cut_all=False, HMM=False)
  for word in raw_list1:
    if word not in words_table.keys():
        token_list1.append(0)
    else:
        token_list1.append(words_table[word])
  # print('%%%%%')
  for word in raw_list2:
    # print(word)
    if word not in words_table.keys():
            token_list2.append(0)
    else:
        token_list2.append(words_table[word])
  token_sample.append([token_list1, token_list2])



from tensorflow import keras

import numpy as np
data1 = []
data2 = []

for sample in token_sample:
  input1 = np.zeros(32)
  input2 = np.zeros(32)
  if len(sample[0]) > 32:
    input1 = sample[0][:32]
  else:
    input1[:len(sample[0])] = sample[0]
  if len(sample[1]) > 32:
    input2 = sample[1][:32]
  else:
    input2[:len(sample[1])] = sample[1]
  data1.append(input1)
  data2.append(input2)

data1 = np.array(data1)
data2 = np.array(data2)

model = keras.models.load_model('atec_model.h5')

dev_predict_value = model.predict([data1, data2])

dev_predict_label = []
for i in dev_predict_value:
  if i >0.5:
    dev_predict_label.append(1)
  else:
    dev_predict_label.append(0)

with open(save_file, 'wb') as f:
    for (line_num, label) in enumerate(dev_predict_label):
        f.write('%d\t%d\n' % (line_num+1, label))

