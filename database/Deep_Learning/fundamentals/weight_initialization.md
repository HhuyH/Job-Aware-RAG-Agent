---
title: Weight Initialization
description: Giải thích các phương pháp khởi tạo trọng số trong neural network, công thức toán, tác động tới huấn luyện và cách áp dụng.
tags: [deep-learning, fundamentals, neural-network, weight-initialization]
---

# Weight Initialization

## 1. Tóm tắt khái niệm (Definition)
Weight initialization là quá trình **gán giá trị ban đầu cho trọng số của neural network** trước khi huấn luyện.  
Mục tiêu: **tránh gradient vanish/explode, giúp hội tụ nhanh hơn**.

---

## 2. Mục đích & khi nào dùng (Use Cases)
- Tránh **vanishing/exploding gradient**.  
- Tăng tốc hội tụ khi huấn luyện.  
- Giúp mạng học biểu diễn phi tuyến tốt hơn.  
- Dùng trước bước training, cho mọi loại layer dense, convolutional, RNN.

---

## 3. Các phương pháp phổ biến

### 3.1 Zero Initialization
```

W = 0

```
- Không nên dùng cho hidden layers → mọi neuron học giống nhau.  
- Có thể dùng cho bias.

---

### 3.2 Random Initialization
```
$$
W \sim U(-a, a) \text{ hoặc } N(0, \sigma^2)
$$

```
- Random nhỏ giúp symmetry break.  
- Chọn a hoặc σ quá lớn → gradient explode.

---

### 3.3 Xavier / Glorot Initialization
- Cho activation **tanh hoặc sigmoid**:

$$
W \sim U\left(-\sqrt{\frac{6}{n_{in} + n_{out}}}, \sqrt{\frac{6}{n_{in} + n_{out}}}\right)
$$

hoặc Gaussian:

$$
W \sim N\left(0, \frac{2}{n_{in} + n_{out}}\right)
$$

- \( n_{in} \): số neuron input  
- \( n_{out} \): số neuron output

---

### 3.4 He Initialization
- Cho activation **ReLU / Leaky ReLU**:

$$
W \sim N\left(0, \frac{2}{n_{in}}\right)
$$

hoặc Uniform:

$$
W \sim U\left(-\sqrt{\frac{6}{n_{in}}}, \sqrt{\frac{6}{n_{in}}}\right)
$$

- Giúp gradient không vanish/explode khi ReLU.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

### PyTorch Example

```python
import torch
import torch.nn as nn

layer = nn.Linear(3, 5)

# Xavier
nn.init.xavier_uniform_(layer.weight)

# He
nn.init.kaiming_normal_(layer.weight, nonlinearity='relu')

# Bias = 0
nn.init.zeros_(layer.bias)
```

---

## 5. Ví dụ code (Code Examples)

```python
import torch

# Dense layer
W = torch.empty(4,3)

# Xavier uniform
nn.init.xavier_uniform_(W)
print("Xavier init:", W)

# He normal
nn.init.kaiming_normal_(W, nonlinearity='relu')
print("He init:", W)
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Zero init hidden layer → symmetry → mọi neuron học giống nhau.
* Random init quá lớn → gradient explode.
* Chọn init không phù hợp với activation → vanishing/exploding gradient.
* Quên init bias → ảnh hưởng convergence.

---

## 7. So sánh với khái niệm liên quan (Comparison)

| Method | Activation phù hợp | Ưu điểm                            | Nhược điểm                  |
| ------ | ------------------ | ---------------------------------- | --------------------------- |
| Zero   | Bias               | Đơn giản                           | Hidden neuron giống nhau    |
| Random | Tất cả             | Break symmetry                     | Cần scale nhỏ               |
| Xavier | tanh, sigmoid      | Gradient ổn định                   | Không tốt với ReLU          |
| He     | ReLU, Leaky ReLU   | Tránh vanishing/exploding gradient | Không dùng cho tanh/sigmoid |

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Hidden layers → Xavier (tanh/sigmoid) hoặc He (ReLU).
* Bias thường khởi tạo = 0.
* Conv layers → dùng He cho ReLU.
* RNN / LSTM → Xavier cho input-hidden, He cho hidden-hidden nếu ReLU.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Vì sao không khởi tạo zero cho hidden layers?
* Khi nào dùng Xavier, khi nào dùng He?
* Random init quá lớn ảnh hưởng gì tới gradient?
* Bias có nên khởi tạo khác 0 không?
* Khởi tạo weight tốt giúp training nhanh hơn như thế nào?

---

## 10. TL;DR (Short Summary)

* Weight initialization quyết định gradient ban đầu.
* Xavier → sigmoid/tanh, He → ReLU.
* Zero init hidden layer → tránh.
* Chọn init phù hợp activation giúp mạng hội tụ nhanh, tránh vanishing/exploding gradient.


