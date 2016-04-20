import unittest
from .context import Person

class TestPerson(unittest.TestCase):
 
    def test_person_is_initialized_with_name(self):
        man = Person("Yusuf", "Moon")
        self.assertEqual("Yusuf", man.name)

    def test_person_is_initialized_with_office_name(self):
        man = Person("Yusuf", "Moon")
        self.assertEqual("Moon", man.office_name)

    def test_person_is_initialized_without_office_name(self):
        man = Person("Yusuf")
        self.assertEqual(None, man.office_name)

if __name__ == '__main__':
    unittest.main()
