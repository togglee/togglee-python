class Togglee:
    def __init__(self, url: str, refresh_rate: int, defaults: dict):
        self.url = url
        self.refresh_rate = refresh_rate
        self.toggles = defaults
    
    def isEnabled(self, prop: str):
        if self.toggles is not None and prop in self.toggles:
            return self.toggles[prop]
        else:
            return False