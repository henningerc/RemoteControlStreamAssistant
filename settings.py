import json
from data import Data
from command import Command


class Settings:
    def __init__(self, filename, dat: Data):
        self.settings = []
        dat.settings = self
        self.data: Data = dat

        self.load(filename)

    def load(self, filename):
        with open(filename, 'r') as setting_file:
            self.settings = json.load(setting_file)
            for setting in self.settings["commands"]:
                self.data.commands.append(Command(setting, self.data))

    def get(self, field):
        return self.settings[field]
