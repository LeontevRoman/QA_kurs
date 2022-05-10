import unittest
from Link import Link


class TestLink(unittest.TestCase):
    def setUp(self):
        self.Link = Link()

    def test_link1(self):
        self.assertEqual(self.Link.link_1(), "Congratulations! You have successfully registered!")

    def test_link2(self):
        self.assertEqual(self.Link.link_2(), "Congratulations! You have successfully registered!")


if __name__ == '__main__':
    unittest.main()
