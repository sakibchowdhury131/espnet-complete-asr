import pandas as pd
import os
import csv
import argparse


parser = argparse.ArgumentParser(description='Generate Text')
parser.add_argument('--kaldi_destination', type=str, default='./dataset/KALDI_FILES')
args = parser.parse_args()

source = './temp/train.txt'
destination_dir = os.path.join(args.kaldi_destination, 'train')

df = pd.read_csv(source, delimiter='\t', header=None, quoting=csv.QUOTE_NONE)
df.columns = ['file_name', 'spk_id', 'transcription']
df.sort_values(['file_name', 'spk_id'], axis=0, ascending=[True, True], inplace=True, ignore_index=True, na_position='first')


if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
f= open(destination_dir + "/text","w")

for i in range (len(df)):
    f.write(df['file_name'][i]+' '+df['transcription'][i]+'\n')
f.close()



source = './temp/val.txt'
destination_dir = os.path.join(args.kaldi_destination, 'val')

df = pd.read_csv(source, delimiter='\t', header=None, quoting=csv.QUOTE_NONE)
df.columns = ['file_name', 'spk_id', 'transcription']
df.sort_values(['file_name', 'spk_id'], axis=0, ascending=[True, True], inplace=True, ignore_index=True, na_position='first')


if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
f= open(destination_dir + "/text","w")

for i in range (len(df)):
    f.write(df['file_name'][i]+' '+df['transcription'][i]+'\n')
f.close()


source = './temp/test.txt'
destination_dir = os.path.join(args.kaldi_destination, 'test')

df = pd.read_csv(source, delimiter='\t', header=None, quoting=csv.QUOTE_NONE)
df.columns = ['file_name', 'spk_id', 'transcription']
df.sort_values(['file_name', 'spk_id'], axis=0, ascending=[True, True], inplace=True, ignore_index=True, na_position='first')


if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
f= open(destination_dir + "/text","w")

for i in range (len(df)):
    f.write(df['file_name'][i]+' '+df['transcription'][i]+'\n')
f.close()
