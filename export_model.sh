EXPORT_DIR=./exported_models/latest
CURRENT_EXP_DIRECTORY=./exp/train_960_pytorch_train_pytorch_transformer_lr5.0_ag8.v2_specaug/results

mkdir -p $EXPORT_DIR/conf/tuning
mkdir -p $EXPORT_DIR/data
mkdir -p $EXPORT_DIR/exp/model


cat ./utils/decode.yaml > $EXPORT_DIR/conf/tuning/decode.yaml
cp $CURRENT_EXP_DIRECTORY/model.acc.best $EXPORT_DIR/exp/model
cp $CURRENT_EXP_DIRECTORY/model.json $EXPORT_DIR/exp/model