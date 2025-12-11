---
title: "Encoding Categorical Features"
description: "Các kỹ thuật mã hóa dữ liệu phân loại (categorical) trong Machine Learning."
tags: ["Preprocessing", "Encoding", "Categorical Data", "Machine Learning"]
---

# Encoding Categorical Features

Dữ liệu phân loại (categorical features) không thể đưa trực tiếp vào mô hình Machine Learning.  
Mã hóa (encoding) chuyển các giá trị dạng chuỗi thành dạng số phù hợp cho mô hình.

---

## 1. One-Hot Encoding

Biến mỗi giá trị category thành một cột nhị phân (0/1).

### Khi dùng
- Khi số lượng category ít.
- Dữ liệu **không có thứ tự** giữa các giá trị (nominal).

### Code
```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
encoded = encoder.fit_transform(df[["color"]])
````

### Nhược điểm

* Nổ số chiều (curse of dimensionality) nếu có nhiều category.

---

## 2. Label Encoding

Gán mỗi category một số nguyên.

### Khi dùng

* Với **mô hình tree-based** (Decision Tree, Random Forest, XGBoost).
* Khi giá trị chỉ để phân biệt, không có thứ tự thực sự.

### Không dùng cho

* Linear/Logistic Regression, SVM → vì tạo thứ tự **giả** → gây sai lệch.

### Code

```python
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
df["sex_encoded"] = encoder.fit_transform(df["sex"])
```

---

## 3. Ordinal Encoding

Mã hóa category **theo thứ tự thực**.

### Khi dùng

* Khi dữ liệu có cấp bậc:

Ví dụ:

* "Low" < "Medium" < "High"
* "Freshman" < "Sophomore" < "Junior" < "Senior"

### Code

```python
from sklearn.preprocessing import OrdinalEncoder

encoder = OrdinalEncoder(categories=[["Low", "Medium", "High"]])
df[["quality"]] = encoder.fit_transform(df[["quality"]])
```

---

## 4. Target Encoding

> *Cẩn trọng: dễ gây **data leakage** nếu không dùng cross-validation.*

### Ý tưởng

* Với mỗi category → thay bằng **mean của target** (đối với bài toán classification/regression).

### Khi dùng

* High-cardinality categorical features (nhiều giá trị khác nhau).
* Mô hình tree-based, boosting (LightGBM, CatBoost, XGBoost).

### Không dùng trực tiếp khi

* Dùng toàn bộ dữ liệu để tính target mean → gây leakage → accuracy ảo.

### Cách an toàn

* Dùng **K-fold target encoding**.

### Code (minh họa)

```python
import category_encoders as ce

encoder = ce.TargetEncoder(cols=["city"])
df["city_encoded"] = encoder.fit_transform(df["city"], df["price"])
```

---

# Tóm tắt

| Phương pháp      | Khi dùng                     | Ưu                   | Nhược                  |
| ---------------- | ---------------------------- | -------------------- | ---------------------- |
| One-hot          | Category ít, không có thứ tự | Dễ hiểu, an toàn     | Tăng số chiều          |
| Label Encoding   | Model tree-based             | Đơn giản             | Áp đặt thứ tự giả      |
| Ordinal Encoding | Category có thứ tự           | Giữ đúng bản chất    | Phải biết trước thứ tự |
| Target Encoding  | High-cardinality             | Hiệu quả, giảm chiều | Dễ leakage nếu sai     |

---

Encoding là bước quan trọng trước khi training mô hình, thường đi cùng scaling, cleaning và feature engineering.
