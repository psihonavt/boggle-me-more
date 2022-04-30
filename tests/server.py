import unittest

from hosted_boggle_python import server


class ServerTestCase(unittest.TestCase):
    def test_make_app(self):
        application = server.make_app()
        self.assertIsNotNone(application)
