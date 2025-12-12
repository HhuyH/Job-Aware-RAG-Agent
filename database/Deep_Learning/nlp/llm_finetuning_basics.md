---
title: LLM Fine-Tuning Basics
description: Ghi chú cơ bản về fine-tuning mô hình ngôn ngữ lớn (LLM), bao gồm các phương pháp, cơ chế, ví dụ code, và ứng dụng trong NLP.
tags: [Deep Learning, NLP, LLM, Fine-Tuning, Transfer Learning, GPT, BERT]
---

## 1. Khái niệm

Fine-tuning là quá trình **tinh chỉnh một mô hình đã được pre-trained** trên một tập dữ liệu lớn, để thích ứng với một task cụ thể. Với LLM, fine-tuning giúp mô hình:

- Dự đoán chính xác hơn trong task cụ thể
- Giảm lượng dữ liệu cần train từ đầu
- Giữ lại kiến thức ngôn ngữ chung của pre-trained model

## 2. Mục đích & khi nào dùng (Use Cases)

- Text classification
- Named Entity Recognition
- Question Answering
- Summarization
- Chatbot / Dialogue systems
- Task-specific generation (code, legal, medical text)

Fine-tuning được dùng khi:
- Có dataset nhỏ/medium nhưng muốn task-specific performance tốt
- Pre-trained LLM đã học được ngôn ngữ chung

## 3. Cách hoạt động bên trong (Internal Logic)

- Bắt đầu với pre-trained model \( \theta_{pretrained} \)
- Thêm hoặc điều chỉnh layer cuối (task-specific)
- Tối ưu hóa loss function cho task cụ thể

### 3.1 Cấu trúc loss function
Ví dụ text classification:

$$
\mathcal{L} = -\frac{1}{N} \sum_{i=1}^{N} y_i \log \hat{y}_i
$$

Với language generation:

$$
\mathcal{L} = -\sum_{t=1}^{T} \log P_\theta(y_t | y_1, ..., y_{t-1}, X)
$$

### 3.2 Phương pháp fine-tuning

- **Full fine-tuning:** cập nhật tất cả parameters
- **Adapter-based tuning:** chỉ train một module nhỏ chèn vào model
- **LoRA (Low-Rank Adaptation):** cập nhật rank thấp của weight matrices
- **Prefix-tuning / Prompt-tuning:** tinh chỉnh embeddings hoặc prefix token, giữ model frozen

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

Python example với `transformers`:

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

train_encodings = tokenizer(train_texts, truncation=True, padding=True, return_tensors="pt")
val_encodings = tokenizer(val_texts, truncation=True, padding=True, return_tensors="pt")

# Dataset class
import torch
class Dataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels
    def __len__(self):
        return len(self.labels)
    def __getitem__(self, idx):
        item = {key: val[idx] for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

train_dataset = Dataset(train_encodings, train_labels)
val_dataset = Dataset(val_encodings, val_labels)

training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    evaluation_strategy="epoch"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset
)

trainer.train()
```

## 5. Ví dụ code (Code Examples)

* Fine-tuning GPT-like model cho text generation:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

inputs = tokenizer("Example prompt", return_tensors="pt")
outputs = model(**inputs, labels=inputs["input_ids"])
loss = outputs.loss
loss.backward()
```

* Adapter / LoRA tuning: chỉ cập nhật một phần nhỏ của mô hình để tiết kiệm tài nguyên.

## 6. Lỗi thường gặp (Common Pitfalls)

* Overfitting khi dataset quá nhỏ
* Learning rate quá cao → mô hình forget knowledge cũ
* Không xử lý tokenization / padding đúng
* Không lưu checkpoints → mất tiến trình
* Gradient explosion / vanishing với các LLM quá lớn

## 7. So sánh với khái niệm liên quan (Comparison)

| Phương pháp                   | Cập nhật weights    | Resource | Pros                            | Cons                    |
| ----------------------------- | ------------------- | -------- | ------------------------------- | ----------------------- |
| Full fine-tuning              | Tất cả              | Cao      | Performance tối đa              | Dễ overfit, cần GPU lớn |
| Adapter / LoRA                | Một phần nhỏ        | Thấp     | Tiết kiệm GPU, tránh overfit    | Có thể giảm hiệu suất   |
| Prompt-tuning / Prefix-tuning | Embeddings / Prefix | Rất thấp | Dữ liệu nhỏ cũng fine-tune được | Giới hạn task-specific  |

## 8. Ứng dụng trong thực tế (Practical Insights)

* Fine-tune BERT/GPT cho classification, QA, summarization
* LoRA / Adapter tuning dùng trong sản xuất vì tiết kiệm GPU
* ChatGPT + prompt-tuning để tùy chỉnh nhiệm vụ mà không thay đổi weights
* Tích hợp LLM trong sản phẩm: search, recommendation, code generation

## 9. Câu hỏi phỏng vấn (Interview Questions)

1. Fine-tuning là gì? Tại sao cần fine-tuning LLM?
2. So sánh full fine-tuning, adapter, LoRA, prompt-tuning
3. Loss function khi fine-tune LM khác classification như thế nào?
4. Làm sao tránh overfitting khi dataset nhỏ?
5. Khi nào nên giữ model frozen và chỉ fine-tune prefix/adapters?

## 10. TL;DR (Short Summary)

Fine-tuning LLM là tinh chỉnh mô hình pre-trained cho task cụ thể. Phương pháp phổ biến: full fine-tuning, adapter, LoRA, prompt-tuning. Giúp đạt hiệu suất task-specific, tiết kiệm tài nguyên và tận dụng kiến thức ngôn ngữ chung.
