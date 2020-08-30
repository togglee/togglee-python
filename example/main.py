import time
from togglee.togglee import Togglee

url = "https://gist.githubusercontent.com/kanekotic/c469f99bef5a5c0634b4a94a4acd6546/raw/toggles"
refresh_rate_seconds = 5
default_values = {
    "prop": False
}
subject = Togglee(url, refresh_rate_seconds, default_values)
while True:
    if subject.is_enabled("prop"):
        print("do stuff")
    else:
        print("dont do stuff")
    if subject.is_enabled("prop3", {"username": "user1"}):
        print("do stuff for user 1")
    else:
        print("dont do stuff for user 1")
    if subject.is_enabled("prop3", {"username": "user2"}):
        print("do stuff for user 2")
    else:
        print("dont do stuff for user 2")
    time.sleep(7)