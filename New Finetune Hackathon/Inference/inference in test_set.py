import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

#อ่านไฟล์จาก test_set.csv

df = pd.read_csv('test set.csv')
df.head(5)


#โหลด Model
path = "D:/New Finetune Hackathon/Finetuned Bert Model State 2/checkpoint-78"
tokenizer = AutoTokenizer.from_pretrained(path)
model = AutoModelForSequenceClassification.from_pretrained(path)


# ตรวจสอบว่ามี GPU ให้ใช้งานหรือไม่ ถ้ามีให้ใช้ cuda ถ้าไม่มีให้ใช้ cpu
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#บังคับว่าต้อง inference ที่ GPU (ถ้ามี)
model.to(device)
model.eval()


#1 ทำ preprocessing สำหรับ log (For Model Stage 2)

def add_prefix_token(text): # log data ต้องผ่าน code นี้ก่อน training / inference
    # clean log
    text = text.replace("\t", " ")
    text = text.strip()
    # add token
    if text[0].isalpha() or text[3].isalpha():
        return "[SQL]\n" + text
    else:
        return "[LOG]\n" + text
    
def predict_log(log_text):
    log_text = add_prefix_token(log_text)
    inputs = tokenizer(
        log_text,
        return_tensors="pt",
        truncation=True,
        padding=True, # ใส่เผื่อเอาไว้ตอน inference มากกว่า 1 log (Batch Size > 1)
        max_length=128
    )

    with torch.no_grad():
        logits = model(**inputs).logits
        pred = torch.argmax(logits, dim=1).item()
        prob = torch.softmax(logits, dim=-1).tolist()[0]

    return "NORMAL" if pred == 1 else "ANOMALY" ,prob


#วัด Accuracy

correct_predictions = 0
total_predictions = len(df)

for index,row in df.iterrows():
    text_to_classify = row['query log'] # ใช้คอลัมน์ 'query log' เป็น input
    true_label = row['status'] # ใช้คอลัมน์ 'status' เป็นคำตอบจริง (normal หรือ anomaly)

    # ทำนาย
    prediction_result,confidence = predict_log(text_to_classify)

    # ตรวจสอบว่าทำนายถูกต้องหรือไม่
    if prediction_result == true_label:
        correct_predictions += 1
        correction = 'True'
    else:
        correction = 'False'
    print(f"prediction = {prediction_result} | true_status = {true_label} | correction = {correction} | confidence = {confidence}")


# วัด Accuracy
accuracy = (correct_predictions / total_predictions) * 100
print(f"test_set จำนวน {total_predictions}")
print(f"ทำนายถูกจำนวน {correct_predictions}")
print(f"Accuracy = {accuracy}")