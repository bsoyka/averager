import unittest, averager

class TestAverager(unittest.TestCase):

    def test_average_1_5(self):
        self.assertEqual(averager.Averager.average(1, 5), 3)

class TestWeightedAverager(unittest.TestCase):
    
    def setUp(self):
        self.averager_instance = averager.WeightedAverager(a=1, b=2, c=3)
    
    def test_average_a_1_c_2(self):
        self.assertEqual(self.averager_instance.average(a=1, c=2), 1.75)

if __name__ == '__main__':
    unittest.main()
