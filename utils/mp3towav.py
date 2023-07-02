import os
from tqdm import tqdm
from pydub import AudioSegment
import argparse


parser = argparse.ArgumentParser(description='Convert mp3 files to wav format')
parser.add_argument('--audio_source', type=str, default='./dataset/audio_files')
args = parser.parse_args()

mp3_files = os.listdir(args.audio_source)
totalFiles = len(mp3_files)

if not os.path.exists('./temp/wavs_out'):
    os.makedirs('./temp/wavs_out')

for i in tqdm(range(totalFiles)):
    wav_file_name = './temp/wavs_out/'+mp3_files[i][0:-4] + '.wav'
    track = AudioSegment.from_file(os.path.join(args.audio_source,mp3_files[i]),  format= 'mp3')
    file_handle = track.export(wav_file_name, format='wav')