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
df = pd.read_csv(INPUT_PATH)
print(f"Total reviews loaded: {len(df)}")

###### Split ######
train_df, temp_df = train_test_split(df, test_size = 0.2, random_state = 42, stratify = df["label"])

val_df, test_df = train_test_split(temp_df, test_size= 0.5, random_state= 42, stratify = temp_df["label"])

###### Save ######

Path("data/splits").mkdir(parents = True, exist_ok = True)

train_df.to_csv(TRAIN_PATH, index = False, encoding = "utf-8-sig")
val_df.to_csv(VAL_PATH, index = False, encoding = "utf-8-sig")
test_df.to_csv(TEST_PATH, index = False, encoding = "utf-8-sig")

###### Output ######
print(f"\n{'='*40}")
print(f"Split complete:")
print(f"  Train: {len(train_df)} rows  → {TRAIN_PATH}")
print(f"  Val:   {len(val_df)} rows  → {VAL_PATH}")
print(f"  Test:  {len(test_df)} rows  → {TEST_PATH}")
 