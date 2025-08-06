# test_pygametutorials.py
"""
Tests for PygameTutorials module.
"""

import unittest
from pygametutorials import PygameTutorials

class TestPygameTutorials(unittest.TestCase):
    """Test cases for PygameTutorials class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PygameTutorials()
        self.assertIsInstance(instance, PygameTutorials)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PygameTutorials()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
