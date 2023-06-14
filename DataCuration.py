from CheckingProtocols.DataCheck import dataIntegrityChecker
from CheckingProtocols.Rename import rename
def main():

    ### data integrity checking 
    OK = True
    dataset_state = dataIntegrityChecker(AUDIO_SOURCE = './dataset/audio_files',  METADATA = './dataset/metadata.tsv')
    if dataset_state == OK:
        print('Dataset ----> OK')
    else:
        print('Dataset ----> Corrupted. Check Errors')
        return
    

    ### rename the files in spk_id-utt_id.wav in this format
    rename(AUDIO_SOURCE = './dataset/audio_files',  
           METADATA = './dataset/metadata.tsv')
    

    ### Fix audio format issues 
    


if __name__ == '__main__':
    main()