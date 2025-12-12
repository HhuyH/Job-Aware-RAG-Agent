---
title: "Train/Test Split & Cross-Validation"
description: "Hướng dẫn chia dữ liệu và các kỹ thuật Cross-Validation trong Machine Learning."
tags: ["Preprocessing", "Model Evaluation", "Cross-Validation"]
---

# Train/Test Split & Cross-Validation

Việc chia dữ liệu đúng cách quyết định độ tin cậy của mô hình.  
Mục tiêu là đánh giá mô hình trên dữ liệu **chưa từng thấy**, tránh overfitting.

---

# 1. Train / Validation / Test Split

## 1.1. Train set
Dùng để mô hình học tham số (weights).

## 1.2. Validation set
Dùng để:
- chọn mô hình,
- tinh chỉnh hyperparameters,
- phát hiện overfitting.

## 1.3. Test set
Chỉ dùng **một lần cuối** để đánh giá mô hình sau khi hoàn thiện.

## 1.4. Tỉ lệ thường dùng
- 70 / 15 / 15  
- 80 / 10 / 10  
- Hoặc 80 / 20 (không dùng validation khi cross-validation)

## Code ví dụ
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
````

---

# 2. Cross-Validation

Cross-validation giúp đánh giá mô hình ổn định hơn bằng cách chia dữ liệu thành nhiều phần và lặp lại quá trình train/test nhiều lần.

---

## 2.1. K-Fold Cross-Validation

Chia dataset thành **K phần bằng nhau**.
Mỗi lần lấy 1 phần làm validation, K–1 phần còn lại để train.

→ K mô hình → trung bình kết quả.

### Khi dùng

* Dữ liệu không quá nhỏ
* Khi cần đánh giá mô hình ổn định

### Code

```python
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier

kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(RandomForestClassifier(), X, y, cv=kf)

print(scores.mean())
```

---

## 2.2. Stratified K-Fold

Dùng cho **classification** khi tỉ lệ lớp lệch.
Đảm bảo mỗi fold giữ nguyên tỉ lệ nhãn, tránh bias.

### Khi dùng

* Classification
* Dataset imbalance

### Code

```python
from sklearn.model_selection import StratifiedKFold, cross_val_score

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(
    RandomForestClassifier(), X, y, cv=skf
)

print(scores.mean())
```

---

# 3. Time Series Split

Không được shuffle dữ liệu theo thời gian.
Mô hình phải luôn được train trên quá khứ và test trên tương lai.

Ví dụ:

| Split | Train | Test    |
| ----- | ----- | ------- |
| 1     | 1–100 | 101–120 |
| 2     | 1–120 | 121–140 |
| 3     | 1–140 | 141–160 |

### Khi dùng

* Dự đoán giá chứng khoán
* Dự đoán thời tiết
* Bất kỳ bài toán time series nào

### Code

```python
from sklearn.model_selection import TimeSeriesSplit
import numpy as np

tscv = TimeSeriesSplit(n_splits=5)

for train_idx, val_idx in tscv.split(X):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]
```

---

# 4. Nên dùng phương pháp nào?

| Tình huống               | Gợi ý                             |
| ------------------------ | --------------------------------- |
| Dataset vừa và lớn       | K-Fold                            |
| Classification imbalance | Stratified K-Fold                 |
| Dữ liệu thời gian        | TimeSeriesSplit                   |
| Dataset nhỏ              | K-Fold (K lớn, ví dụ 10)          |
| Cần speed                | Hold-out (train/test bình thường) |

---

# 5. Lưu ý quan trọng

* Tuyệt đối **không để dữ liệu test rò rỉ vào train/validation**.
* Không scaling trước rồi mới split — phải **fit scaler bằng train, transform lên cả train/test**.
* Với time series: không dùng random split.
* Không dùng test set để tuning hyperparameters.
