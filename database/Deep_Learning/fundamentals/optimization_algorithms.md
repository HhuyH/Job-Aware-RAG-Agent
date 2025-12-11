---
title: Optimization Algorithms
description: Giải thích các thuật toán tối ưu hóa phổ biến trong Deep Learning, công thức toán, cơ chế hoạt động và ứng dụng thực tế.
tags: [deep-learning, fundamentals, optimization, gradient-descent, adam, sgd]
---

# Optimization Algorithms

## 1. Tóm tắt khái niệm (Definition)
Thuật toán tối ưu hóa xác định **cách cập nhật trọng số** trong quá trình huấn luyện neural network để **minimize loss function**.

---

## 2. Mục đích & khi nào dùng (Use Cases)
- Tìm minimum của hàm mất mát.  
- Cập nhật trọng số nhanh, ổn định, tránh local minima xấu.  
- Dùng cho mọi mô hình neural network: MLP, CNN, RNN, LLM.

---

## 3. Cách hoạt động bên trong (Internal Logic)

### 3.1 Gradient Descent (GD)

Cập nhật trọng số:

$$
\theta := \theta - \eta \nabla_\theta L(\theta)
$$

- \( \theta \): vector trọng số  
- \( \eta \): learning rate  
- \( \nabla_\theta L(\theta) \): gradient của loss theo trọng số

---

### 3.2 Stochastic Gradient Descent (SGD)

Cập nhật theo mini-batch hoặc từng sample:

$$
\theta := \theta - \eta \nabla_\theta L_i(\theta)
$$

- Giúp **học nhanh hơn**, thêm **ngẫu nhiên** tránh local minima.

---

### 3.3 Momentum

Thêm trọng số quán tính:

$$
v_t = \beta v_{t-1} + (1 - \beta) \nabla_\theta L(\theta)
$$

$$
\theta := \theta - \eta v_t
$$

- \( \beta \): hệ số momentum (0.9 thường dùng)  
- Giúp **hướng đi ổn định**, giảm oscillation.

---

### 3.4 Nesterov Accelerated Gradient (NAG)

Cập nhật gradient tại vị trí “ước lượng trước”:

$$
v_t = \beta v_{t-1} + (1 - \beta) \nabla_\theta L(\theta - \eta \beta v_{t-1})
$$

$$
\theta := \theta - \eta v_t
$$

- Giúp **dự đoán trước**, hội tụ nhanh hơn Momentum thông thường.

---

### 3.5 AdaGrad

Điều chỉnh learning rate theo từng parameter:

$$
G_t = G_{t-1} + (\nabla_\theta L(\theta))^2
$$

$$
\theta := \theta - \frac{\eta}{\sqrt{G_t + \epsilon}} \nabla_\theta L(\theta)
$$

- Nhạy với rare features, learning rate giảm dần cho features xuất hiện nhiều.

---

### 3.6 RMSProp

Sửa nhược điểm AdaGrad:

$$
E[g^2]_t = \beta E[g^2]_{t-1} + (1-\beta)(\nabla_\theta L(\theta))^2
$$

$$
\theta := \theta - \frac{\eta}{\sqrt{E[g^2]_t + \epsilon}} \nabla_\theta L(\theta)
$$

- \(\beta \approx 0.9\), \(\epsilon = 10^{-8}\)  
- Phổ biến cho RNN, LSTM.

---

### 3.7 Adam (Adaptive Moment Estimation)

Kết hợp Momentum + RMSProp:

$$
m_t = \beta_1 m_{t-1} + (1-\beta_1) \nabla_\theta L(\theta)
$$

$$
v_t = \beta_2 v_{t-1} + (1-\beta_2) (\nabla_\theta L(\theta))^2
$$

$$
\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}
$$

$$
\theta := \theta - \eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}
$$

- \(\beta_1 = 0.9\), \(\beta_2 = 0.999\), \(\epsilon = 10^{-8}\)  
- Rất phổ biến cho hầu hết neural network hiện đại.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

### PyTorch Example

```python
import torch
import torch.nn as nn

model = nn.Linear(3,1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
# Hoặc Adam
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
```

---

## 5. Ví dụ code (Code Examples)

```python
import torch

x = torch.randn(5,3)
y = torch.randn(5,1)
model = torch.nn.Linear(3,1)
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Forward
pred = model(x)
loss = criterion(pred, y)

# Backward + Update
loss.backward()
optimizer.step()
optimizer.zero_grad()
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Learning rate quá lớn → gradient explode.
* Learning rate quá nhỏ → hội tụ quá chậm.
* Quên zero_grad → gradient cộng dồn.
* Chọn optimizer không phù hợp cho mô hình → training chậm, không ổn định.

---

## 7. So sánh với khái niệm liên quan (Comparison)

| Optimizer      | Khi nào dùng          | Ưu điểm                | Nhược điểm                    |
| -------------- | --------------------- | ---------------------- | ----------------------------- |
| SGD            | Dữ liệu nhỏ, đơn giản | Dễ hiểu                | Chậm, oscillation             |
| SGD + Momentum | Thường xuyên          | Hội tụ nhanh hơn       | Thêm hyperparameter           |
| NAG            | Thường xuyên          | Dự đoán gradient trước | Thêm tính toán                |
| AdaGrad        | Sparse features       | LR tự điều chỉnh       | LR giảm quá nhanh             |
| RMSProp        | RNN / LSTM            | Giữ LR ổn định         | Hyperparameter cần tinh chỉnh |
| Adam           | Hầu hết NN hiện đại   | Nhanh, ổn định         | Hyperparameter cần tune       |

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Hầu hết CNN/RNN/LLM → Adam.
* Sparse features → AdaGrad hoặc RMSProp.
* Large dataset → SGD với momentum hoặc NAG.
* Tối ưu tốc độ + ổn định → Adam + LR scheduler.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Giải thích sự khác nhau giữa SGD, Momentum và NAG.
* Vì sao Adam phổ biến hơn SGD?
* Khi nào dùng RMSProp thay cho Adam?
* Các hyperparameter β1, β2, ε trong Adam có tác dụng gì?
* Tác hại của learning rate quá lớn/quá nhỏ?

---

## 10. TL;DR (Short Summary)

* Optimizer quyết định cách cập nhật trọng số.
* SGD cơ bản, thêm momentum/NAG cải thiện hội tụ.
* AdaGrad/RMSProp/Adam thích hợp cho gradient adaptive.
* Adam phổ biến nhất, kết hợp Momentum + RMSProp.
* Chọn optimizer + LR phù hợp giúp mô hình hội tụ nhanh và ổn định.