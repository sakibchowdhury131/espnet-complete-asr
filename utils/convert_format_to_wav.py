import os
from tqdm import tqdm
from pydub import AudioSegment
import argparse


parser = argparse.ArgumentParser(description='Convert any audio file to wav format')
parser.add_argument('--audio_source', type=str, default='./dataset/audio_files')
args = parser.parse_args()

m4a_files = os.listdir(args.audio_source)
totalFiles = len(m4a_files)

if not os.path.exists('./temp/wavs_out'):
    os.makedirs('./temp/wavs_out')

for i in tqdm(range(totalFiles)):
    format = m4a_files[i][-3:]
    wav_file_name = './temp/wavs_out/'+m4a_files[i][0:-4] + '.wav'
    track = AudioSegment.from_file(os.path.join(args.audio_source,m4a_files[i]),  format = format)
    file_handle = track.export(wav_file_name, format='wav')