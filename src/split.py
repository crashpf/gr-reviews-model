"""
split.py
A script that splits the data (CSV) into train/test/val splits.

How to use:
python src/split.py
"""
from pandas import pd
from pathlib import Path
from sklearn.model_selection import train_test_split

###### Config ######

INPUT_PATH = Path("data/raw/Sentiment-analysis.xlsx")
TRAIN_PATH = Path("data/splits/train.csv")
TEST_PATH = Path("data/splits/test.csv")
VAL_PATH = Path("data/splits/train.csv")

###### Load ######