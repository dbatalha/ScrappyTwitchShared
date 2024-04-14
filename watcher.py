import json


class Watcher:
    name = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def parse_watcher(self, json_string):
        json_watcher = json.loads(json_string)
        self.set_name(json_watcher["name"])
