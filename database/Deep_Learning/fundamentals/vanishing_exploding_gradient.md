---
title: Vanishing & Exploding Gradient
description: Giải thích hiện tượng vanishing và exploding gradient trong Deep Learning, nguyên nhân, công thức toán, cách nhận biết và giải pháp.
tags: [deep-learning, fundamentals, gradient, vanishing, exploding, rnn, backpropagation]
---

# Vanishing & Exploding Gradient

## 1. Tóm tắt khái niệm (Definition)
- **Vanishing Gradient**: gradient quá nhỏ → trọng số gần như không cập nhật → mạng học chậm hoặc không học được.  
- **Exploding Gradient**: gradient quá lớn → trọng số thay đổi quá mạnh → training không ổn định hoặc NaN.

---

## 2. Mục đích & khi nào dùng (Use Cases)
- Hiểu nguyên nhân **gradient không ổn định** khi training mạng sâu hoặc RNN.  
- Ứng dụng: thiết kế network, chọn activation, weight initialization, gradient clipping.

---

## 3. Cách hoạt động bên trong (Internal Logic)

### 3.1 Gradient trong backpropagation

Với một neural network có L layer:

$$
\frac{\partial L}{\partial W^{[l]}} = \delta^{[l]} (a^{[l-1]})^T
$$

Gradient delta:

$$
\delta^{[l]} = (W^{[l+1]})^T \delta^{[l+1]} \odot f'(z^{[l]})
$$

- Nếu \( \| W^{[l]} \| < 1 \) và \( f'(z^{[l]}) < 1 \) → gradient giảm dần → **vanishing gradient**  
- Nếu \( \| W^{[l]} \| > 1 \) hoặc \( f'(z^{[l]}) > 1 \) → gradient tăng mạnh → **exploding gradient**

---

### 3.2 Ví dụ với RNN

Gradient qua time step t:

$$
\frac{\partial L}{\partial h_t} = \prod_{k=t}^{T} W^T \text{diag}(f'(h_k)) \frac{\partial L}{\partial h_T}
$$

- Multiplying nhiều ma trận với giá trị nhỏ → gradient → 0  
- Multiplying nhiều ma trận với giá trị lớn → gradient → ∞

---

## 4. Nguyên nhân
- **Activation phi tuyến**: sigmoid/tanh → f’<1  
- **Weight khởi tạo không phù hợp** → gradient giảm/explode  
- **Mạng quá sâu / RNN dài** → nhiều phép nhân ma trận liên tiếp

---

## 5. Giải pháp
- **Weight Initialization**: Xavier, He  
- **Activation function**: ReLU, Leaky ReLU thay sigmoid/tanh cho hidden layer  
- **Gradient Clipping**:

$$
\text{if } \| g \| > \tau, \quad g := g \frac{\tau}{\| g \|}
$$

- **Normalized input**: standardization / batch normalization  
- **Residual connections / LSTM / GRU**: giúp thông tin gradient truyền ổn định

---

## 6. Cấu trúc / Cú pháp (Syntax / Structure)

### PyTorch Example: Gradient Clipping

```python
import torch
import torch.nn as nn
import torch.optim as optim

model = nn.RNN(10, 20, batch_first=True)
optimizer = optim.Adam(model.parameters(), lr=0.001)

for x, y in dataloader:
    optimizer.zero_grad()
    out, _ = model(x)
    loss = criterion(out, y)
    loss.backward()
    
    # Gradient clipping
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    
    optimizer.step()
````

---

## 7. Ví dụ code (Code Examples)

```python
import torch

# Simple illustration of exploding gradient
x = torch.tensor([1.0, 2.0], requires_grad=True)
W = torch.tensor([[3.0, 4.0],[5.0, 6.0]], requires_grad=True)

y = x @ W
y = y**10  # exaggerate gradient

y.backward()
print("Gradient:", W.grad)
```

---

## 8. Lỗi thường gặp (Common Pitfalls)

* Sử dụng sigmoid/tanh cho mạng sâu → vanishing gradient
* Weight initialization quá lớn → exploding gradient
* Quên gradient clipping cho RNN → NaN trong training

---

## 9. So sánh với khái niệm liên quan (Comparison)

| Hiện tượng | Nguyên nhân      | Hậu quả                     | Giải pháp                           |
| ---------- | ---------------- | --------------------------- | ----------------------------------- |
| Vanishing  | Gradient quá nhỏ | Mạng học chậm/không học     | ReLU, He init, batch norm, residual |
| Exploding  | Gradient quá lớn | Training không ổn định, NaN | Gradient clipping, small init       |

---

## 10. Ứng dụng trong thực tế (Practical Insights)

* RNN/LSTM/GRU → luôn chuẩn hóa input + gradient clipping
* Mạng sâu CNN → He init + ReLU
* Residual connections (ResNet) giúp gradient ổn định layer sâu
* BatchNorm giúp ổn định gradient → học nhanh hơn

---

## 11. Câu hỏi phỏng vấn (Interview Questions)

* Vanishing gradient xảy ra khi nào?
* Exploding gradient có thể nhận biết như thế nào?
* Làm thế nào để giảm vanishing gradient cho RNN?
* Gradient clipping hoạt động ra sao?
* Weight initialization nào giúp tránh vanishing/exploding?

---

## 12. TL;DR (Short Summary)

* Vanishing gradient → gradient quá nhỏ, Exploding → quá lớn.
* Nguyên nhân: activation, weight init, network sâu, RNN dài.
* Giải pháp: He/Xavier init, ReLU, batch norm, residual, gradient clipping.
* Hiểu hiện tượng → thiết kế mạng ổn định, hội tụ nhanh.