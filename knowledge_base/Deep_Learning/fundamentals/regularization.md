---
title: Regularization Techniques
description: Giải thích các kỹ thuật Regularization trong Deep Learning, công thức toán, cơ chế hoạt động và ứng dụng thực tế.
tags: [deep-learning, fundamentals, regularization, overfitting, dropout, l1, l2]
---

# Regularization Techniques

## 1. Tóm tắt khái niệm (Definition)
Regularization là kỹ thuật **giảm overfitting** bằng cách thêm **ràng buộc hoặc điều chỉnh trọng số** trong quá trình huấn luyện.

---

## 2. Mục đích & khi nào dùng (Use Cases)
- Ngăn mô hình học quá kỹ dữ liệu training → generalization tốt.  
- Dùng khi mô hình quá phức tạp so với dữ liệu.  
- Thường kết hợp với neural network, regression, logistic regression.

---

## 3. Các phương pháp phổ biến

### 3.1 L1 Regularization (Lasso)

$$
L = L_0 + \lambda \sum_{i} |w_i|
$$

- \( L_0 \): loss gốc (MSE, BCE…)  
- \( \lambda \): hệ số điều chỉnh  
- Tạo **sparse weights**, một số weight = 0 → feature selection.

---

### 3.2 L2 Regularization (Ridge / Weight Decay)

$$
L = L_0 + \lambda \sum_{i} w_i^2
$$

- Trọng số giảm dần → giảm overfitting.  
- Phổ biến trong neural network, logistic regression.

---

### 3.3 Dropout

- Random loại bỏ một số neuron trong layer:

$$
\text{during training: } a_i = a_i \cdot d_i, \quad d_i \sim \text{Bernoulli}(p)
$$

- \( p \): keep probability  
- Giúp mô hình **không quá phụ thuộc vào neuron nào**.

---

### 3.4 Early Stopping

- Giám sát **validation loss**, dừng training khi loss không giảm.  
- Không cần thêm term vào loss, nhưng giúp tránh overfitting.

---

### 3.5 Data Augmentation

- Tăng dữ liệu bằng cách **biến đổi input**: rotation, flipping, scaling, noise.  
- Giúp mô hình **học robust hơn**, không overfit vào training set.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

### PyTorch Example

```python
import torch
import torch.nn as nn
import torch.optim as optim

model = nn.Linear(10,1)

# L2 Regularization
optimizer = optim.SGD(model.parameters(), lr=0.01, weight_decay=0.001)

# Dropout layer
dropout = nn.Dropout(p=0.5)
````

---

## 5. Ví dụ code (Code Examples)

```python
import torch
import torch.nn as nn

x = torch.randn(5,10)
y = torch.randn(5,1)

model = nn.Sequential(
    nn.Linear(10,20),
    nn.ReLU(),
    nn.Dropout(0.5),
    nn.Linear(20,1)
)

criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=0.001)

# Forward
pred = model(x)
loss = criterion(pred, y)

# Backward + update
loss.backward()
optimizer.step()
optimizer.zero_grad()
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Quá nhiều dropout → underfitting.
* Quá nhỏ λ trong L1/L2 → không giảm overfitting.
* Không shuffle dữ liệu khi early stopping → đánh giá sai.
* Data augmentation không hợp lý → mô hình học sai pattern.

---

## 7. So sánh với khái niệm liên quan (Comparison)

| Method            | Output             | Ưu điểm              | Nhược điểm               |
| ----------------- | ------------------ | -------------------- | ------------------------ |
| L1                | Sparse weights     | Feature selection    | Gradient không mượt      |
| L2                | Small weights      | Gradient ổn định     | Không sparse             |
| Dropout           | Random neuron mask | Reduce co-adaptation | Training lâu hơn         |
| Early Stopping    | Stop training      | Đơn giản, hiệu quả   | Không tận dụng full data |
| Data Augmentation | Augmented dataset  | Robust model         | Cần domain knowledge     |

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* CNN: Dropout + L2 → tránh overfitting khi data ít.
* Logistic regression: L1 → chọn feature quan trọng.
* Large dataset: Early stopping + data augmentation → generalization tốt.
* Kết hợp nhiều phương pháp → hiệu quả cao hơn.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* L1 vs L2, khi nào dùng cái nào?
* Dropout ảnh hưởng đến forward/backward như thế nào?
* Early stopping có thể gây underfitting không?
* Data augmentation giúp giảm overfitting ra sao?
* Weight decay là gì và khác gì với L2?

---

## 10. TL;DR (Short Summary)

* Regularization giảm overfitting → generalization tốt hơn.
* L1 → sparse, L2 → small weights.
* Dropout loại bỏ neuron ngẫu nhiên, Early Stopping dừng training sớm.
* Data augmentation tăng dữ liệu, robust model.
* Kết hợp các phương pháp → mô hình ổn định, tránh overfitting.
