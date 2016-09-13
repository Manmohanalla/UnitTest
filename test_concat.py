import unittest
from concat import Add

class MyTestCase(unittest.TestCase):
    def test1(self):
        concat = Add()
        self.assertEqual(concat.add('Hello','world'), 'Hello world')
    def test2(self):
        concat = Add()
        self.assertEqual(concat.add(5,5), 10)
if __name__ == '__main__':
    unittest.main()

