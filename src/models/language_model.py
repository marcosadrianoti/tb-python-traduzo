from .abstract_model import AbstractModel
from database.db import db


# Req. 1
class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, json_data):
        super().__init__(json_data)
        self.data = json_data

    # Req. 2
    def to_dict(self):
        return {
            'name': self.data['name'],
            'acronym': self.data['acronym']
        }

    # Req. 3
    @classmethod
    def list_dicts(cls):
        languages = cls._collection.find()
        return [language for language in languages]
