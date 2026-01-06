#1 ทำ preprocessing สำหรับ log
import re

def clean_log(text):
    # ลบ timestamp (optional แต่แนะนำ)
    text = re.sub(r"\d{4}-\d{2}-\d{2}T.*?Z", "", text)
    # แปลง tab เป็น space
    text = text.replace("\t", " ")
    return text.strip()


#2 โหลด CSV + clean

from datasets import load_dataset

dataset = load_dataset(
    "csv",
    data_files="training_set.csv"
)["train"]

dataset = dataset.map(
    lambda x: {"text": clean_log(x["query log"])}
)

dataset = dataset.remove_columns(["query log", "status"])
dataset = dataset.rename_column("label", "labels")



#3 ทำ Tokenization
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "google-bert/bert-base-uncased"
)

def tokenize(batch):
    return tokenizer(
        batch["text"],
        padding="max_length",
        truncation=True,
        max_length=256
    )

dataset = dataset.map(tokenize, batched=True)
dataset.set_format(
    "torch",
    columns=["input_ids", "attention_mask", "labels"]
)


#4 Train / Validation Split

dataset = dataset.train_test_split(test_size=0.2, seed=42)
train_ds = dataset["train"]
val_ds = dataset["test"]



#5 โหลดโมเดลสำหรับ Binary Classification

from transformers import BertForSequenceClassification

model = BertForSequenceClassification.from_pretrained(
    "google-bert/bert-base-uncased",
    num_labels=2
)


#6 Training Configuration (เหมาะกับ Log)
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="Finetuned Bert Model",
    eval_strategy="epoch", #เลิกใช้ evaluation_strategy แล้ว
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=4,
    weight_decay=0.01,
    logging_steps=50,
    load_best_model_at_end=True,
    metric_for_best_model="f1",
    report_to="none",   # 🔴 ปิด wandb
)


#7 Metric (สำคัญมากสำหรับ Anomaly)

from sklearn.metrics import precision_recall_fscore_support, accuracy_score

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = logits.argmax(axis=1)

    precision, recall, f1, _ = precision_recall_fscore_support(
        labels, preds, average="binary"
    )
    acc = accuracy_score(labels, preds)

    return {
        "accuracy": acc,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }


#8 เริ่ม Fine-tune 🚀

from transformers import Trainer, EarlyStoppingCallback

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    eval_dataset=val_ds,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
    callbacks=[EarlyStoppingCallback(early_stopping_patience=1)]  #หยุด Train เมื่อค่า F1 ไม่ดีขึ้น
)

trainer.train()

