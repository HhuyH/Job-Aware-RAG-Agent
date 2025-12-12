---
title: LSTM Basics
description: Ghi chú chi tiết về Long Short-Term Memory (LSTM), cơ chế hoạt động, các gate, forward/backward propagation, vanishing gradient và ứng dụng.
tags: [LSTM, RNN, Deep Learning, Sequence Modeling, Neural Network]
---

## 1. Tóm tắt khái niệm (Definition)

LSTM là loại RNN đặc biệt, được thiết kế để giải quyết vấn đề vanishing gradient, cho phép học các phụ thuộc dài hạn trong dữ liệu tuần tự nhờ **cell state** và các **gate**.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Dự đoán chuỗi thời gian dài.
* Machine translation, text generation.
* Speech recognition.
* Khi RNN cơ bản gặp khó khăn với dữ liệu có phụ thuộc dài hạn.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* **Cell state (c_t)**: giữ thông tin dài hạn.
* **Forget gate**: quyết định thông tin nào giữ lại hoặc loại bỏ.
* **Input gate**: quyết định thông tin nào thêm vào cell state.
* **Output gate**: quyết định thông tin nào đưa ra hidden state.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

$$
f_t = \sigma(W_f x_t + U_f h_{t-1} + b_f)
$$
$$
i_t = \sigma(W_i x_t + U_i h_{t-1} + b_i)
$$
$$
\tilde{c}*t = \tanh(W_c x_t + U_c h*{t-1} + b_c)
$$
$$
c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}*t
$$
$$
o_t = \sigma(W_o x_t + U_o h*{t-1} + b_o)
$$
$$
h_t = o_t \odot \tanh(c_t)
$$

---

## 5. Ví dụ code (Code Examples)

```python
import tensorflow as tf
from tensorflow.keras import layers, models

model = models.Sequential()
model.add(layers.LSTM(50, activation='tanh', input_shape=(10,1)))
model.add(layers.Dense(1))
model.compile(optimizer='adam', loss='mse')
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Vanishing gradient nếu thiết kế RNN sâu hoặc dùng activation không hợp lý.
* Exploding gradient nếu trọng số quá lớn.
* Quên chuẩn hóa input hoặc không dùng dropout gây overfitting.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* LSTM vs RNN vs GRU:

  * RNN: đơn giản nhưng dễ vanishing gradient.
  * LSTM: cell state và gate, giảm vanishing gradient, học dài hạn.
  * GRU: đơn giản hơn LSTM, vẫn giữ thông tin dài hạn.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Text generation và machine translation.
* Speech recognition và chatbot.
* Time-series prediction dài hạn như tài chính, khí hậu.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* LSTM hoạt động như thế nào?
* Các gate trong LSTM có chức năng gì?
* LSTM giải quyết vanishing gradient thế nào?
* Khi nào chọn GRU thay vì LSTM?

---

## 10. TL;DR (Short Summary)

* LSTM là RNN cải tiến với cell state và gate để học dài hạn.
* Công thức cơ bản: f_t, i_t, o_t, c_t, h_t.
* Giảm vanishing gradient, học được phụ thuộc dài hạn.
* Dùng trong text generation, machine translation, speech recognition.
