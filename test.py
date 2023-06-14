import os
from tqdm import tqdm


files = os.listdir('dataset/audio_files')

with open('trash/asr_bengali/utt_spk_text.tsv', 'r') as f:
    lines = f.readlines()

for line in tqdm(lines):
    data = line.split('\t')
    filename = data[0]
    spk_id = data[1]
    utt = data[2]

    if filename + '.flac' in files:
        with open('./dataset/metadata.tsv', 'a') as f:
            f.write(f"{filename}\t{spk_id}\t{utt}")