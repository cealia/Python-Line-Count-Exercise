import unittest
import os
from linecounter import LineCounter

class LineCounterTestCase(unittest.TestCase):
    """
    A Python unittest module to test LineCounter
    """
    def setUp(self):
        # print(os.path.join(os.getcwd(), "mydir"))
        self.args1 = (os.path.join(os.getcwd(), "mydir"), '.txt')
        self.args2 = (os.path.join(os.getcwd(), "mydir2"), '.txt')
        self.args3 = (os.path.join(os.getcwd(), "mydir2"), '.py')
        self.args4 = (os.path.join(os.getcwd(), "mydir2"), '.sh')

    def tearDown(self):
        self.args1 = None
        self.args2 = None
        self.args3 = None
        self.args4 = None

    def test1(self):
        """
        Test for a 2-layer recursive directory listing for .txt extension files
        """
        expected = (5, 33, 6.6)
        l_c = LineCounter(*self.args1)
        result = l_c.get_line()
        self.assertTupleEqual(expected, result)
    def test2(self):
        """
        Test for a 3-layer recursive directory listing for .txt extension files
        """
        expected = (3, 4, 1.333)
        l_c = LineCounter(*self.args2)
        result = l_c.get_line()
        self.assertTupleEqual(expected[:2], result[:2])
        self.assertAlmostEqual(expected[2], result[2], 3)
    def test3(self):
        """
        Test for a 3-layer recursive directory listing for .py extension
        (something other than .txt) files
        """
        expected = (3, 10, 3.333)
        l_c = LineCounter(*self.args3)
        result = l_c.get_line()
        self.assertTupleEqual(expected[:2], result[:2])
        self.assertAlmostEqual(expected[2], result[2], 3)
    def test4(self):
        """
        Test for directory listing when there's no file of the same extension:
        should be able to handle division by zero
        """
        expected = (0, 0, float('-inf'))
        l_c = LineCounter(*self.args4)
        result = l_c.get_line()
        print(result)
        self.assertTupleEqual(expected[:2], result[:2])
        self.assertAlmostEqual(expected[2], result[2], 3)

if __name__ == "__main__":
    """
    Test for linecounter
    """
    unittest.main()
