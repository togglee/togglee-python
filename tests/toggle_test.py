from unittest import TestCase
from faker import Faker
from togglee import Togglee

fake = Faker()

class ToggleTest(TestCase):
    def test_use_default_toggles(self):
        prop_True = fake.pystr()
        prop_False = fake.pystr()
        fakeDict =	{
            prop_True: True,
            prop_False: False
        }
        subject = Togglee(fake.pystr(), fake.pyint(), fakeDict)
        assert subject.isEnabled(prop_True) == True
        assert subject.isEnabled(prop_False) == False

    def test_return_false_as_default(self):
        prop = fake.pystr()
        subject = Togglee(fake.pystr(), fake.pyint(), {})
        assert subject.isEnabled(prop) == False

    def test_return_false_if_no_defaults(self):
        prop = fake.pystr()
        subject = Togglee(fake.pystr(), fake.pyint(), None)
        assert subject.isEnabled(prop) == False