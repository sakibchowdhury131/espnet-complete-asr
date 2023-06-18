import pandas as pd
import os
import csv
import random
import argparse


parser = argparse.ArgumentParser(description='Generate SCP')
parser.add_argument('--kaldi_destination', type=str, default='./dataset/KALDI_FILES')
parser.add_argument('--audio_source', type=str, default='./dataset/audio_files')
args = parser.parse_args()

source = './temp/train.txt'
destination_dir = os.path.join(args.kaldi_destination, 'train')
audio_dir = args.audio_source

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
destination_dir = os.path.join(args.kaldi_destination, 'val')
audio_dir = args.audio_source

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
destination_dir = os.path.join(args.kaldi_destination, 'test')
audio_dir = args.audio_source

df = pd.read_csv(source, delimiter='\t', header=None, quoting=csv.QUOTE_NONE)
df.columns = ['file_name', 'spk_id', 'transcription']

df.sort_values(['file_name', 'spk_id'], axis=0, ascending=[True, True], inplace=True, ignore_index=True, na_position='first')


if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
f= open(destination_dir + "/wav.scp","w")

for i in range (len(df)):
    f.write(df['file_name'][i]+' '+audio_dir + '/'+df['file_name'][i]+'.'+file_extension +'\n')
f.close()