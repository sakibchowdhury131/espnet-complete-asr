import requests
import json
from jiwer import wer,cer
from tqdm import tqdm

def wer_cer(gt,pred):
    return wer(gt,pred),cer(gt,pred)

WERs = []
CERs = []
audio_dir = './test_set/audios'
text = './test_set/text'

with open(text, 'r') as f:
    lines = f.readlines()

for line in tqdm(lines):
    data = line.split(' ')
    filename = data[0]+'.wav'
    audio_location = f"{audio_dir}/{filename}"
    ground_truth = ' '.join(data[1:]).replace('\n', '')
    with open(audio_location, 'rb') as f:
        r = requests.post('http://172.16.4.132:6589/nlp/dataset/v1/audio/speech-to-text', files={'files': f})
    x = json.loads(r.text)
    prediction = x["text"]
    WER = wer(ground_truth, prediction)
    CER = cer(ground_truth, prediction)
    WERs.append(WER)
    CERs.append(CER)
    print('avg WER: ',sum(WERs)/len(WERs))
    print('avg CER: ',sum(CERs)/len(CERs))
    print('gt: ',ground_truth)
    print('pred: ', prediction)

