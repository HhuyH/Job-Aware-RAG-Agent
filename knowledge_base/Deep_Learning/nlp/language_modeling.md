---
title: Language Modeling in NLP
description: Ghi chú về Language Modeling trong NLP, bao gồm khái niệm, các loại mô hình, công thức xác suất, ví dụ code, và ứng dụng trong dự đoán từ, sinh văn bản, và các mô hình ngôn ngữ lớn.
tags: [Deep Learning, NLP, Language Modeling, LM, RNN, LSTM, Transformer, GPT, BERT]
---

## 1. Khái niệm

Language Modeling (LM) là bài toán dự đoán xác suất của một chuỗi từ trong ngôn ngữ. Mục tiêu là **dự đoán từ tiếp theo** dựa trên các từ trước đó:

$$
P(w_1, w_2, ..., w_T) = \prod_{t=1}^{T} P(w_t | w_1, ..., w_{t-1})
$$

LM là nền tảng của hầu hết các task NLP như text generation, machine translation, và speech recognition.

## 2. Mục đích & khi nào dùng (Use Cases)

- Dự đoán từ tiếp theo (next-word prediction)
- Sinh văn bản tự động (text generation)
- Chatbot & dialogue systems
- Machine Translation (seq2seq + LM)
- Pre-training cho các mô hình LLM (BERT, GPT)

## 3. Cách hoạt động bên trong (Internal Logic)

### 3.1 N-gram Language Model
Dựa trên xác suất có điều kiện:

$$
P(w_t | w_1, ..., w_{t-1}) \approx P(w_t | w_{t-(n-1)}, ..., w_{t-1})
$$

- Ưu điểm: đơn giản, dễ hiểu
- Nhược điểm: không capture phụ thuộc dài, sparse data

### 3.2 Neural Language Model
- Dùng embedding và mạng neural (RNN, LSTM, GRU, Transformer) để dự đoán từ tiếp theo.
- Với RNN/LSTM:

$$
h_t = f(h_{t-1}, x_t)
$$
$$
P(w_t | w_1, ..., w_{t-1}) = \text{softmax}(Wh_t + b)
$$

### 3.3 Transformer-based LM
- Dùng self-attention để capture long-range dependency
- Ví dụ GPT:

$$
P(w_t | w_1, ..., w_{t-1}) = \text{softmax}(W \cdot \text{TransformerLayer}(w_1,...,w_{t-1}))
$$

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

Python example với `transformers`:

```python
from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

input_text = "Deep learning is"
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs, max_length=20)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)
```

## 5. Ví dụ code (Code Examples)

* N-gram LM với NLTK:

```python
import nltk
from nltk.util import ngrams
from collections import Counter

text = "deep learning is fun"
tokens = nltk.word_tokenize(text)
bigrams = list(ngrams(tokens, 2))
bigram_counts = Counter(bigrams)
print(bigram_counts)
```

* RNN Language Model (PyTorch):

```python
import torch
import torch.nn as nn

class RNNLM(nn.Module):
    def __init__(self, vocab_size, embed_size, hidden_size):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_size)
        self.rnn = nn.LSTM(embed_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, x, hidden=None):
        x = self.embed(x)
        out, hidden = self.rnn(x, hidden)
        out = self.fc(out)
        return out, hidden
```

## 6. Lỗi thường gặp (Common Pitfalls)

* OOV (out-of-vocabulary) words: cần xử lý tokenization, subword (BPE, WordPiece)
* Không padding hoặc batch sequence đúng → lỗi khi training
* Sequence quá dài → gradient vanishing/exploding với RNN
* Overfitting khi dữ liệu nhỏ

## 7. So sánh với khái niệm liên quan (Comparison)

| Kiểu LM                | Điểm mạnh                                     | Điểm yếu                                    |
| ---------------------- | --------------------------------------------- | ------------------------------------------- |
| N-gram                 | Đơn giản, dễ tính toán                        | Sparse, không capture long-range dependency |
| RNN/LSTM/GRU           | Capture phụ thuộc dài hơn N-gram              | Khó parallel, training chậm                 |
| Transformer (GPT/BERT) | Parallelizable, capture long-range dependency | Cần nhiều dữ liệu & GPU                     |

## 8. Ứng dụng trong thực tế (Practical Insights)

* Chatbot: dự đoán câu trả lời tiếp theo
* Text generation: sinh bài viết, code, email
* Machine Translation: kết hợp LM để sinh output trơn tru
* Pre-training: BERT/GPT dùng LM để học contextual embeddings

## 9. Câu hỏi phỏng vấn (Interview Questions)

1. Language Modeling là gì? Công thức xác suất tổng quát?
2. So sánh N-gram, RNN LM, Transformer LM
3. Gradient vanishing/exploding trong RNN LM xảy ra khi nào?
4. Subword tokenization là gì? Tại sao cần?
5. Ứng dụng LM trong pre-training LLM?

## 10. TL;DR (Short Summary)

Language Modeling dự đoán xác suất từ tiếp theo dựa trên context. Các phương pháp: N-gram, RNN/LSTM, Transformer. Là nền tảng của text generation, chatbot, machine translation, và pre-training cho LLM.
