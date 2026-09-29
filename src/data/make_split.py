import pandas as pd
from sklearn.model_selection import train_test_split
from src.config import DATASET, ARTIFACTS, SEED

df = pd.read_csv(DATASET / "train.csv")

# stratify on price deciles so train and validation have similar price distributions
bins = pd.qcut(df["price"], q=10, duplicates="drop")
train_df, val_df = train_test_split(
    df, test_size=0.20, random_state=SEED, shuffle=True, stratify=bins
)

out = ARTIFACTS / "splits"
out.mkdir(parents=True, exist_ok=True)
train_df[["sample_id"]].to_csv(out / "train_ids.csv", index=False)
val_df[["sample_id"]].to_csv(out / "val_ids.csv", index=False)

assert set(train_df.sample_id).isdisjoint(val_df.sample_id)
print("train:", len(train_df), "| val:", len(val_df))
