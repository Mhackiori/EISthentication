# ID1: architecture (LCO = 2)
# ID2: model (Eunicell LR2032 = 5)
# ID3: stage

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

# Battery stage
id3s = {
    '_I_': 0,
    '_II_': 1,
    '_III_': 2,
    '_IV_': 3,
    '_V_': 4,
    '_VI_': 5,
    '_VII_': 6,
    '_VIII_': 7,
    '_IX_': 8,
}

dfs = []

for i, file in enumerate(files):
    filePath = os.path.join(datasetDir, file)

    # Only cells @ 25C contain the header, handling this
    if '25C' in filePath:
        df = pd.read_csv(filePath, sep="\t")
    else:
        df = pd.read_csv(filePath, sep="\t", names=['time/s', '           cycle number', 'freq/Hz', '           Re(Z)/Ohm', '  -Im(Z)/Ohm', '   |Z|/Ohm', '   Phase(Z)/deg'], header=None)

    max_cycles = int(max(df['           cycle number']))

    for cycle in range(max_cycles):
        print(f'[🔢 PROCESSING] {i+1}/{len(files)} {cycle+1}/{max_cycles}', end='\r')

        df_cycle = df[df['           cycle number'] == cycle + 1]
        z1 = df_cycle['           Re(Z)/Ohm']
        z2 = df_cycle['  -Im(Z)/Ohm']

        z1 = smooth(z1)
        z2 = smooth(z2)

        for k in id3s:
            if k in file:
                id3 = id3s[k]

        proc_df = pd.DataFrame({
            'z1': z1,
            'z2': z2,
            'id1': [0] * len(z1),
        })

        features = tsfresh.extract_features(proc_df, column_id="id1", column_sort="z1", disable_progressbar=True)

        # Saving IDs again
        features['id1'] = [2] * len(features)
        features['id2'] = [5] * len(features)
        features['id3'] = [id3] * len(features)

        dfs.append(features)

    print()

feat = pd.concat(dfs)
feat.to_parquet(saveName)

print()