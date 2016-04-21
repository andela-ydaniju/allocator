import unittest
from .context import Fellow

class TestFellow(unittest.TestCase):
    def test_fellow_is_initialized_with_name(self):
        man = Fellow("Yusuf")
        self.assertEqual("Yusuf", man.name)

    def test_set_amity_interest(self):
        man = Fellow("Yusuf")
        man.set_amity_interest("Y")
        self.assertEqual("Y", man.amity_interest)

    def test_set_amity_room_name(self):
        man = Fellow("Yusuf")
        man.set_amity_room_name("Yacht")
        self.assertEqual("Yacht", man.amity_room_name)

    def test_show_fellow_info(self):
        man = Fellow("Yusuf")
        self.assertIsNone(man.show_fellow_info())

if __name__ == '__main__':
    unittest.main()
