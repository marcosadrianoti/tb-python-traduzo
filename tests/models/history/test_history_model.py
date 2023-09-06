import json
from src.models.history_model import HistoryModel
# from tests.models.history.conftest import prepare_base


# Req. 7
def test_request_history():
    response = json.loads(
        HistoryModel.list_as_json(),
        # https://docs.python.org/3/library/json.html
        object_hook=lambda dic: {
            key: value for key, value in dic.items() if key != "_id"
        },
    )
    expected = [
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]
    assert response == expected
