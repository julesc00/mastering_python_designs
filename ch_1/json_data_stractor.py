import json


class JSONDATAExtractor:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        """
        This function extracts data from json file
        :return: data
        """
        return self.data
