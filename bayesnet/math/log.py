import numpy as np
from bayesnet.tensor.constant import Constant
from bayesnet.tensor.tensor import Tensor
from bayesnet.function import Function


class Log(Function):
    """
    element-wise natural logarithm of the input
    y = log(x)
    """

    def _forward(self, x):
        x = self._convert2tensor(x)
        self.x = x
        output = np.log(self.x.value)
        if isinstance(self.x, Constant):
            return Constant(output)
        return Tensor(output, function=self)

    def _backward(self, delta):
        dx = delta / self.x.value
        self.x.backward(dx)


def log(x):
    """
    element-wise natural logarithm of the input
    y = log(x)
    """
    return Log().forward(x)
