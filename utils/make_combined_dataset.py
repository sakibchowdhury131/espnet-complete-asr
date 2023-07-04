import os
import shutil
from tqdm import tqdm

OPENSLR = './openslr53-bn'
COMMON_VOICE = './common_voice/cv-corpus-11.0-2022-09-21/bn/prepared_dataset'
BANKING = './banking-domain-dataset'
DATASETS = [OPENSLR, COMMON_VOICE, BANKING]


FULL_DATASET = './complete_dataset'
audio_dst = os.path.join(FULL_DATASET, 'audio_files')
metadata_dst = os.path.join(FULL_DATASET, 'metadata.tsv')

if not os.path.exists(audio_dst):
    os.makedirs(audio_dst)

### copy openslr
for dataset in DATASETS:
    print(f'processing {dataset}')
    files = os.listdir(os.path.join(dataset, 'audio_files'))
    for file in tqdm(files):
        src = os.path.join(dataset, 'audio_files', file)
        shutil.copy(src, audio_dst)
    with open(os.path.join(dataset, 'metadata.tsv'), 'r') as f:
        text = f.read()
    
    with open(metadata_dst, 'a') as f:
        f.write(text)