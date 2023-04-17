import os

# Seed for reproducibility
SEED = 151836

# Folders
RAW = './Datasets/Raw/'
PROCESSED = './Datasets/Processed/'

# Datasets
if os.path.exists(PROCESSED):
    DATASETS = sorted(os.listdir(PROCESSED))