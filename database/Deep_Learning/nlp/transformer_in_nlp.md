---
title: Transformer in NLP
description: Ghi chú về mô hình Transformer trong NLP, bao gồm kiến trúc, cơ chế self-attention, positional encoding, ví dụ code, và ứng dụng trong các task NLP hiện đại.
tags: [Deep Learning, NLP, Transformer, Attention, Self-Attention, BERT, GPT]
---

## 1. Khái niệm

Transformer là kiến trúc mạng neural **hoàn toàn dựa trên attention**, không dùng RNN hay CNN. Nó cho phép **xử lý song song** và capture mối quan hệ từ xa trong chuỗi. Transformer là nền tảng của các mô hình NLP hiện đại như BERT, GPT, T5.

Cấu trúc cơ bản gồm:
- **Encoder**: tập hợp các lớp self-attention + feed-forward
- **Decoder**: self-attention + encoder-decoder attention + feed-forward

## 2. Mục đích & khi nào dùng (Use Cases)

- Machine Translation
- Text Summarization
- Question Answering
- Language Modeling
- Text Generation
- Chatbots

Transformer thay thế Seq2Seq truyền thống khi:
- Cần capture phụ thuộc dài
- Cần parallelizable training
- Dữ liệu lớn, cần mô hình mạnh mẽ

## 3. Cách hoạt động bên trong (Internal Logic)

### 3.1 Self-Attention
Tính trọng số giữa các token trong cùng một chuỗi:

$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V
$$

Trong đó:
- \(Q\) = Query
- \(K\) = Key
- \(V\) = Value
- \(d_k\) = chiều vector key, dùng để scale

### 3.2 Multi-Head Attention
- Chia Q, K, V thành nhiều “head” để học các mối quan hệ khác nhau
$$
\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1,...,\text{head}_h)W^O
$$
$$
\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)
$$

### 3.3 Positional Encoding
- Thêm thông tin vị trí vào embeddings vì Transformer không dùng RNN
$$
PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right)
$$
$$
PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)
$$

### 3.4 Feed-Forward & Residual
- Mỗi lớp encoder/decoder có feed-forward layer và residual connection
$$
\text{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2
$$
$$
\text{Output} = \text{LayerNorm}(x + \text{Sublayer}(x))
$$

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

Python example với `transformers` library:

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

text = "Deep Learning with Transformers"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
last_hidden_states = outputs.last_hidden_state
```

* `last_hidden_state` là embeddings contextual của từng token, có thể dùng cho downstream tasks.

## 5. Ví dụ code (Code Examples)

* Fine-tuning BERT cho text classification:

```python
from transformers import BertForSequenceClassification, Trainer, TrainingArguments

model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

training_args = TrainingArguments(
    output_dir='./results', 
    num_train_epochs=3, 
    per_device_train_batch_size=16
)

trainer = Trainer(
    model=model, 
    args=training_args, 
    train_dataset=train_dataset, 
    eval_dataset=eval_dataset
)

trainer.train()
```

## 6. Lỗi thường gặp (Common Pitfalls)

* Không xử lý tokenization đúng chuẩn (WordPiece/BPE) → lỗi embedding
* Sequence quá dài → memory overflow
* Quên positional encoding → mất thông tin thứ tự token
* Overfitting khi fine-tune với dữ liệu quá nhỏ

## 7. So sánh với khái niệm liên quan (Comparison)

| Kiến trúc           | Điểm mạnh                                   | Điểm yếu                                          |
| ------------------- | ------------------------------------------- | ------------------------------------------------- |
| RNN/Seq2Seq         | Đơn giản, dễ hiểu                           | Khó capture long-range dependency, không parallel |
| Seq2Seq + Attention | Giải quyết phụ thuộc dài                    | Không parallelizable, training chậm               |
| Transformer         | Parallelizable, capture long-range, mạnh mẽ | Cần dữ liệu & GPU lớn, phức tạp                   |

## 8. Ứng dụng trong thực tế (Practical Insights)

* Google Translate, ChatGPT, BERT, T5, GPT: tất cả dùng Transformer
* Text classification, sentiment analysis, QA, summarization
* Language modeling & text generation
* Embeddings contextual cho downstream NLP tasks

## 9. Câu hỏi phỏng vấn (Interview Questions)

1. Transformer khác RNN/Seq2Seq ở điểm gì?
2. Giải thích self-attention và multi-head attention.
3. Positional encoding dùng để làm gì?
4. Khi nào nên fine-tune pre-trained Transformer?
5. Lợi ích của residual connection trong Transformer là gì?

## 10. TL;DR (Short Summary)

Transformer là kiến trúc NLP hiện đại hoàn toàn dựa trên attention, xử lý song song, capture mối quan hệ dài hạn. Core: self-attention, multi-head attention, positional encoding, feed-forward + residual. Ứng dụng rộng rãi trong dịch máy, QA, text generation, và fine-tuning các mô hình lớn.
