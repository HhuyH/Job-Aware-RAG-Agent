---

title: Attention Mechanism Basics
description: Ghi chú cơ bản về cơ chế Attention trong deep learning, bao gồm scaled dot-product attention, multi-head attention, cơ chế self-attention và ứng dụng.
tags: [Attention, Transformer, Deep Learning, NLP, Sequence Modeling]
---------------------------------------------------------------------

## 1. Tóm tắt khái niệm (Definition)

Attention là cơ chế cho phép mô hình học cách tập trung vào những phần quan trọng của input khi dự đoán output, cải thiện hiệu suất trong xử lý chuỗi dài hoặc dữ liệu có ngữ cảnh phức tạp.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Machine translation.
* Text summarization.
* Question answering.
* Khi dữ liệu có phụ thuộc dài hạn và cần mô hình biết trọng số quan trọng cho từng phần input.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* Tạo **query (Q)**, **key (K)** và **value (V)** từ input.
* Tính attention score giữa query và key.
* Trích xuất thông tin quan trọng từ value theo trọng số attention.
* Có thể mở rộng bằng multi-head attention để học các mối quan hệ khác nhau.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

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
from tensorflow.keras import layers

# Simple scaled dot-product attention
query = tf.random.normal(shape=(1,5,64))
key = tf.random.normal(shape=(1,5,64))
value = tf.random.normal(shape=(1,5,64))
attention_output = layers.Attention()([query, value, key])
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Kích thước Q, K, V không khớp.
* Không chuẩn hóa bằng sqrt(d_k) → gradient khó ổn định.
* Không mask khi làm NLP dẫn đến leak thông tin.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* Attention vs RNN/LSTM/GRU:

  * Attention không cần tuần tự tính toán, học trực tiếp phụ thuộc toàn bộ input.
  * RNN/LSTM/GRU tuần tự, khó học phụ thuộc dài hạn.
* Multi-head attention vs single-head:

  * Multi-head học các mối quan hệ khác nhau cùng lúc.
  * Single-head học một mối quan hệ duy nhất.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Transformer architectures (BERT, GPT, etc.).
* Machine translation, text summarization, question answering.
* Image captioning và speech recognition.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Cơ chế attention hoạt động thế nào?
* Tại sao phải chia sqrt(d_k) trong scaled dot-product attention?
* Multi-head attention cải thiện gì so với single-head?
* Khi nào cần mask attention?

---

## 10. TL;DR (Short Summary)

* Attention giúp mô hình tập trung vào phần quan trọng của input.
* Công thức: Attention(Q,K,V) = softmax(Q K^T / sqrt(d_k)) V.
* Multi-head attention học nhiều mối quan hệ cùng lúc.
* Dùng rộng rãi trong NLP và các tác vụ sequence modeling.
