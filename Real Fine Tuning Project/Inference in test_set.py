import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch
import re

#อ่านไฟล์จาก test_set.csv
df = pd.read_csv('test_set.csv')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

#โหลด Model
path = 'Finetuned Bert Model\checkpoint-60000'
tokenizer = AutoTokenizer.from_pretrained(path)
model = AutoModelForSequenceClassification.from_pretrained(path)
model.to(device)
model.eval()

def clean_log(text):
    # ลบ timestamp (optional แต่แนะนำ)
    text = re.sub(r"\d{4}-\d{2}-\d{2}T.*?Z", "", text)
    # แปลง tab เป็น space
    text = text.replace("\t", " ")
    return text.strip()

def predict_log(log_text):
    log_text = clean_log(log_text)
    inputs = tokenizer(
        log_text,
        return_tensors="pt",
        truncation=True,
        padding=True, # ใส่เผื่อเอาไว้ตอน inference มากกว่า 1 log (Batch Size > 1)
        max_length=128
    )
    # ⭐ ย้าย input ไป GPU
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        logits = model(**inputs).logits
        pred = torch.argmax(logits, dim=1).item()

    return "normal" if pred == 1 else "anomaly"

#วัด Accuracy

correct_predictions = 0
total_predictions = len(df)

for index, row in df.iterrows():
    text_to_classify = row['query log'] # ใช้คอลัมน์ 'query log' เป็น input
    true_label = row['status'] # ใช้คอลัมน์ 'status' เป็นคำตอบจริง (normal หรือ anomaly)

    # ทำนาย
    prediction_result = predict_log(text_to_classify)

    # ตรวจสอบว่าทำนายถูกต้องหรือไม่
    if prediction_result == true_label:
        correct_predictions += 1

# วัด Accuracy
accuracy = (correct_predictions / total_predictions) * 100
print(f"test_set จำนวน {total_predictions}")
print(f"ทำนายถูกจำนวน {correct_predictions}")
print(f"Accuracy = {accuracy}")
