"""split.py
A script that splits the data (CSV) into train/test/val splits.

python src/split.py
"""
from pandas import pd
from pathlib import Path
from sklearn.model_selection import train_test_split