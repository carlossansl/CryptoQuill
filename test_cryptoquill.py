# test_cryptoquill.py
"""
Tests for CryptoQuill module.
"""

import unittest
from cryptoquill import CryptoQuill

class TestCryptoQuill(unittest.TestCase):
    """Test cases for CryptoQuill class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoQuill()
        self.assertIsInstance(instance, CryptoQuill)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoQuill()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
