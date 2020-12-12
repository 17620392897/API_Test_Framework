# -!- coding: utf-8 -!-


import paramunittest
import unittest

@paramunittest.parametrized(
    (5,10),
    (10,30)
)
class ApiTestDemo(paramunittest.ParametrizedTestCase):
    def setParameters(self, numa, numb):
        self.a = numa
        self.b = numb
    def test_add_case(self):
        print('%d+%d?=%d'%(self.a,self.b,15))
        self.assertEqual(self.a + self.b,15)



if __name__ == '__main__':
    unittest.main(verbosity=2)

