from flask.testing import FlaskClient
from parsel import Selector
from src.models.language_model import LanguageModel


def test_request_translate(app_test: FlaskClient):
    response = app_test.get("/")
    assert "O que deseja traduzir" in response.text
    assert "Tradução" in response.text
    assert "ENGLISH" in response.text
    assert "AFRIKAANS" in response.text
    assert "MOUSE" not in response.text

    selector = Selector(text=response.text)

    total_options = selector.css("option")
    assert len(total_options) == len(LanguageModel.find()) * 2

    selected_option_from = selector.css(
        'select[name="translate-from"] option[selected]::attr(value)'
    ).get()
    assert selected_option_from is not None

    selected_option_to = selector.css(
        'select[name="translate-to"] option[selected]::attr(value)'
    ).get()
    assert selected_option_to is not None


def test_post_translate(app_test: FlaskClient):
    response = app_test.post(
        "/",
        data={
            "text-to-translate": "Hello, I like videogame",
            "translate-from": "en",
            "translate-to": "pt",
        },
    )
    assert "Olá, eu gosto de videogame" in response.text


def test_post_reverse(app_test: FlaskClient):
    response = app_test.post(
        "/reverse",
        data={
            "text-to-translate": "Hello, I like videogame",
            "translate-from": "en",
            "translate-to": "pt",
        },
    )

    content_html = response.text

    assert "Olá, eu gosto de videogame" in content_html

    selected_option_to = (
        Selector(text=content_html)
        .css('select[name="translate-to"] option[selected]::attr(value)')
        .get()
    )

    assert selected_option_to == "en"

    selected_option_from = (
        Selector(text=content_html)
        .css('select[name="translate-from"] option[selected]::attr(value)')
        .get()
    )
    assert selected_option_from == "pt"
