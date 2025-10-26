# test_mangaallocator.py
"""
Tests for MangaAllocator module.
"""

import unittest
from mangaallocator import MangaAllocator

class TestMangaAllocator(unittest.TestCase):
    """Test cases for MangaAllocator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MangaAllocator()
        self.assertIsInstance(instance, MangaAllocator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MangaAllocator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
