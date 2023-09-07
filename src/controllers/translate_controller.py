from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


def save_history(text_to_translate, translate_from, translated):
    HistoryModel(
        {
            "text_to_translate": text_to_translate,
            "translate_from": translate_from,
            "translated": translated,
        }
    ).save()


def render(
    form_text_to_translate,
    form_translate_from,
    form_translate_to,
    form_translated,
):
    return render_template(
        "index.html",
        languages=LanguageModel.find(),
        text_to_translate=form_text_to_translate,
        translate_from=form_translate_from,
        translate_to=form_translate_to,
        translated=form_translated,
    )


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render("O que deseja traduzir", "pt", "en", "Tradução")
    elif request.method == "POST":
        form_text_to_translate = request.form.get("text-to-translate")
        form_translate_from = request.form.get("translate-from")
        form_translate_to = request.form.get("translate-to")
        form_translated = GoogleTranslator(
            source=form_translate_from, target=form_translate_to
        ).translate(form_text_to_translate)
        save_history(
            form_text_to_translate, form_translate_from, form_translated
        )
        return render(
            form_text_to_translate,
            form_translate_from,
            form_translate_to,
            form_translated,
        )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    form_text_to_translate = request.form.get("text-to-translate")
    form_translate_from = request.form.get("translate-from")
    form_translate_to = request.form.get("translate-to")
    form_translated = GoogleTranslator(
        source=form_translate_from, target=form_translate_to
    ).translate(form_text_to_translate)
    return render(
            form_text_to_translate,
            form_translate_to,
            form_translate_from,
            form_translated,
        )
