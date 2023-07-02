from tqdm import tqdm
import shutil
import os
TEST="./test_set"
if not os.path.exists(TEST):
    os.makedirs(TEST)
with open('wav.scp', 'r') as f:
    lines = f.readlines()
for line in tqdm(lines):
    data = line.split(' ')
    src = data[1].replace('\n', '')
    shutil.copy(src, TEST)