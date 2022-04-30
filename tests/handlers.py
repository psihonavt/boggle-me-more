import unittest


from hosted_boggle_python.handlers import load_dictionary


class HandlerTestCases(unittest.TestCase):
    def test_load_dictionary(self):
        dictionary = load_dictionary()
        self.assertEqual(len(dictionary), 370103)
