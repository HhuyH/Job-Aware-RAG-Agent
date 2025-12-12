---
title: Transformer Architecture Basics
description: Ghi chú chi tiết về kiến trúc Transformer, cơ chế self-attention, multi-head attention, positional encoding và ứng dụng trong NLP và sequence modeling.
tags: [Transformer, Attention, Deep Learning, NLP, Sequence Modeling]
---

## 1. Tóm tắt khái niệm (Definition)

Transformer là kiến trúc mạng neural dựa trên cơ chế attention, thay thế RNN/LSTM cho các tác vụ xử lý chuỗi. Nó sử dụng **self-attention** và **multi-head attention** để học các phụ thuộc dài hạn mà không cần tuần tự tính toán.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Machine translation.
* Text summarization và question answering.
* Sequence modeling dài hạn.
* Khi muốn xử lý song song, tăng tốc training so với RNN/LSTM.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* **Input embedding**: ánh xạ token thành vector.
* **Positional encoding**: cung cấp thông tin vị trí trong chuỗi.
* **Encoder layer**: gồm multi-head self-attention + feed-forward + residual + normalization.
* **Decoder layer**: tương tự encoder, thêm masked self-attention và encoder-decoder attention.
* Output từ decoder được ánh xạ ra từ vựng qua softmax.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

Positional encoding:
$$
PE_{(pos, 2i)} = \sin(pos / 10000^{2i/d_{model}})
$$
$$
PE_{(pos, 2i+1)} = \cos(pos / 10000^{2i/d_{model}})
$$

Scaled dot-product attention:
$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V
$$

Multi-head attention:
$$
\text{MultiHead}(Q,K,V) = \text{Concat}(head_1, ..., head_h) W^O
$$
$$
head_i = \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)
$$

---

## 5. Ví dụ code (Code Examples)

```python
import tensorflow as tf
from tensorflow.keras import layers, models

inputs = tf.keras.Input(shape=(None, 512))
attention_output = layers.MultiHeadAttention(num_heads=8, key_dim=64)(inputs, inputs)
model = models.Model(inputs=inputs, outputs=attention_output)
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Kích thước Q, K, V không khớp.
* Quên positional encoding → mô hình không phân biệt vị trí.
* Gradient instability khi không chuẩn hóa hoặc learning rate quá cao.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* Transformer vs RNN/LSTM:

  * Transformer: parallelizable, học phụ thuộc dài hạn hiệu quả.
  * RNN/LSTM: tuần tự, khó học phụ thuộc dài hạn.
* Encoder-decoder vs encoder-only vs decoder-only:

  * Encoder-decoder: dịch thuật, seq2seq.
  * Encoder-only: BERT, classification.
  * Decoder-only: GPT, text generation.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Machine translation (Google Translate).
* Pretrained NLP models: BERT, GPT, T5.
* Text summarization, question answering.
* Sequence prediction trong time-series, speech, hoặc music generation.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Transformer khác RNN/LSTM thế nào?
* Self-attention và multi-head attention hoạt động ra sao?
* Positional encoding có tác dụng gì?
* Khi nào dùng encoder-only, decoder-only hoặc encoder-decoder?

---

## 10. TL;DR (Short Summary)

* Transformer dựa trên attention, thay RNN/LSTM, parallelizable.
* Công thức cơ bản: Positional encoding, scaled dot-product attention, multi-head attention.
* Dùng trong machine translation, text generation, NLP tasks.
