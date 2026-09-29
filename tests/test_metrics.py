import numpy as np
from src.metrics import smape

def test_perfect():
    y = np.array([1.0, 10.0, 250.5])
    assert smape(y, y) == 0.0

def test_symmetric():
    a, b = np.array([10.0, 20.0, 5.0]), np.array([12.0, 15.0, 9.0])
    assert np.isclose(smape(a, b), smape(b, a))

def test_zero_no_nan():
    z = np.zeros(4)
    assert smape(z, z) == 0.0
