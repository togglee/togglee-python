from unittest import TestCase
from faker import Faker
from togglee import Togglee

fake = Faker()

class ToggleTest(TestCase):
    def test_use_default_toggles(self):
        prop_True = fake.pystr()
        prop_False = fake.pystr()
        expected = fake.pystr()
        fakeDict =	{
            prop_True: True,
            prop_False: False
        }
        subject = Togglee(fake.pystr(), fake.pyint(), fakeDict)
        assert subject.isEnabled(prop_True) == True
        assert subject.isEnabled(prop_False) == False