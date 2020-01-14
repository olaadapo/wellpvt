import unittest
from wellpvt import Gas
from wellpvt import Oil
        
class TestOilClass(unittest.TestCase):
    def setUp(self):
        self.oil = Oil(40)
        
    def test_initialization(self):
        self.assertEqual(self.oil.api, 40, 'incorrect api')
        
    def test_calculatesg(self):
        sg = self.oil.calculate_sg()
        
        self.assertEqual(round(sg, 2), 0.83, 'incorrect specific gravity')
        
    def test_calculatedensity(self):
        density = self.oil.calculate_density()
        
        self.assertEqual(round(density, 1), 51.5, 'incorrect density')
        
    def test_setapi(self):
        self.oil.set_api(38)
        
        self.assertEqual(self.oil.api, 38, 'incorrect api')
        
class TestGasClass(unittest.TestCase):
    def setUp(self):
        self.gas = Gas(1200, 60, 0.78)
        
    def test_initialization(self):
        self.assertEqual(self.gas.pressure, 1200, 'incorrect pressure')
        self.assertEqual(self.gas.temperature, 60, 'incorrect temperature')
        self.assertEqual(self.gas.sg, 0.78, 'incorrect specific gravity')
        
    def test_calculatepseudocritical(self):
        pc, tc = self.gas.calculate_pseudo_critical()
        
        self.assertEqual(round(pc, 1), 658.9, 'incorrect pseudo-critical pressure')
        self.assertEqual(round(tc, 1), 400.9, 'incorrect pseudo-critical temperature')
        
    def test_calculatez(self):
        z = self.gas.calculate_z()
        
        self.assertEqual(round(z, 3), 0.705, 'incorrect gas compressibility')
        
    def test_calculatedensity(self):
        density = self.gas.calculate_density()
        
        self.assertEqual(round(density, 3), 6.896, 'incorrect density')
        
    def test_calculatebg(self):
        bg = self.gas.calculate_bg()
        
        self.assertEqual(round(bg, 3), 0.009, 'incorrect formation volume factor (bg)')
        
    def test_calculateviscosity(self):
        viscosity = self.gas.calculate_viscosity()
        
        self.assertEqual(round(viscosity, 3), 0.015, 'incorrect viscosity')
    
if __name__ == '__main__':
    unittest.main()