# Copyright (c) 2025 Louis Jouret
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from transformers import AutoModelForSeq2SeqLM, TrainingArguments, Trainer
from app.preprocess import load_and_preprocess_data

# Load preprocessed data
train_data, test_data, tokenizer = load_and_preprocess_data()

# Load model
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    save_steps=500,
    evaluation_strategy="epoch",
    save_total_limit=2
)

# Trainer setup
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
    eval_dataset=test_data
)

if __name__ == "__main__":
    trainer.train()
    model.save_pretrained("./trained_model")
    tokenizer.save_pretrained("./trained_model")
    print("Training complete! Model saved to ./trained_model")
