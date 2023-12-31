import os
from tqdm import tqdm
import random


def rename(AUDIO_SOURCE = './dataset/audio_files',  
           METADATA = './dataset/metadata.tsv'):
    
    TEMP_DIR = './temp'
    print(f'Renaming files in ----> {AUDIO_SOURCE}')
    possible_formats = ['mp3', 'm4a', 'flac', 'wav']
    # fileExtension = random.choice(os.listdir(AUDIO_SOURCE)).split('.')[-1]
    with open(METADATA, 'r') as f:
        lines = f.readlines()

    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)
    for line in tqdm(lines):
        utt_id = line.split('\t')[0]
        spk_id = line.split('\t')[1]
        utt = line.split('\t')[2]
        fileExtension = None
        for format in possible_formats:
            current_filename = f'{AUDIO_SOURCE}/{utt_id}.{format}'
            if os.path.exists(current_filename):
                fileExtension = format
                break
            
        new_filename = f'{AUDIO_SOURCE}/{spk_id}-{utt_id}.{fileExtension}'
        os.rename(current_filename, new_filename)

        with open(f'{TEMP_DIR}/metadata.tsv', 'a') as f:
            f.write(f"{spk_id}-{utt_id}\t{spk_id}\t{utt}")
        
    
    ## replace the old metadata file
    with open(f'{TEMP_DIR}/metadata.tsv', 'r') as f:
        text = f.read()
    with open(METADATA, 'w') as f:
        f.write(text)