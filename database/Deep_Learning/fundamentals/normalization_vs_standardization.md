---
title: Normalization vs Standardization
description: Giải thích sự khác nhau giữa Normalization và Standardization trong xử lý dữ liệu, công thức toán, cách hoạt động và ứng dụng trong Deep Learning.
tags: [deep-learning, fundamentals, data-preprocessing, normalization, standardization]
---

# Normalization vs Standardization

## 1. Tóm tắt khái niệm (Definition)
- **Normalization**: chuyển đổi dữ liệu về cùng **dải giá trị chuẩn**, thường [0,1] hoặc [-1,1].  
- **Standardization**: chuẩn hóa dữ liệu để có **mean = 0** và **std = 1**.

---

## 2. Mục đích & khi nào dùng (Use Cases)
- Giúp **gradient descent hội tụ nhanh hơn**.  
- Tránh feature scale khác nhau làm mô hình học lệch.  
- Normalization: khi cần giới hạn dữ liệu trong dải nhất định.  
- Standardization: khi phân phối dữ liệu không đều, cần zero-centered.

---

## 3. Công thức

### 3.1 Min-Max Normalization

$$
x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
$$

- Dữ liệu được scale về [0,1].  
- Nhạy với **outlier**.

---

### 3.2 Standardization (Z-score)

$$
x' = \frac{x - \mu}{\sigma}
$$

- \(\mu\): trung bình dữ liệu  
- \(\sigma\): độ lệch chuẩn  
- Zero-centered, ít nhạy với outlier hơn normalization.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

### Python Example (scikit-learn)

```python
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Normalization
scaler = MinMaxScaler()
X_norm = scaler.fit_transform(X)

# Standardization
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
````

---

## 5. Ví dụ code (Code Examples)

```python
import numpy as np

X = np.array([1, 2, 3, 4, 5]).reshape(-1,1)

# Min-Max Normalization
X_norm = (X - X.min()) / (X.max() - X.min())

# Standardization
X_std = (X - X.mean()) / X.std()

print("Normalized:", X_norm)
print("Standardized:", X_std)
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Quên fit trên **training set**, rồi transform cả test → dữ liệu leak.
* Min-Max nhạy với outlier → ảnh hưởng scale.
* Standardization giả định phân phối gần Gaussian, nếu lệch quá → vẫn cần xử lý outlier.

---

## 7. So sánh với khái niệm liên quan (Comparison)

| Phương pháp     | Output        | Ưu điểm                         | Nhược điểm                               |
| --------------- | ------------- | ------------------------------- | ---------------------------------------- |
| Normalization   | [0,1]         | Dữ liệu có scale giống nhau     | Nhạy với outlier                         |
| Standardization | mean=0, std=1 | Zero-centered, gradient ổn định | Cần tính mean/std, vẫn ảnh hưởng outlier |

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Neural Network: nên **standardization** để gradient descent ổn định.
* Khi input vào activation như sigmoid/relu: min-max normalization giúp tránh saturation.
* Tree-based models (Random Forest, XGBoost) thường **không cần scaling**.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Khi nào dùng normalization, khi nào dùng standardization?
* Vì sao min-max normalization nhạy với outlier?
* Standardization giúp gradient descent ổn định thế nào?
* Scaling có cần thiết cho decision tree không?

---

## 10. TL;DR (Short Summary)

* Normalization: scale về dải cố định, nhạy outlier.
* Standardization: zero-centered, std=1, ít nhạy outlier.
* Chọn phương pháp tùy loại mô hình và dữ liệu.
* Neural network thường chuẩn hóa input để gradient descent hiệu quả.