import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import csv

source = './dataset/metadata.tsv'


df = pd.read_csv(source, delimiter='\t', header=None, quoting=csv.QUOTE_NONE)
df.columns = ['file_name', 'spk_id', 'transcription']
df = shuffle(df)


train, middle = train_test_split(df, test_size=0.1)
val, test = train_test_split(middle, test_size=0.5)

train.to_csv('./temp/train.txt', sep = '\t', index = False, header = False)
val.to_csv('./temp/val.txt', sep = '\t', index = False, header = False)
test.to_csv('./temp/test.txt', sep = '\t', index = False, header = False)