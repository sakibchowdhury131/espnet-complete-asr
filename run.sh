### paths and params
DATASET_PATH='./dataset/'
AUDIO_PATH=$DATASET_PATH/audio_files
RESAMPLED_AUDIO_PATH='./temp/resampled_audios'
METADATA_PATH=$DATASET_PATH/metadata.tsv
KALDI_DIRECTORY=$DATASET_PATH/KALDI_FILES
ESPNET_RECIPEE_PATH='../espnet/egs/librispeech/asr1'
ESPNET_TRAIN_CONFIG_FILE='train_pytorch_transformer_lr5.0_ag8.v2.yaml'
BITRATE=16
SAMPLING_RATE=16000


############################ Manual Control over each operational stage
### preprocessing stages
DATA_CURATION=true
FORMAT_CORRECTION=false
DATA_SPLITTING=false
KALDI_FILES_PREPARATION=false


### Training stages
TRAINING_START=false
STAGE1=false
STAGE2=false
STAGE3=false
STAGE4=false
STAGE5=false



############################ Preprocessing Stages
### curate the dataset
if `$DATA_CURATION -eq true`
then
    python3 DataCuration.py --audio_source $AUDIO_PATH --metadata $METADATA_PATH
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
        sox $AUDIO_PATH/$i -r $SAMPLING_RATE -b $BITRATE -c 1 $RESAMPLED_AUDIO_PATH/${i//flac/wav}
    done
    mv $AUDIO_PATH/* ./temp
    mv $RESAMPLED_AUDIO_PATH/* $AUDIO_PATH
    echo AUDIO FORMAT CORRECTION COMPLETED
fi

### Preparing Train - dev - test sets (default 90% - 5% - 5%)
if `$DATA_SPLITTING -eq true`
then 
    echo data splitting ---- 
    python3 ./misc/train_test_dev_split.py --metadata $METADATA_PATH --train_split 0.9
    echo completed
fi


### Kaldi Data Prep
if `$KALDI_FILES_PREPARATION -eq true`
then
    mkdir $KALDI_DIRECTORY
    echo generating utt2spk files 
    python3 ./KaldiPreprocessing/generate_utt2spk.py --kaldi_destination $KALDI_DIRECTORY

    echo generating spk2utt files
    perl ./KaldiPreprocessing/utt2spk_to_spk2utt.pl $KALDI_DIRECTORY/train/utt2spk > $KALDI_DIRECTORY/train/spk2utt
    perl ./KaldiPreprocessing/utt2spk_to_spk2utt.pl $KALDI_DIRECTORY/val/utt2spk > $KALDI_DIRECTORY/val/spk2utt
    perl ./KaldiPreprocessing/utt2spk_to_spk2utt.pl $KALDI_DIRECTORY/test/utt2spk > $KALDI_DIRECTORY/test/spk2utt

    echo generating text files
    python3 ./KaldiPreprocessing/gen-text.py --kaldi_destination $KALDI_DIRECTORY
    
    echo generating scp files
    python3 ./KaldiPreprocessing/gen-scp.py --kaldi_destination $KALDI_DIRECTORY --audio_source $AUDIO_PATH
fi




############################ Training Stages

### move the files to appropriate directory 
if `$TRAINING_START -eq true`
then
    echo preparing recipe
    mv $DATASET_PATH $ESPNET_RECIPEE_PATH
    mkdir $ESPNET_RECIPEE_PATH/data
    cd $ESPNET_RECIPEE_PATH
    cp -r $KALDI_DIRECTORY/* ./data
    mv ./data/val ./data/dev
fi




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
    ./run.sh  --ngpu 1 --stage 3 --stop-stage 3 --train-config ./conf/tuning/$ESPNET_TRAIN_CONFIG_FILE
fi


### training stage 4
if `$STAGE4 -eq true`
then
    ./run.sh  --ngpu 1 --stage 4 --stop-stage 4 --train-config ./conf/tuning/$ESPNET_TRAIN_CONFIG_FILE
fi


### training stage 5
if `$STAGE5 -eq true`
then
    ./run.sh  --ngpu 1 --stage 5 --stop-stage 5
fi
