import numpy as np


class Individual:
    def __init__(self, dimensions=0):
        self.variables = np.zeros(dimensions)
