import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import csv
import argparse


parser = argparse.ArgumentParser(description='Train Dev and Test set Splitting')
parser.add_argument('--metadata', type=str, required=True)
parser.add_argument('--train_split', type=float, default=0.9)
args = parser.parse_args()

source = args.metadata


df = pd.read_csv(source, delimiter='\t', header=None, quoting=csv.QUOTE_NONE)
df.columns = ['file_name', 'spk_id', 'transcription']
df = shuffle(df)


train, middle = train_test_split(df, test_size=(1 - args.train_split))
val, test = train_test_split(middle, test_size=0.5)

train.to_csv('./temp/train.txt', sep = '\t', index = False, header = False)
val.to_csv('./temp/val.txt', sep = '\t', index = False, header = False)
test.to_csv('./temp/test.txt', sep = '\t', index = False, header = False)