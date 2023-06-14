'''
This file checks if all the audios mentioned in the METADATA are present in the AUDIO_SOURCE folder
'''

import os
from tqdm import tqdm


def dataIntegrityChecker(AUDIO_SOURCE = './dataset/audio_files',  METADATA = './dataset/metadata.tsv'):
    OK = True
    dataset_integrity = OK

    files = os.listdir(AUDIO_SOURCE)
    with open (METADATA, 'r') as f:
        lines = f.readlines()

    for line in tqdm(lines):
        filename = line.split('\t')[0]
        spk_id = line.split('\t')[1]
        utt = line.split('\t')[2]

        if not filename+'.flac' in files:
            print(f'Filename: {filename} || Speaker ID: {spk_id} || Utterance: {utt} ---> audio file missing')
            dataset_integrity = not OK
    
    return dataset_integrity