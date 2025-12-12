---
title: "Scaling & Normalization"
description: "Chuẩn hóa và biến đổi dữ liệu số trước khi huấn luyện mô hình Machine Learning."
tags: ["Preprocessing", "Scaling", "Normalization", "Machine Learning"]
---

# Scaling & Normalization

Nhiều mô hình Machine Learning nhạy cảm với **độ lớn của feature**.  
Scaling và normalization giúp đưa dữ liệu về cùng thang đo, cải thiện hiệu suất và tốc độ hội tụ.

---

# 1. StandardScaler

Chuẩn hóa dữ liệu về phân phối có **mean = 0** và **variance = 1**.

$$
x_{scaled} = \frac{x - \mu}{\sigma}
$$

### Khi dùng
- Linear Regression  
- Logistic Regression  
- SVM  
- KNN  
- Neural Network

### Không phù hợp
- Tree-based models (Decision Tree, Random Forest, XGBoost)

### Code
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled = scaler.fit_transform(df[["age", "income"]])
````

---

# 2. MinMaxScaler

Đưa dữ liệu về khoảng **[0, 1]**.

$$
x_{scaled} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
$$

### Khi dùng

* KNN, SVM
* Neural Network (đặc biệt khi dùng sigmoid/tanh)

### Nhược điểm

* Nhạy cảm với outliers → dễ kéo giãn toàn bộ dữ liệu.

### Code

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaled = scaler.fit_transform(df[["age", "income"]])
```

---

# 3. RobustScaler

Dùng median và IQR để giảm ảnh hưởng của outliers.

$$
x_{scaled} = \frac{x - Q_2}{IQR}
$$

### Khi dùng

* Dữ liệu có outlier mạnh
* Thay thế an toàn cho StandardScaler

### Code

```python
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
scaled = scaler.fit_transform(df[["salary", "expenses"]])
```

---

# 4. Normalization vs Standardization

### **Standardization (Z-score scaling)**

* Biến dữ liệu về mean = 0, std = 1
* Áp dụng cho **từng feature**

### **Normalization (Vector normalization — L1, L2)**

Chuẩn hóa **từng mẫu dữ liệu** về độ dài vector nhất định.

Ví dụ L2 normalization:

$$
x_{norm} = \frac{x}{|x|_2}
$$

### Khi dùng normalization

* Text data (TF-IDF → normalize)
* KNN / Cosine similarity
* Clustering dựa trên khoảng cách

### Khi KHÔNG dùng normalization

* Khi feature có ý nghĩa tuyệt đối (income, age) → giữ nguyên thang đo

### Code (Normalization)

```python
from sklearn.preprocessing import Normalizer

normalizer = Normalizer(norm="l2")
normalized = normalizer.fit_transform(df)
```

---

# Tóm tắt

| Phương pháp    | Khi dùng                      | Ưu điểm                      | Hạn chế                        |
| -------------- | ----------------------------- | ---------------------------- | ------------------------------ |
| StandardScaler | Dữ liệu không có outlier mạnh | Phổ biến, ổn định            | Nhạy với outlier               |
| MinMaxScaler   | KNN, SVM, NN                  | Giữ cấu trúc khoảng cách tốt | Rất nhạy với outlier           |
| RobustScaler   | Dữ liệu có outlier            | Chống nhiễu tốt              | Không đưa về [0,1]             |
| Normalization  | Vector-based tasks (KNN, NLP) | Phù hợp tính similarity      | Không áp dụng cho từng feature |

---

Scaling là bước cốt lõi trong ML pipeline, ảnh hưởng trực tiếp đến tốc độ hội tụ và chất lượng mô hình.
