import os
import soundfile as sf    
from tqdm import tqdm
import librosa

def formatAudio(AUDIO_SOURCE = './dataset/audio_files'):  #path to the folder containing the audio files
    for line in tqdm(lines):
        #extract the fields
        filename = line.split("\t")[0]
        speaker_id = line.split("\t")[1]
        
        #Adding the extension .flac
        audio_name = filename + '.flac'
        
        #rename by this format : SpeakerId-FileName
        new_name = speaker_id + "-" + filename
        
        #read the audio 
        data, samplerate = sf.read(os.path.join(AUDIO_SOURCE, audio_name))
        
        #check sampling rate
        if samplerate!=16000:
            #if sampling rate isn't 16k then resample it to 16k
            data = librosa.resample(data, orig_sr = samplerate, target_sr = 16000)
            
        
        #reading the audio
        audio = sf.SoundFile(os.path.join(AUDIO_SOURCE, audio_name))
        
        
        #checking if it is 16-bit PCM encoded
        
        if audio.subtype=='PCM_16':
            # Just rename the file and save
            os.rename(os.path.join(AUDIO_SOURCE,audio_name),os.path.join(AUDIO_SOURCE,new_name+".wav"))
        else:
            #convert to 16 bit PCM and rewrite it
            sf.write(os.path.join(AUDIO_SOURCE,new_name+".wav"), data, 16000 , subtype='PCM_16')
        