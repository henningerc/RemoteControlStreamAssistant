import json


class Settings:
    def __init__(self, filename):
        self.settings = []
        self.load(filename)
        pass

    def load(self, filename):
        with open(filename, 'r') as setting_file:
            self.settings = json.load(setting_file)

    def get(self, field):
        return self.settings[field]
