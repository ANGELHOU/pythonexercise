import unittest
from ..settings import USERS


class TestCase(unittest.TestCase):
    def __init__(self):
        self.user = USERS['dingbei']

    def setup(self):
        pass

    def tearDown(self):
        pass
