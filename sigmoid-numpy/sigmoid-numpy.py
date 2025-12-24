import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.array(x)
    dnm = np.exp(-x) + 1

    return 1.0/dnm