import os
import unittest

if __name__ == '__main__':
    os.environ['TESTING'] = 'True'

    unittest.main('tests')
