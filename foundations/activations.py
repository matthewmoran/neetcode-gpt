import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        res = []
        for i in z:
            res.append(round(1/(1+ math.e ** - i), 5))

        return res
        pass

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        res = []
        for i in z:
            if i < 0:
                res.append(0.0)
            else:
                res.append(round(i, 5))

        return res
        pass
