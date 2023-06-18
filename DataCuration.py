import argparse
from CheckingProtocols.DataCheck import dataIntegrityChecker
from CheckingProtocols.Rename import rename



def main(AUDIO_SOURCE, METADATA, audio_format):
    
    ### data integrity checking 
    OK = True
    dataset_state = dataIntegrityChecker(AUDIO_SOURCE = AUDIO_SOURCE,  METADATA = METADATA, audio_format=audio_format)
    if dataset_state == OK:
        print('Dataset ----> OK')
    else:
        print('Dataset ----> Corrupted. Check Errors')
        return
    


    ### rename the files in spk_id-utt_id.wav in this format
    rename(AUDIO_SOURCE = AUDIO_SOURCE,  
           METADATA = AUDIO_SOURCE)
    

    ### Fix audio format issues 
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Curate Dataset')
    parser.add_argument('--audio_source', type=str, required=True)
    parser.add_argument('--metadata', type=str, required=True)
    parser.add_argument('--audio_format', type=str, required=True)
    args = parser.parse_args()
    main(args.audio_source, args.metadata, args.audio_format)