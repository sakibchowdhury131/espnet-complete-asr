### paths and params

AUDIO_PATH='./dataset/audio_files'
RESAMPLED_AUDIO_PATH='./temp/resampled_audios'
METADATA_PATH='./dataset.metadata.tsv'
KALDI_DIRECTORY='./dataset/KALDI_FILES'
ESPNET_RECIPEE_PATH='../espnet/egs/librispeech/asr1/'
BITRATE=16
SAMPLING_RATE=16000


############################ Stages: you can manually control any of the preprocessing stages
### preprocessing stages
DATA_CURATION=true
FORMAT_CORRECTION=true
DATA_SPLITTING=true
KALDI_FILES_PREPARATION=true


### Training stages
STAGE1=false
STAGE2=false
STAGE3=false
STAGE4=false
STAGE5=false



############################ Preprocessing Stages
### curate the dataset
if `$DATA_CURATION -eq true`
then
    python3 DataCuration.py
fi



### correct the audio formats

if `$FORMAT_CORRECTION -eq true`
then
    echo Formatting Audio in $AUDIO_PATH
    echo Configuration is: -------------
    echo BITRATE: PCM$BITRATE
    echo SAMPLING_RATE: $SAMPLING_RATE
    mkdir $RESAMPLED_AUDIO_PATH
    for i in `ls $AUDIO_PATH`;
        do 
        sox $AUDIO_PATH/$i -r $SAMPLING_RATE -b $BITRATE -c 1 $RESAMPLED_AUDIO_PATH/$i
    done
    mv $AUDIO_PATH/* ./temp
    mv $RESAMPLED_AUDIO_PATH/* $AUDIO_PATH
    echo AUDIO FORMAT CORRECTION COMPLETED
fi

### Preparing Train - dev - test sets (default 90% - 5% - 5%)
if `$DATA_SPLITTING -eq true`
then 
    echo data splitting ---- 
    python3 ./misc/train_test_dev_split.py
    echo completed
fi


### Kaldi Data Prep
if `$KALDI_FILES_PREPARATION -eq true`
then
    mkdir $KALDI_DIRECTORY
    echo generating utt2spk files
    python3 ./KaldiPreprocessing/generate_utt2spk.py

    echo generating spk2utt files
    perl ./KaldiPreprocessing/utt2spk_to_spk2utt.pl ./dataset/KALDI_FILES/train/utt2spk > ./dataset/KALDI_FILES/train/spk2utt
    perl ./KaldiPreprocessing/utt2spk_to_spk2utt.pl ./dataset/KALDI_FILES/val/utt2spk > ./dataset/KALDI_FILES/val/spk2utt
    perl ./KaldiPreprocessing/utt2spk_to_spk2utt.pl ./dataset/KALDI_FILES/test/utt2spk > ./dataset/KALDI_FILES/test/spk2utt

    echo generating text files
    python3 ./KaldiPreprocessing/gen-text.py
    
    echo generating scp files
    python3 ./KaldiPreprocessing/gen-scp.py
fi




############################ Training Stages

### move the files to appropriate directory 
echo preparing recipe
mv ./dataset $ESPNET_RECIPEE_PATH
mkdir $ESPNET_RECIPEE_PATH/data
cd $ESPNET_RECIPEE_PATH
cp -r $KALDI_DIRECTORY/* ./data
mv ./data/val ./data/dev




### training stage 1
if `$STAGE1 -eq true`
then
    ./run.sh  --ngpu 1 --stage 1 --stop-stage 1
fi


### training stage 2
if `$STAGE2 -eq true`
then
    ./run.sh  --ngpu 1 --stage 2 --stop-stage 2
fi


### training stage 3
if `$STAGE3 -eq true`
then
    ./run.sh  --ngpu 1 --stage 3 --stop-stage 3
fi


### training stage 4
if `$STAGE4 -eq true`
then
    ./run.sh  --ngpu 1 --stage 4 --stop-stage 4
fi


### training stage 5
if `$STAGE5 -eq true`
then
    ./run.sh  --ngpu 1 --stage 5 --stop-stage 5
fi
