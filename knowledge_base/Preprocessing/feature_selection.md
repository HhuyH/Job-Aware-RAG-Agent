---
title: "Feature Selection"
description: "Các kỹ thuật lựa chọn đặc trưng trong Machine Learning."
tags: ["Machine Learning", "Preprocessing", "Feature Selection"]
---

# Feature Selection

Feature Selection là quá trình **chọn ra các đặc trưng quan trọng nhất** nhằm giảm nhiễu, tăng hiệu suất mô hình, giảm thời gian huấn luyện và hạn chế overfitting.

Có ba nhóm kỹ thuật chính:
- **Filter Methods**
- **Wrapper Methods**
- **Embedded Methods**

---

## 1. Filter Methods

Filter methods chọn feature dựa trên **thống kê độc lập với mô hình**.

### 1.1. Chi-Square (Chi²)

- Áp dụng cho: **biến phân loại (categorical)**  
- Đo mức độ phụ thuộc giữa feature và target.  
- Giá trị Chi² cao → feature có ảnh hưởng mạnh.

```python
from sklearn.feature_selection import chi2, SelectKBest

selector = SelectKBest(chi2, k=10)
X_new = selector.fit_transform(X, y)
````

### 1.2. Mutual Information (MI)

* Đo lượng thông tin **giữa feature và target**.
* Dùng được cho cả **classification và regression**.
* MI không giả định quan hệ tuyến tính — phù hợp dữ liệu phức tạp.

```python
from sklearn.feature_selection import mutual_info_classif

mi = mutual_info_classif(X, y)
```

### Khi nào dùng Filter?

* Khi dataset rất lớn.
* Khi muốn loại bớt feature trước các bước nâng cao.
* Khi chưa biết mô hình nào phù hợp.

---

## 2. Wrapper Methods

Wrapper Methods **đánh giá trực tiếp hiệu suất mô hình** để quyết định chọn feature.

### 2.1. Recursive Feature Elimination (RFE)

* Huấn luyện mô hình nhiều lần
* Mỗi vòng loại feature ít quan trọng nhất
* Lặp đến khi còn số feature mong muốn

```python
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
rfe = RFE(model, n_features_to_select=10)
X_new = rfe.fit_transform(X, y)
```

### Ưu điểm

* Tối ưu cho chính mô hình mà bạn sẽ train.
* Hiệu suất cao khi số feature không quá nhiều.

### Nhược điểm

* Tốn thời gian.
* Không phù hợp dataset lớn.

---

## 3. Embedded Methods

Các mô hình **tự chọn feature** trong quá trình học.

### 3.1. L1 Regularization (Lasso)

* Với Lasso, trọng số của các feature không quan trọng sẽ bị **đẩy về 0**.
* Dùng để **chọn feature tuyến tính**.

```python
from sklearn.linear_model import Lasso

model = Lasso(alpha=0.01)
model.fit(X, y)
importance = model.coef_
```

### 3.2. Tree-based Feature Importance

Áp dụng cho:

* Decision Tree
* Random Forest
* XGBoost / LightGBM / CatBoost

Các mô hình cây tự đánh giá mức đóng góp của từng feature vào việc giảm impurity.

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X, y)
importance = model.feature_importances_
```

### Ưu điểm

* Hoạt động tốt với quan hệ phi tuyến.
* Không cần scale dữ liệu.
* Thường chính xác hơn filter methods.

---

## 4. Nên chọn phương pháp nào?

| Dataset                   | Lời khuyên                        |
| ------------------------- | --------------------------------- |
| > 10.000 features         | Dùng **Filter** trước để giảm bớt |
| < 2000 features           | Dùng **RFE** hoặc **Embedded**    |
| Dữ liệu phi tuyến         | Dùng Tree-based hoặc MI           |
| Mô hình tuyến tính        | Lasso + MI                        |
| Muốn giảm thời gian train | Filter hoặc Embedded              |

---

## Kết luận

Feature Selection giúp mô hình:

* **Giảm overfitting**
* **Tăng tốc độ học**
* **Cải thiện độ chính xác**
* **Tăng khả năng diễn giải**

Kết hợp nhiều phương pháp thường cho kết quả tốt nhất.
