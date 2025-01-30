# Copyright (c) 2025 Louis Jouret
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from flask import Flask, request, jsonify
from app.model import load_summarizer

app = Flask(__name__)
summarizer = load_summarizer()


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return jsonify({"summary": summary[0]["summary_text"]})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
