# Copyright (c) 2025 Louis Jouret
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from transformers import AutoTokenizer
from datasets import load_dataset


def preprocess_data(example, tokenizer, max_input=1024, max_output=150):
    """Tokenizes input and output text."""
    inputs = tokenizer(
        example["article"], max_length=max_input, truncation=True, padding="max_length")
    outputs = tokenizer(
        example["highlights"], max_length=max_output, truncation=True, padding="max_length")
    return {"input_ids": inputs["input_ids"], "labels": outputs["input_ids"]}


def load_and_preprocess_data(tokenizer_name="facebook/bart-large-cnn"):
    """Loads and preprocesses the dataset."""
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    dataset = load_dataset("cnn_dailymail", "3.0.0")

    train_data = dataset["train"].map(
        lambda x: preprocess_data(x, tokenizer), batched=True)
    test_data = dataset["test"].map(
        lambda x: preprocess_data(x, tokenizer), batched=True)

    return train_data, test_data, tokenizer
