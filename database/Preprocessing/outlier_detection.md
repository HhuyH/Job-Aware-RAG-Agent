---
title: "Outlier Detection"
description: "Các phương pháp phát hiện ngoại lệ (outliers) trong dữ liệu."
tags: ["Preprocessing", "Outlier Detection", "Machine Learning"]
---

# Outlier Detection

Outlier (giá trị ngoại lệ) là các điểm dữ liệu khác biệt lớn so với phần còn lại.  
Xử lý đúng outlier giúp giảm nhiễu, cải thiện mô hình và tăng độ ổn định.

Có bốn nhóm kỹ thuật phổ biến:

- **Z-score**
- **IQR**
- **Isolation Forest**
- **Local Outlier Factor (LOF)**

---

## 1. Z-score

Phát hiện điểm bất thường dựa trên khoảng cách so với trung bình tính theo đơn vị độ lệch chuẩn.

### Công thức
$$
z = \frac{x - \mu}{\sigma}
$$

### Quy tắc
- |z| > 3 → thường được coi là outlier

### Khi dùng
- Dữ liệu phân phối gần **Gaussian**
- Không phù hợp với phân phối lệch

### Code
```python
import numpy as np

z = np.abs((df["value"] - df["value"].mean()) / df["value"].std())
outliers = df[z > 3]
````

---

## 2. IQR (Interquartile Range)

Dựa trên phân vị:

* Q1 = 25%
* Q3 = 75%
* IQR = Q3 - Q1

### Rule

* Outlier nếu:
  $$
  x < Q1 - 1.5 \cdot IQR \quad \text{hoặc} \quad x > Q3 + 1.5 \cdot IQR
  $$

### Khi dùng

* Dữ liệu không phân phối chuẩn
* Dữ liệu có nhiều lệch (skewed distribution)

### Code

```python
Q1 = df["value"].quantile(0.25)
Q3 = df["value"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df["value"] < Q1 - 1.5 * IQR) | 
              (df["value"] > Q3 + 1.5 * IQR)]
```

---

## 3. Isolation Forest

Phương pháp dựa trên ý tưởng: **outlier dễ bị cô lập** qua các phép chia nhánh ngẫu nhiên.

### Đặc điểm

* Hiệu quả cho dữ liệu lớn
* Hỗ trợ dữ liệu nhiều chiều (high-dimensional)
* Không cần giả định phân phối dữ liệu
* Dễ scale

### Khi dùng

* Dataset lớn
* Quan hệ phi tuyến phức tạp
* Feature nhiều chiều

### Code

```python
from sklearn.ensemble import IsolationForest

iso = IsolationForest(contamination=0.05, random_state=42)
df["outlier"] = iso.fit_predict(df[features])

outliers = df[df["outlier"] == -1]
```

---

## 4. Local Outlier Factor (LOF)

Đo lường độ bất thường dựa trên **mật độ lân cận** (local density).
Outlier → có mật độ thấp hơn so với hàng xóm.

### Đặc điểm

* Tốt khi dữ liệu có cấu trúc không đồng nhất
* Dựa vào khoảng cách KNN
* Không phù hợp dataset quá lớn

### Code

```python
from sklearn.neighbors import LocalOutlierFactor

lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)
outliers = lof.fit_predict(df[features])

df["outlier"] = outliers
df_outliers = df[df["outlier"] == -1]
```

---

# Nên dùng kỹ thuật nào?

| Tình huống                       | Khuyến nghị               |
| -------------------------------- | ------------------------- |
| Dữ liệu 1 chiều, phân phối chuẩn | Z-score                   |
| Dữ liệu lệch (skewed)            | IQR                       |
| Dataset lớn, nhiều chiều         | Isolation Forest          |
| Dữ liệu có cụm rõ ràng           | LOF                       |
| Không biết phân phối             | IQR hoặc Isolation Forest |

---

# Lưu ý quan trọng

* Không nên loại outlier khi chúng là **thông tin quan trọng** của bài toán.
* Với mô hình tree-based, outlier ít ảnh hưởng → có thể bỏ qua.
* Luôn kiểm tra bằng visualization (boxplot, scatter…) trước khi xử lý.

