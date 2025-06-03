import unittest
import numpy as np
from mean_var_std import calculate

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = calculate([2,6,2,8,4,0,1,5,7])
        expected = {
          'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889],
          'variance': [[9.555555555555555, 0.6666666666666666, 10.666666666666666], [4.222222222222222, 10.666666666666666, 5.555555555555555], 6.987654320987654],
          'standard deviation': [[3.091206165165235, 0.816496580927726, 3.265986323710904], [2.0548046676563256, 3.265986323710904, 2.357022603955158], 2.6434171674156266],
          'max': [[8, 6, 7], [6, 8, 7], 8],
          'min': [[1, 4, 0], [2, 0, 1], 0],
          'sum': [[11, 15, 9], [10, 12, 13], 35]
        }
        self.assertAlmostEqual(actual['mean'][0][0], expected['mean'][0][0], places=1, msg='Expected different value for mean[0][0]')
        self.assertAlmostEqual(actual['variance'][2], expected['variance'][2], places=1, msg='Expected different value for flattened variance')
        self.assertAlmostEqual(actual['standard deviation'][1][1], expected['standard deviation'][1][1], places=1, msg='Expected different value for standard deviation[1][1]')
        self.assertEqual(actual['max'][0][2], expected['max'][0][2], 'Expected different value for max[0][2]')
        self.assertEqual(actual['min'][1][0], expected['min'][1][0], 'Expected different value for min[1][0]')
        self.assertEqual(actual['sum'][2], expected['sum'][2], 'Expected different value for sum[2]')

    def test_calculate_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculate([2, 6, 2, 8])
