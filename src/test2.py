import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print(1)

    def tearDown(self):
        print(0)


class MyTest(Test):
    def test1(self):
        print('test1')

    def test2(self):
        print('test2')


class MyTest2(Test):
    def tst1(self):
        print('tst1')

    def tst2(self):
        print('tst2')


if __name__ == '__main__':
   suit = unittest.TestSuite()
   suit.addTest(MyTest2("tst1"))
   runner = unittest.TextTestRunner()
   runner.run(suit)
