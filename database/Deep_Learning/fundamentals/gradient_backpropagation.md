---
title: Gradient & Backpropagation
description: Giải thích gradient, cơ chế lan truyền ngược, công thức đạo hàm, cách hoạt động và ứng dụng trong Deep Learning.
tags: [deep-learning, optimization, fundamentals, backpropagation, gradient]
---

# Gradient & Backpropagation

## 1. Tóm tắt khái niệm (Definition)

**Gradient**: vector chứa đạo hàm của hàm mất mát theo tham số, cho biết hướng thay đổi nhanh nhất.

**Backpropagation**: thuật toán dùng chain rule để lan truyền gradient từ output về input nhằm cập nhật trọng số.

---

## 2. Mục đích & khi nào dùng (Use Cases)

- Tối ưu hóa mô hình bằng Gradient Descent.  
- Huấn luyện neural network với nhiều lớp.  
- Tính đạo hàm hiệu quả mà không cần symbolic math.  
- Áp dụng trong CNN, RNN, Transformer, LLM.

---

## 3. Cách hoạt động bên trong (Internal Logic)

### Gradient của hàm mất mát theo tham số

Ví dụ đạo hàm MSE theo trọng số \( w \):

$$
\frac{\partial L}{\partial w} = \frac{1}{N} \sum_{i=1}^{N} 2 (y_i - \hat{y}_i)(-x_i)
$$

---

### Chain Rule – nền tảng Backpropagation

Nếu output \( L \) phụ thuộc nhiều lớp:

$$
\frac{\partial L}{\partial w} 
= \frac{\partial L}{\partial a}\cdot\frac{\partial a}{\partial z}\cdot\frac{\partial z}{\partial w}
$$

---

### Lan truyền qua các lớp Neural Network

Xét 1 lớp:

- \( z = w x + b \)  
- \( a = f(z) \)

Gradient theo \( w, b \):

$$
\frac{\partial L}{\partial w} = \frac{\partial L}{\partial a}
\cdot f'(z)
\cdot x
$$

$$
\frac{\partial L}{\partial b} = \frac{\partial L}{\partial a}
\cdot f'(z)
$$

Gradient đưa về lớp trước:

$$
\frac{\partial L}{\partial x}=\frac{\partial L}{\partial a} \cdotf'(z)\cdot w
$$

---

### ✔ Cập nhật trọng số (Gradient Descent)

$$
w := w - \eta \frac{\partial L}{\partial w}
$$

$$
b := b - \eta \frac{\partial L}{\partial b}
$$

Trong đó \( \eta \) là learning rate.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

### PyTorch – Tự tính gradient
```python
loss = criterion(outputs, labels)
loss.backward()   # tính gradient
optimizer.step()  # cập nhật trọng số
optimizer.zero_grad()
```

PyTorch dùng **autograd** để tự động áp dụng chain rule.

---

## 5. Ví dụ code (Code Examples)

```python
import torch
import torch.nn as nn

model = nn.Linear(3, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
criterion = nn.MSELoss()

x = torch.randn(5, 3)
y = torch.randn(5, 1)

pred = model(x)
loss = criterion(pred, y)

loss.backward()        # tính gradient
optimizer.step()       # cập nhật w, b
optimizer.zero_grad()
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Quên `zero_grad()` → gradient bị cộng dồn.
* Dùng `with torch.no_grad()` sai chỗ → gradient không truyền được.
* Gradient exploding/vanishing trong RNN.
* Learning rate lớn → gradient cập nhật quá mạnh, khó hội tụ.
* Tắt gradient của tensor nhưng quên bật lại khi fine-tune.

---

## 7. So sánh với khái niệm liên quan (Comparison)

### Backpropagation vs Autograd

* **Backpropagation**: thuật toán lý thuyết (chain rule).
* **Autograd**: implementation giúp tính toán tự động.

### Gradient Descent vs Backpropagation

* **Gradient Descent**: cập nhật tham số bằng gradient.
* **Backpropagation**: tính gradient bằng chain rule.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Huấn luyện toàn bộ mạng deep learning rely 100% vào backprop.
* Autograd frameworks (PyTorch, TensorFlow) tối ưu mạnh để giảm chi phí tính đạo hàm.
* Dùng kỹ thuật gradient clipping để tránh exploding gradient.
* Trong LLM, backprop được dùng ở scale rất lớn (tỉ tham số).

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Giải thích chain rule và vai trò trong backpropagation?
* Tại sao cần `optimizer.zero_grad()`?
* Sự khác nhau giữa backprop và autograd?
* Tính gradient qua hàm kích hoạt sigmoid như thế nào?
* Vì sao xảy ra vanishing gradient trong mạng sâu?

---

## 10. TL;DR (Short Summary)

* Gradient cho biết hướng thay đổi nhanh nhất của hàm mất mát.
* Backpropagation dùng chain rule để lan truyền gradient ngược.
* Autograd giúp tính gradient tự động.
* Gradient Descent cập nhật trọng số sử dụng gradient.
* Rất quan trọng cho toàn bộ training deep learning.

