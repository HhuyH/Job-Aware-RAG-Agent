---
title: Loss Functions
description: Giải thích các hàm mất mát phổ biến trong Deep Learning, công thức, cơ chế hoạt động, ứng dụng và lỗi thường gặp.
tags: [deep-learning, fundamentals, loss-functions, optimization]
---

# Loss Functions

## 1. Tóm tắt khái niệm (Definition)
Hàm mất mát (loss function) đo mức độ **dự đoán sai lệch** của mô hình so với giá trị thực.  
Là cơ sở để tính gradient và cập nhật tham số trong quá trình huấn luyện.

---

## 2. Mục đích & khi nào dùng (Use Cases)
- Định lượng sai số của mô hình.  
- Hướng dẫn gradient descent cập nhật trọng số.  
- Chọn loss phù hợp với loại bài toán:
  - Regression → MSE, MAE  
  - Classification → Cross-Entropy, Hinge

---

## 3. Các loại loss function phổ biến

### 3.1 Mean Squared Error (MSE)

$$
\text{MSE} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2
$$

- Phù hợp cho regression.  
- Nhạy với outlier.

---

### 3.2 Mean Absolute Error (MAE)

$$
\text{MAE} = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i|
$$

- Ít nhạy với outlier hơn MSE.  
- Gradient không mượt tại điểm $0$.

---

### 3.3 Binary Cross-Entropy (BCE)

$$
\text{BCE} = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log \hat{y}_i + (1 - y_i) \log (1 - \hat{y}_i) \right]
$$

- Dùng cho **binary classification**.  
- Output mô hình phải qua sigmoid.

---

### 3.4 Categorical Cross-Entropy (CCE)

$$
\text{CCE} = -\frac{1}{N} \sum_{i=1}^{N} \sum_{c=1}^{C} y_{i,c} \log \hat{y}_{i,c}
$$

- Dùng cho **multi-class classification**.  
- Output mô hình phải qua softmax.

---

### 3.5 Hinge Loss (SVM)

$$
\text{Hinge} = \frac{1}{N} \sum_{i=1}^{N} \max(0, 1 - y_i \cdot \hat{y}_i)
$$

- Dùng cho **linear classifier / SVM**.  
- $y_i \in \{-1, +1\}$.

---

### 3.6 Kullback-Leibler Divergence (KL Divergence)

$$
D_{KL}(P \parallel Q) = \sum_{i} P(i) \log \frac{P(i)}{Q(i)}
$$

- Dùng để đo sự khác nhau giữa **two probability distributions**.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

### PyTorch Example
```python
import torch
import torch.nn as nn

# MSE
criterion = nn.MSELoss()

# Cross-Entropy
criterion = nn.CrossEntropyLoss()

# Hinge Loss
criterion = nn.MultiMarginLoss()
````

---

## 5. Ví dụ code (Code Examples)

```python
import torch

y_true = torch.tensor([1.0, 2.0, 3.0])
y_pred = torch.tensor([1.1, 1.9, 2.8])

# MSE Loss
loss_fn = nn.MSELoss()
loss = loss_fn(y_pred, y_true)
print(loss)
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Dùng BCE nhưng output chưa qua sigmoid → loss = NaN.
* Dùng CCE nhưng target không one-hot hoặc không đúng shape.
* MSE cho classification → không phù hợp.
* Gradient vanish/explode khi loss quá lớn hoặc không chuẩn hóa dữ liệu.

---

## 7. So sánh với khái niệm liên quan (Comparison)

| Loss          | Dùng cho                   | Đặc điểm            |
| ------------- | -------------------------- | ------------------- |
| MSE           | Regression                 | Nhạy với outlier    |
| MAE           | Regression                 | Ít nhạy với outlier |
| BCE           | Binary classification      | Output sigmoid      |
| CCE           | Multi-class classification | Output softmax      |
| Hinge         | Linear classifier / SVM    | Target ±1           |
| KL Divergence | Probability distribution   | So sánh P vs Q      |

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Regression: dự đoán giá, thời gian, nhiệt độ → MSE / MAE
* Classification: hình ảnh, NLP → BCE / CCE
* SVM: phân loại tuyến tính → Hinge Loss
* LLM / probabilistic models → KL Divergence

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Giải thích sự khác nhau giữa MSE và MAE.
* Khi nào dùng BCE thay vì MSE?
* Hinge Loss áp dụng ra sao cho binary classification?
* KL Divergence khác Cross-Entropy thế nào?
* Dùng loss không phù hợp → hậu quả gì?

---

## 10. TL;DR (Short Summary)

* Loss function đo sai số dự đoán, cốt lõi cho gradient descent.
* Regression → MSE / MAE; Classification → BCE / CCE; SVM → Hinge.
* KL Divergence đo sự khác biệt giữa distribution.
* Chọn loss đúng bài toán giúp mô hình hội tụ tốt và chính xác.

