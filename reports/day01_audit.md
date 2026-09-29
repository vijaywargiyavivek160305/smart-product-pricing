# Day 1 — Data Audit Report

## Dataset
- Train rows: 75,000
- Test rows: 75,000
- Random seed: 42

## Data Quality
- Missing values: 0
- Duplicate train sample IDs: 0
- Duplicate test sample IDs: 0
- Train/test sample ID overlap: 0
- Empty catalog_content rows: 0
- Zero/negative prices: 0

## Price Distribution
- Median price: approximately 14
- Maximum price: 2796
- Raw price skew: 13.60
- log1p(price) skew: 0.20

## Duplicate Analysis
- Duplicated catalog_content rows: 193
- Duplicate catalog_content groups: 93
- Maximum price ratio within duplicate groups: approximately 16.1x
- Duplicated image_link rows: 2,712
- Exact catalog_content matches between train and test: 234

## Text Statistics
- Character count analyzed
- Word count analyzed
- Digit count analyzed
- Punctuation count analyzed

Train punctuation:
- Mean: approximately 35.76
- Median: approximately 25
- Maximum: 541

Test punctuation:
- Mean: approximately 35.93
- Median: approximately 25
- Maximum: 653

## Outlier Analysis
- Q1: approximately 6.795
- Q3: approximately 28.625
- IQR: approximately 21.830
- Upper IQR bound: approximately 61.37
- IQR outlier rows: 5,524
- Outlier percentage: approximately 7.37%

Outliers are not removed at this stage.

## SMAPE
- Sanity check: 18.18%

## Constant Baseline
- Best constant SMAPE: approximately 72.69%

## Validation Split
- Training IDs: 60,000
- Validation IDs: 15,000
- Seed: 42

Split files:
- artifacts/splits/train_ids.csv
- artifacts/splits/val_ids.csv

## Day 1 Conclusion
The initial data audit is complete. The price target is strongly right-skewed, while log1p substantially reduces the skew. Duplicate and near-duplicate catalog text must be considered during validation. No missing values or ID overlap were found.
