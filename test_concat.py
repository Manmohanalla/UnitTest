import unittest
from concat import Add

class MyTestCase(unittest.TestCase):
    def test1(self):
        concat = Add()
        self.assertEqual(concat.add('Hello','world!'), 'Hello world!')
    def test2(self):
        concat = Add()
        try:
        	self.assertEqual(concat.add(5,5), 11)
        except Exception as (e):
        	print e
if __name__ == '__main__':
    unittest.main()

