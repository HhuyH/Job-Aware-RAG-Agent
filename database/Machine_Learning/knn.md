---
title: "K-Nearest Neighbors (KNN)"
description: "Tài liệu tổng hợp KNN cho cả Classification và Regression."
tags: ["Machine Learning", "KNN", "Classifier", "Regressor"]
---

# K-Nearest Neighbors (KNN)

## 1. Khái niệm

KNN là thuật toán **hàng xóm gần nhất**, hoạt động dựa trên ý tưởng: *một điểm dữ liệu sẽ có nhãn hoặc giá trị giống với các điểm lân cận gần nhất của nó trong không gian đặc trưng*.

Không có giả định mô hình → thuộc nhóm **non-parametric**.
Không có quá trình train thực sự → thuộc loại **lazy learning**.

---

## 2. Cách hoạt động

1. Chọn giá trị **k** (số lượng hàng xóm gần nhất).
2. Tính khoảng cách giữa điểm cần dự đoán và tất cả điểm trong tập train.
3. Lấy ra **k điểm gần nhất**.
4. **Classification:** bỏ phiếu số đông để quyết định nhãn.
5. **Regression:** trung bình giá trị của k hàng xóm.

Các loại khoảng cách phổ biến:

* Euclidean
* Manhattan
* Minkowski
* Cosine similarity (ít hơn nhưng vẫn dùng)

---

## 3. KNN Classifier

### Mô hình

Dự đoán nhãn bằng majority voting.

Ví dụ trực quan:

* Nếu 3/5 hàng xóm gần nhất thuộc class 1 → dự đoán class 1.

### Đặc điểm

* Hiệu quả tốt khi dữ liệu **nhỏ và ít chiều**.
* Nhạy cảm với scale → cần chuẩn hoá.
* Nhạy cảm với outliers.

### Metric

* Accuracy
* F1-score
* Confusion matrix

---

## 4. KNN Regressor

### Mô hình

Dự đoán giá trị bằng trung bình (mean) hoặc median của k hàng xóm.

### Đặc điểm:

* Nhạy cảm với noise → nên dùng median trong trường hợp có outlier.
* Tương tự classifier, yêu cầu chuẩn hoá dữ liệu.

### Metric

* MSE / RMSE
* MAE
* R² score

---

## 5. Hyperparameters quan trọng

| Tham số   | Ý nghĩa                                              |
| --------- | ---------------------------------------------------- |
| k         | số lượng hàng xóm. k nhỏ → overfit, k lớn → underfit |
| metric    | loại khoảng cách                                     |
| weights   | uniform hoặc distance-based (gần hơn nặng hơn)       |
| algorithm | ball_tree, kd_tree, brute                            |

---

## 6. Ưu và nhược điểm

### Ưu điểm

* Đơn giản, dễ hiểu.
* Không cần train.
* Hiệu quả tốt khi dữ liệu phân bố rõ ràng.

### Nhược điểm

* Tốc độ chậm khi dataset lớn.
* Bộ nhớ tốn vì lưu toàn bộ data.
* Nhạy cảm với scale và outlier.
* Hiệu năng kém ở dữ liệu nhiều chiều.

---

## 7. Khi nào nên dùng KNN?

* Dữ liệu không quá lớn (<50k rows).
* Feature không quá nhiều (<50 features).
* Bài toán cần baseline nhanh.
* Mối quan hệ giữa các điểm có tính cục bộ.

---

## 8. Quy trình áp dụng chuẩn

1. Chuẩn hoá dữ liệu (StandardScaler / MinMaxScaler).
2. Chọn k bằng cross-validation.
3. Thử nhiều metric.
4. Nếu dataset lớn → dùng KD-tree hoặc Ball-tree.

---

## 9. Code mẫu

### Classification

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(accuracy_score(y_test, y_pred))
```

### Regression

```python
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = KNeighborsRegressor(n_neighbors=5)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(mean_squared_error(y_test, y_pred))
```

---

## 10. Kết luận

KNN phù hợp cho bài toán nhỏ, cần mô hình đơn giản, dễ hiểu. Chất lượng phụ thuộc mạnh vào preprocessing và scaling. Không thích hợp cho dữ liệu lớn hoặc nhiều chiều.
