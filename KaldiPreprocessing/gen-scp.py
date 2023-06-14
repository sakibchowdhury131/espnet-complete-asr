import pandas as pd
import os
import csv
import random

source = './temp/train.txt'
destination_dir = './dataset/KALDI_FILES/train'
audio_dir = './dataset/audio_files'

file_extension = random.choice(os.listdir(audio_dir)).split('.')[-1]

df = pd.read_csv(source, delimiter='\t', header=None, quoting=csv.QUOTE_NONE)
df.columns = ['file_name', 'spk_id', 'transcription']

df.sort_values(['file_name', 'spk_id'], axis=0, ascending=[True, True], inplace=True, ignore_index=True, na_position='first')


if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
f= open(destination_dir + "/wav.scp","w")

for i in range (len(df)):
    f.write(df['file_name'][i]+' '+audio_dir + '/'+df['file_name'][i]+'.'+file_extension +'\n')
f.close()




source = './temp/val.txt'
destination_dir = './dataset/KALDI_FILES/val'
audio_dir = './dataset/audio_files'

df = pd.read_csv(source, delimiter='\t', header=None, quoting=csv.QUOTE_NONE)
df.columns = ['file_name', 'spk_id', 'transcription']

df.sort_values(['file_name', 'spk_id'], axis=0, ascending=[True, True], inplace=True, ignore_index=True, na_position='first')


if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
f= open(destination_dir + "/wav.scp","w")

for i in range (len(df)):
    f.write(df['file_name'][i]+' '+audio_dir + '/'+df['file_name'][i]+'.'+file_extension +'\n')
f.close()



source = './temp/test.txt'
destination_dir = './dataset/KALDI_FILES/test'
audio_dir = './dataset/audio_files'

df = pd.read_csv(source, delimiter='\t', header=None, quoting=csv.QUOTE_NONE)
df.columns = ['file_name', 'spk_id', 'transcription']

df.sort_values(['file_name', 'spk_id'], axis=0, ascending=[True, True], inplace=True, ignore_index=True, na_position='first')


if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
f= open(destination_dir + "/wav.scp","w")

for i in range (len(df)):
    f.write(df['file_name'][i]+' '+audio_dir + '/'+df['file_name'][i]+'.'+file_extension +'\n')
f.close()