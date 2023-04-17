# ID1: architecture (NMC = 0)
# ID2: model (unknown = 4)
# ID3: SOC

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

socs = [20, 40, 60, 80]

dfs = []

for i, file in enumerate(files):
    print(f'[🔢 PROCESSING] {i+1}/{len(files)}', end='\r')
    filePath = os.path.join(datasetDir, file)

    df = pd.read_csv(filePath)

    for soc in socs:

        df_soc = df[df['SOC [%]'] == soc]
        z1 = list(df_soc['Real Part of Impedance [Ohm]'])
        z2 = list(df_soc['Imaginary Part of Impedance [Ohm]'])

        z1 = smooth(z1)
        z2 = smooth(z2)

        proc_df = pd.DataFrame({
            'z1': z1,
            'z2': z2,
            'id1': [0] * len(z1),
        })

        features = tsfresh.extract_features(proc_df, column_id="id1", column_sort="z1", disable_progressbar=True)

        # Saving IDs again
        features['id1'] = [0] * len(features)
        features['id2'] = [4] * len(features)
        features['id3'] = [int((soc/20) - 1)] * len(features)

        dfs.append(features)

feat = pd.concat(dfs)
feat.to_parquet(saveName)

print()