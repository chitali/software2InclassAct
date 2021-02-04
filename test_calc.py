import unittest
import calc

class Testcalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10.39, 20.39),30.78)
        self.assertEqual(calc.add(-10, 5),-5)
        self.assertEqual(calc.add("yes", 10),"Error")
        self.assertEqual(calc.add(10, "ten"),"Error")
        self.assertEqual(calc.add("10", 10), 20)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(10.5, 20.5),-10)
        self.assertEqual(calc.subtract(10, 2), 8)
        self.assertEqual(calc.subtract("yes", 10),"Error")
        self.assertEqual(calc.subtract(10, "ten"),"Error")
        self.assertEqual(calc.subtract("10", 10),0)
    
    def test_multipy(self):
        self.assertEqual(calc.multipy(10.39, 20.39),211.8521)
        self.assertEqual(calc.multipy(5, 5),25)
        self.assertEqual(calc.multipy("yes", 10),"Error")
        self.assertEqual(calc.multipy(10, "ten"),"Error")
        self.assertEqual(calc.multipy("10", 10),100)
    
    def test_divide(self):
        self.assertEqual(calc.divide(10, 2),5)
        self.assertEqual(calc.divide(5, 2),2.5)
        self.assertEqual(calc.divide(5, 0),"Error")
        self.assertEqual(calc.divide("yes", 10),"Error")
        self.assertEqual(calc.divide(10, "ten"),"Error")
        self.assertEqual(calc.divide("10", 10),1)

if __name__ ==  "__main__":
    unittest.main()