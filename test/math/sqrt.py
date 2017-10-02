import unittest
import numpy as np
import bayesnet as bn


class TestSqrt(unittest.TestCase):

    def test_sqrt(self):
        x = bn.Parameter(2.)
        y = bn.sqrt(x)
        self.assertEqual(y.value, np.sqrt(2))
        y.backward()
        self.assertEqual(x.grad, 0.5 / np.sqrt(2))


if __name__ == '__main__':
    unittest.main()
