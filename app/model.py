# Copyright (c) 2025 Louis Jouret
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from transformers import pipeline


def load_summarizer(model_name="facebook/bart-large-cnn"):
    """Loads a pre-trained transformer model for summarization."""
    return pipeline("summarization", model=model_name)


# Load model
summarizer = load_summarizer()
