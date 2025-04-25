import unittest
from inbo_tests.mr import MRTestCase

def suite():
    """Create a test suite for all tests in the module."""
    suite = unittest.TestSuite()
    suite.addTest(MRTestCase('test_mr_data'))
    # Add more test cases as needed
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())