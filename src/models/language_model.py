from .abstract_model import AbstractModel
from database.db import db


# Req. 1
class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, json_data):
        super().__init__(json_data)

    # Req. 2
    def to_dict(self):
        raise NotImplementedError

    # Req. 3
    @classmethod
    def list_dicts(cls):
        raise NotImplementedError
