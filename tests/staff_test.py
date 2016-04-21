import unittest
from .context import Staff

class TestFellow(unittest.TestCase):
    def test_staff_is_initialized_with_name(self):
        man = Staff("Makinwa")
        self.assertEqual("Makinwa", man.name)

    def test_show_staff_info(self):
        man = Staff("Makinwa")
        self.assertIsNone(man.show_staff_info())

if __name__ == '__main__':
    unittest.main()
