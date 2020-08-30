from unittest import TestCase
import responses

from faker import Faker
from togglee.togglee import Togglee
import time

fake = Faker()


class ToggleTest(TestCase):
    def test_use_default_toggles(self):
        url = fake.url()
        fakeDict = {
            "prop_True": {
                "type": "release",
                "value": True
            },
            "prop_False": {
                "type": "release",
                "value": False
            }
        }
        subject = Togglee(url, 100, fakeDict)
        assert subject.is_enabled("prop_True")
        assert not subject.is_enabled("prop_False")


    def test_return_false_as_default(self):
        prop = fake.pystr()
        subject = Togglee(fake.url(), fake.pyint(), {})
        assert not subject.is_enabled(prop)


    def test_return_false_if_no_defaults(self):
        prop = fake.pystr()
        subject = Togglee(fake.url(), fake.pyint(), None)
        assert not subject.is_enabled(prop)


    @responses.activate
    def test_refresh_cache_in_rate(self):
        url = fake.url()

        fakeDict = {
            "toggles": [
                {
                    "name": "prop_True",
                    "type": "release",
                    "value": True
                },
                {
                    "name": "prop_False",
                    "type": "release",
                    "value": False
                }
            ]
        }
        responses.add(responses.GET, url,
                      json=fakeDict, status=200)
        subject = Togglee(url, 1, {})
        time.sleep(5)
        assert subject.is_enabled("prop_True")
        assert not subject.is_enabled("prop_False")
