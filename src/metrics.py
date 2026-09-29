import numpy as np

def smape(y_true, y_pred, eps=1e-8):
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    denom = (np.abs(y_true) + np.abs(y_pred)) / 2.0
    ratio = np.where(denom < eps, 0.0, np.abs(y_true - y_pred) / np.maximum(denom, eps))
    return float(100.0 * ratio.mean())
