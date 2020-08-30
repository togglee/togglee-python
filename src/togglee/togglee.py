import threading
import time

import requests

from togglee.helpers.mappers import map_json_to_toggles
from togglee.strategies.main import strategy_maps


class Togglee:
    def __init__(self, url: str, refresh_rate: int, defaults: dict):
        self._url = url
        self._refresh_rate = refresh_rate
        self._toggles = defaults
        self._thread = threading.Thread(target=self._scheduler_event)
        self._thread.start()

    def is_enabled(self, prop: str, context=None):
        return self._get_value(prop, context) if self._toggles is not None and prop in self._toggles else False

    def _get_value(self, prop, context):
        toggle = self._toggles[prop]
        return strategy_maps[toggle['type']](toggle, context)

    def _scheduler_event(self):
        self._refresh_toggles()
        while True:
            time.sleep(self._refresh_rate)
            self._refresh_toggles()

    def _refresh_toggles(self):
        try:
            response = requests.get(self._url)
            self._toggles = map_json_to_toggles(response.json())
        except Exception as e:
            print("unable to retrieve value", e)
