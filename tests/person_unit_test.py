import unittest
from .context import Person

class TestPerson(unittest.TestCase):
 
    def test_person_is_initialized_with_name(self):
        man = Person("Yusuf", "Fellow")
        self.assertEqual("Yusuf", man.name)

    def test_person_is_initialized_with_status(self):
        man = Person("Yusuf", "Fellow")
        self.assertEqual("Fellow", man.status)

if __name__ == '__main__':
    unittest.main()
