---
title: "Handling Missing Values"
description: "Các phương pháp xử lý dữ liệu bị thiếu trong Machine Learning."
tags: ["Preprocessing", "Missing Values", "Machine Learning"]
---

# Handling Missing Values

Thiếu dữ liệu (missing values) xuất hiện phổ biến trong mọi bài toán Machine Learning. Nếu không xử lý đúng, mô hình có thể học sai quy luật hoặc giảm mạnh độ chính xác.

---

## 1. Mean / Median Imputation

### Khi dùng
- Dùng cho dữ liệu số (numerical).
- Mean dùng khi phân phối gần chuẩn.
- Median tốt hơn khi dữ liệu có outlier.

### Cách làm
Thay giá trị thiếu bằng **mean** hoặc **median** của cột.

```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="median")
df[["age"]] = imputer.fit_transform(df[["age"]])
````

---

## 2. KNN Imputation

### Ý tưởng

* Tìm **k mẫu gần nhất** (K Nearest Neighbors) dựa trên các feature còn đầy đủ.
* Điền giá trị thiếu bằng trung bình/điểm trung vị của k hàng đó.

### Khi dùng

* Dữ liệu có quan hệ giữa các feature.
* Không quá nhiều missing (vì KNN tốn chi phí tính toán).

### Code

```python
from sklearn.impute import KNNImputer

imputer = KNNImputer(n_neighbors=5)
df_imputed = imputer.fit_transform(df)
```

---

## 3. MICE (Multiple Imputation by Chained Equations)

### Ý tưởng

* Xây mô hình dự đoán cho từng cột bị thiếu.
* Lặp qua từng cột nhiều lần để giá trị hội tụ.
* Sinh nhiều phiên bản dữ liệu → tăng độ tin cậy thống kê.

### Khi dùng

* Thiếu dữ liệu nhiều và phân phối phức tạp.
* Cần giữ tương quan giữa nhiều biến.

### Code (sklearn + fancyimpute style)

```python
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

imputer = IterativeImputer()
df_imputed = imputer.fit_transform(df)
```

---

## 4. Khi nào nên xóa hàng/cột?

### Xóa hàng (row deletion)

Chỉ nên dùng khi:

* Số lượng hàng missing **< 5%** dataset.
* Hàng chứa quá nhiều lỗi → không thể sửa.

```python
df = df.dropna()
```

### Xóa cột (column deletion)

Chỉ dùng khi:

* Cột missing **> 40–50%** và không quan trọng.
* Không thể ước lượng giá trị hợp lý.
* Feature không liên quan bản chất bài toán.

```python
df = df.drop(columns=["feature_x"])
```

---

## Tóm tắt

| Phương pháp  | Ưu điểm                      | Nhược điểm                   | Khi dùng                                  |
| ------------ | ---------------------------- | ---------------------------- | ----------------------------------------- |
| Mean/Median  | Nhanh, đơn giản              | Mất thông tin, giảm variance | Numerical đơn giản                        |
| KNN          | Giữ quan hệ giữa các feature | Chậm khi dataset lớn         | Dữ liệu có cấu trúc rõ                    |
| MICE         | Chính xác, giữ tương quan    | Tốn thời gian                | Dataset phức tạp                          |
| Xóa hàng/cột | Tinh gọn dữ liệu             | Mất thông tin                | Khi missing quá lớn hoặc không quan trọng |

---

Xử lý missing values là bước quan trọng trước scaling, encoding và training mô hình.
