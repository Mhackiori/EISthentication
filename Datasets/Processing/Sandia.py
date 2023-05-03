# ID1: all
# ID2: from 0 to 3
# ID3: cell number

import os
import pandas as pd
import tsfresh
import warnings

import sys
sys.path.insert(0, os.getcwd())

from utils.const import *
from utils.helperFunctions import *


warnings.filterwarnings("ignore")

if not sys.warnoptions:
    warnings.simplefilter("ignore")
    os.environ["PYTHONWARNINGS"] = "ignore"


datasetName = __file__.split('/')[-1].split('.')[0]
datasetDir = os.path.join(RAW, datasetName)

numFiles = sum(len(files) for _, _, files in os.walk(datasetDir))
files = sorted(os.listdir(datasetDir))

processedFolder = './Datasets/Processed/'
saveName = os.path.join(processedFolder, datasetName) + '.parquet'

if not os.path.exists(processedFolder):
    os.mkdir(processedFolder)

id1s = ['NMC', 'LFP', 'LCO', 'NCA']

dfs = []

for i, file in enumerate(files):
    print(f'[🔢 PROCESSING] {i+1}/{len(files)}', end='\r')
    filePath = os.path.join(datasetDir, file)

    z1 = []
    z2 = []

    if 'Cycling' in file:
        with open(filePath, 'r') as f:
            content = f.read()
            data = content.split('End Comments\n')[1]
            rows = data.split('\n')
            for row in rows:
                if len(row) > 0:
                    z1.append(row.split('\t')[4])
                    z2.append(row.split('\t')[5])
    else:
        with open(filePath, 'r') as f:
            try:
                content = f.read()
                rows = content.split('\n')
                for row in rows[1:]:
                    if len(row) > 0:
                        z1.append(row.split(',')[2])
                        z2.append(row.split(',')[3])
            except UnicodeDecodeError:
                continue

    z1 = smooth(z1)
    z2 = smooth(z2)

    for j, id in enumerate(id1s):
        if id in file:
            id1 = j

    if '_1_' in file:
        id3 = 1
    elif '_2_' in file:
        id3 = 2
    elif '_3_' in file:
        id3 = 3

    df = pd.DataFrame({
        'z1': z1,
        'z2': z2,
        'id1': [j] * len(z1),
    })

    features = tsfresh.extract_features(df, column_id="id1", column_sort="z1", disable_progressbar=True)

    # Saving IDs again
    features['id1'] = [id1] * len(features)
    features['id2'] = [id1] * len(features) # ID1 and ID2 for this first dataset are the same
    features['id3'] = [id3] * len(features)

    dfs.append(features)

feat = pd.concat(dfs)
feat.to_parquet(saveName)

print()