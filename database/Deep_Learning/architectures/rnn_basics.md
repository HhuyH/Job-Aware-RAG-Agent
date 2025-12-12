---
title: RNN Basics
description: Ghi chú cơ bản về Recurrent Neural Networks (RNN), cơ chế hoạt động, forward/backward propagation, vanishing/exploding gradient, và ứng dụng.
tags: [RNN, Recurrent Neural Network, Deep Learning, Sequence Modeling]
---

## 1. Tóm tắt khái niệm (Definition)

RNN là loại mạng neural network dùng để xử lý dữ liệu tuần tự (sequence), có khả năng ghi nhớ thông tin trước đó nhờ state (hidden layer).

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Dự đoán chuỗi thời gian (time-series forecasting).
* Xử lý ngôn ngữ tự nhiên (NLP), ví dụ text generation, sentiment analysis.
* Speech recognition.
* Khi dữ liệu có thứ tự hoặc phụ thuộc vào ngữ cảnh trước đó.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* Mỗi thời điểm t, RNN nhận input x_t và hidden state h_{t-1}.
* Hidden state được cập nhật và truyền sang bước tiếp theo.
* Forward propagation qua thời gian, backward propagation gọi là **Backpropagation Through Time (BPTT)**.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

$$
h_t = f(W_{xh} x_t + W_{hh} h_{t-1} + b_h)
$$
$$
y_t = g(W_{hy} h_t + b_y)
$$
Trong đó:

* `h_t`: hidden state tại thời điểm t
* `x_t`: input tại thời điểm t
* `y_t`: output tại thời điểm t
* `W_{xh}, W_{hh}, W_{hy}`: trọng số
* `b_h, b_y`: bias
* `f, g`: activation functions (tanh, ReLU, sigmoid, softmax)

---

## 5. Ví dụ code (Code Examples)

```python
import tensorflow as tf
from tensorflow.keras import layers, models

model = models.Sequential()
model.add(layers.SimpleRNN(50, activation='tanh', input_shape=(10, 1)))
model.add(layers.Dense(1))
model.compile(optimizer='adam', loss='mse')
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Vanishing gradient khi dùng activation nhỏ (tanh/sigmoid) trên mạng dài.
* Exploding gradient khi trọng số quá lớn.
* Cần gradient clipping hoặc LSTM/GRU để khắc phục.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* RNN vs LSTM vs GRU:

  * RNN: cơ bản, dễ bị vanishing/exploding gradient.
  * LSTM: cell state và gates, giảm vanishing gradient.
  * GRU: đơn giản hơn LSTM, vẫn giữ thông tin dài hạn.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Text generation, machine translation.
* Time-series prediction cho tài chính, khí hậu.
* Speech recognition và chatbot.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* RNN hoạt động như thế nào?
* Vanishing và exploding gradient trong RNN là gì?
* Khi nào dùng LSTM hoặc GRU thay cho RNN?
* BPTT khác gì với backpropagation bình thường?

---

## 10. TL;DR (Short Summary)

* RNN xử lý dữ liệu tuần tự, giữ hidden state để ghi nhớ thông tin trước.
* h_t = f(W_{xh} x_t + W_{hh} h_{t-1} + b_h)
* y_t = g(W_{hy} h_t + b_y)
* Vanishing/exploding gradient là vấn đề thường gặp.
* LSTM/GRU dùng để giảm vanishing gradient và học dài hạn.
