# import os

# with open('vocab_issue/old_vocabs.txt', 'r') as f:
#     lines = f.readlines()

# f = open('vocab_issue/new_units.txt', 'a')
# for i, line in enumerate(lines):
#     line = line.replace('\n', '')
#     f.write(f'{line} {i+1}\n')

# f.close()

# f = open('vocab_issue/new_vocab.txt', 'a')
# for i, line in enumerate(lines):
#     line = line.replace('\n', '')
#     f.write(f'{line}\t0\n')

# f.close()
existing_vocabulary = []
with open('vocab_issue/old_vocabs.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    existing_vocabulary.append(line.replace('\n', ''))



with open('vocab_issue/train_960_unigram5000_units.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    line = line.split()[0]
    if not line in existing_vocabulary:
        existing_vocabulary.append(line)

# f = open('vocab_issue/new_units.txt', 'a')
# for i, item in enumerate(existing_vocabulary):
#     f.write(f"{item} {i+1}\n")

# f.close()

dictionary = {}
with open('vocab_issue/train_960_unigram5000.vocab', 'r') as f:
    lines = f.readlines()



for line in lines:
    data = line.split('\t')
    dictionary[data[0]] = data[1].replace('\n', '')




f = open('vocab_issue/new_.vocab', 'a')
for i, item in enumerate(existing_vocabulary):

    if not item in dictionary:
        f.write(f"{item}\t0\n")
    else:
        f.write(f"{item}\t{dictionary[item]}\n")
f.close()
