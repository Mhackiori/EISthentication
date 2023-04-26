import os

# Seed for reproducibility
SEED = 151836

# Folders
RAW = './Datasets/Raw/'
PROCESSED = './Datasets/Processed/'
RESULTS = './Results/'
FIGURES = './Results/Figures/'
COMPLEXITY = './Results/Complexity/'

# Datasets
if os.path.exists(PROCESSED):
    DATASETS = sorted(os.listdir(PROCESSED))

# Balance
BALANCES = [
    [50, 50],
    [60, 40],
    [70, 30],
    [80, 20]
]