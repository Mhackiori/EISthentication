# ID1: architecture (NCA = 3)
# ID2: model (NCR18650B = 5)
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

dfs = []

for i, file in enumerate(files):
    print(f'[🔢 PROCESSING] {i+1}/{len(files)}', end='\r')
    filePath = os.path.join(datasetDir, file)

    # Loading file
    xls = pd.ExcelFile(filePath)

    # Extracting and merging sheets
    sheets = xls.sheet_names
    df = xls.parse(sheets[0])

    for col in df.columns:
        if 'Re' in col:
            z1 = df[col].tolist()
        else:
            z2 = df[col].tolist()

    z1 = smooth(z1)
    z2 = smooth(z2)

    proc_df = pd.DataFrame({
        'z1': z1,
        'z2': z2,
        'id1': [3] * len(z1),
    })

    features = tsfresh.extract_features(
        proc_df, column_id="id1", column_sort="z1", disable_progressbar=True)

    # Saving IDs again
    features['id1'] = [3] * len(features)
    features['id2'] = [5] * len(features)

    soc = int(file.split('.')[0][-2:])
    if soc == 20:
        id3 = 0
    elif soc == 50:
        id3 = 1
    else:
        id3 = 2

    features['id3'] = [id3] * len(features)

    dfs.append(features)

feat = pd.concat(dfs)
feat.to_parquet(saveName)

print()
