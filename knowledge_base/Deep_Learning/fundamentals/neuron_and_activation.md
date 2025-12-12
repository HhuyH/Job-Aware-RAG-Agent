---
title: Neurons & Activation Functions
description: Giải thích cơ chế hoạt động của neuron, các hàm kích hoạt phổ biến trong Deep Learning, công thức và ứng dụng.
tags: [deep-learning, fundamentals, neuron, activation-functions]
---

# Neurons & Activation Functions

## 1. Tóm tắt khái niệm (Definition)
- **Neuron**: đơn vị cơ bản của neural network, tính tổng có trọng số các input và áp dụng hàm kích hoạt để ra output.
- **Activation function**: hàm phi tuyến áp dụng lên đầu ra neuron, giúp mạng học được các biểu diễn phi tuyến.

---

## 2. Mục đích & khi nào dùng (Use Cases)
- Giúp mạng học được **phi tuyến**, mở rộng khả năng biểu diễn.  
- Quyết định output neuron trong từng layer.  
- Ứng dụng: CNN, RNN, Transformer, LLM, bất kỳ mạng deep learning nào.

---

## 3. Cách hoạt động bên trong (Internal Logic)

Neuron tính toán:

$$
z = w_1 x_1 + w_2 x_2 + \dots + w_n x_n + b
$$

Output sau hàm kích hoạt:

$$
a = f(z)
$$

---

## 4. Các hàm kích hoạt phổ biến

### 4.1 Sigmoid

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

- Output trong [0, 1].  
- Nhạy với gradient nhỏ khi $|z|$ lớn → vanishing gradient.

---

### 4.2 Tanh

$$
\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}
$$

- Output trong [-1, 1].  
- Zero-centered, thường tốt hơn sigmoid.

---

### 4.3 ReLU (Rectified Linear Unit)

$$
\text{ReLU}(z) = \max(0, z)
$$

- Nhanh, đơn giản, tránh vanishing gradient cho positive z.  
- Nhược điểm: “dying ReLU” khi gradient luôn = 0.

---

### 4.4 Leaky ReLU

$$
\text{LeakyReLU}(z) =
\begin{cases}
z & z > 0 \\
\alpha z & z \le 0
\end{cases}
$$

- Khắc phục dying ReLU, với $\alpha \approx 0.01$.

---

### 4.5 Softmax (multi-class output)

$$
\text{softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{C} e^{z_j}}
$$

- Dùng ở layer output multi-class classification.  
- Output là xác suất phân phối trên các lớp.

---

## 5. Cấu trúc / Cú pháp (Syntax / Structure)

### PyTorch Example

```python
import torch
import torch.nn as nn

# Sigmoid
activation = nn.Sigmoid()

# Tanh
activation = nn.Tanh()

# ReLU
activation = nn.ReLU()

# Leaky ReLU
activation = nn.LeakyReLU(0.01)

# Softmax (dim=1 cho multi-class)
activation = nn.Softmax(dim=1)
````

---

## 6. Ví dụ code (Code Examples)

```python
import torch

x = torch.tensor([-1.0, 0.0, 1.0, 2.0])

# Sigmoid
a = torch.sigmoid(x)

# ReLU
b = torch.relu(x)

# Tanh
c = torch.tanh(x)

print(a, b, c)
```

---

## 7. Lỗi thường gặp (Common Pitfalls)

* Chọn sigmoid/tanh cho mạng quá sâu → vanishing gradient.
* ReLU chết neuron (dying ReLU) khi LR quá cao.
* Softmax dùng nhầm ở hidden layer → không chuẩn.
* Không chuẩn hóa input → gradient không ổn định.

---

## 8. So sánh với khái niệm liên quan (Comparison)

| Activation | Output       | Ưu điểm                 | Nhược điểm            |
| ---------- | ------------ | ----------------------- | --------------------- |
| Sigmoid    | [0,1]        | Đơn giản                | Vanishing gradient    |
| Tanh       | [-1,1]       | Zero-centered           | Vanishing gradient    |
| ReLU       | [0, ∞)       | Nhanh, gradient ổn định | Dying ReLU            |
| Leaky ReLU | (-∞, ∞)      | Tránh dying ReLU        | Thêm α hyperparameter |
| Softmax    | [0,1], sum=1 | Xác suất multi-class    | Chỉ output layer      |

---

## 9. Ứng dụng trong thực tế (Practical Insights)

* Hidden layer: ReLU hoặc Leaky ReLU.
* Output binary classification: Sigmoid.
* Output multi-class classification: Softmax.
* LSTM/GRU: Sigmoid/Tanh để điều khiển gate.
* Zero-centered activations giúp mạng học ổn định hơn.

---

## 10. Câu hỏi phỏng vấn (Interview Questions)

* Vì sao cần activation function phi tuyến?
* Dùng sigmoid vs tanh, khi nào?
* ReLU có nhược điểm gì?
* Softmax dùng thế nào cho multi-class?
* Khắc phục dying ReLU bằng cách nào?

---

## 11. TL;DR (Short Summary)

* Neuron: tổng trọng số + bias → áp dụng activation.
* Sigmoid/Tanh: output giới hạn, vanishing gradient.
* ReLU/Leaky ReLU: nhanh, gradient ổn định, phổ biến cho hidden layer.
* Softmax: multi-class output.
* Chọn activation phù hợp layer và bài toán.

```
