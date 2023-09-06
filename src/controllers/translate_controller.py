from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template(
            "index.html",
            languages=LanguageModel.find(),
            text_to_translate="O que deseja traduzir",
            translate_from="pt",
            translate_to="en",
            translated="Tradução",
        )
    elif request.method == "POST":
        form_text_to_translate = request.form.get("text-to-translate")
        form_translate_from = request.form.get("translate-from")
        form_translate_to = request.form.get("translate-to")

        return render_template(
            "index.html",
            languages=LanguageModel.find(),
            text_to_translate=form_text_to_translate,
            translate_from=form_translate_from,
            translate_to=form_translate_to,
            translated=GoogleTranslator(
                source=form_translate_from, target=form_translate_to
            ).translate(form_text_to_translate),
        )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    raise NotImplementedError
