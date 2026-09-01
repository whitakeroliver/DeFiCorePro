# test_deficorepro.py
"""
Tests for DeFiCorePro module.
"""

import unittest
from deficorepro import DeFiCorePro

class TestDeFiCorePro(unittest.TestCase):
    """Test cases for DeFiCorePro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DeFiCorePro()
        self.assertIsInstance(instance, DeFiCorePro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DeFiCorePro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
