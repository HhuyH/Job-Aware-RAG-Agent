---
title: GRU Basics
description: Ghi chú chi tiết về Gated Recurrent Unit (GRU), cơ chế hoạt động, các gate, forward/backward propagation, vanishing gradient và ứng dụng.
tags: [GRU, RNN, Deep Learning, Sequence Modeling, Neural Network]
---

## 1. Tóm tắt khái niệm (Definition)

GRU là biến thể của RNN, giống LSTM nhưng đơn giản hơn, kết hợp **update gate** và **reset gate** để kiểm soát luồng thông tin, giúp giảm vanishing gradient và học các phụ thuộc dài hạn.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Dự đoán chuỗi thời gian.
* NLP: text generation, sentiment analysis.
* Speech recognition.
* Khi cần mạng tuần tự đơn giản hơn LSTM nhưng vẫn học được thông tin dài hạn.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* **Update gate (z_t)**: quyết định bao nhiêu thông tin cũ giữ lại.
* **Reset gate (r_t)**: quyết định thông tin cũ nào sẽ bỏ khi tạo candidate hidden state.
* **Candidate hidden state (\tilde{h}_t)** kết hợp input hiện tại và hidden state trước.
* Hidden state mới h_t được tính từ update gate và candidate hidden state.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

$$
z_t = \sigma(W_z x_t + U_z h_{t-1} + b_z)
$$
$$
r_t = \sigma(W_r x_t + U_r h_{t-1} + b_r)
$$
$$
\tilde{h}*t = \tanh(W_h x_t + U_h (r_t \odot h*{t-1}) + b_h)
$$
$$
h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t
$$

---

## 5. Ví dụ code (Code Examples)

```python
import tensorflow as tf
from tensorflow.keras import layers, models

model = models.Sequential()
model.add(layers.GRU(50, activation='tanh', input_shape=(10,1)))
model.add(layers.Dense(1))
model.compile(optimizer='adam', loss='mse')
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Vanishing/exploding gradient khi mạng quá sâu.
* Quên chuẩn hóa input gây học chậm hoặc không ổn định.
* Không dùng dropout gây overfitting.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* GRU vs RNN vs LSTM:

  * RNN: đơn giản, dễ vanishing gradient.
  * LSTM: phức tạp, có cell state và 3 gate, giảm vanishing gradient.
  * GRU: đơn giản hơn LSTM, 2 gate, học dài hạn, nhanh hơn.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Time-series prediction.
* Text generation và NLP tasks.
* Speech recognition.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* GRU hoạt động như thế nào?
* Update gate và reset gate chức năng gì?
* Khi nào chọn GRU thay vì LSTM?
* GRU giúp giải quyết vanishing gradient ra sao?

---

## 10. TL;DR (Short Summary)

* GRU là RNN cải tiến với update và reset gate.
* Công thức: z_t, r_t, \tilde{h}_t, h_t.
* Giảm vanishing gradient, học được thông tin dài hạn.
* Đơn giản hơn LSTM, dùng trong time-series, NLP, speech recognition.
