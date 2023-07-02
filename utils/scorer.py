from jiwer import wer,cer
import argparse


parser = argparse.ArgumentParser(description='EVALUATER FOR ASR')
parser.add_argument('--ground_truth', type=str)
parser.add_argument('--predicted_sentence', type=str)
args = parser.parse_args()
#ground_truth = "My name is Murad"
#predicted_sentence = 'My nam is Murad'

ground_truth = [args.ground_truth]
predicted_sentence = [args.predicted_sentence]

def wer_cer(gt,pred):
    return wer(gt,pred),cer(gt,pred)

WER,CER = wer_cer(ground_truth,predicted_sentence)
print("WER : ",WER)
print("CER : ",CER)