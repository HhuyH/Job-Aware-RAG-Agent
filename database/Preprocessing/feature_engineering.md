---
title: "Feature Engineering"
description: "Tạo đặc trưng mới để cải thiện mô hình."
tags: ["Machine Learning", "Preprocessing", "Feature Engineering"]
---

# Feature Engineering

Feature Engineering là quá trình **tạo ra các đặc trưng mới** từ dữ liệu gốc nhằm giúp mô hình học tốt hơn. Đây là một trong những bước có ảnh hưởng mạnh nhất tới hiệu suất mô hình.

---

## 1. Polynomial Features

### Khái niệm  
Tạo các đặc trưng mới bằng cách lấy **lũy thừa** hoặc **tương tác** giữa các feature liên tục.

Ví dụ:  
- $$
x \rightarrow [x, x^2, x^3]
$$

- Tạo thêm feature từ tương tác: 

$$
x_1 \cdot x_2
$$


### Khi nào dùng?
- Khi mô hình có tính **tuyến tính** (Linear Regression, Logistic Regression, SVM Linear) nhưng dữ liệu lại quan hệ **phi tuyến**.
- Khi nghi ngờ có tương tác giữa các biến.

### Nhược điểm
- Làm tăng số lượng biến → dễ gây **overfitting**.  
- Tốn tài nguyên tính toán.

### Cách dùng với scikit-learn

```python
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2, include_bias=False)
X_new = poly.fit_transform(X)
````

---

## 2. Interaction Features

### Khái niệm

Tạo feature bằng cách kết hợp **nhiều biến với nhau** để biểu diễn mối quan hệ.

Ví dụ:

* Nhân: 
$$
x_1 \cdot x_2
$$

* Chia: 
$$
x_1 / x_2
$$

* Hiệu: 
$$
x_1 - x_2
$$

### Khi nào dùng?

* Khi có ý nghĩa domain:

  * **BMI = weight / height²**
  * **Speed = distance / time**
* Khi các mối quan hệ tương tác ảnh hưởng trực tiếp đến đầu ra.

### Lưu ý

* Nên dựa vào **kiến thức miền (domain knowledge)**.
* Tránh tạo quá nhiều feature vô nghĩa → làm nhiễu mô hình.

---

## 3. Domain-Specific Features

### Khái niệm

Đặc trưng được tạo ra dựa trên **hiểu biết chuyên môn của lĩnh vực**.

### Ví dụ theo từng domain

#### Finance / E-commerce

* Ratio: revenue / cost
* Profit margin
* Days since last purchase
* Customer lifetime value (CLV)

#### NLP

* Word count
* TF-IDF score
* Sentiment score
* Number of named entities

#### Computer Vision

* Edge density
* Histogram of oriented gradients (HOG)
* Color histogram

#### Time Series

* Lag features
* Rolling mean/variance
* Trend / seasonality decomposition

### Khi nào cần?

* Khi dataset phức tạp hoặc mô hình baseline không đủ mạnh.
* Khi thuật toán truyền thống (tree-based, linear models) không tự động trích đặc trưng.

---

## Ghi chú quan trọng

* Feature Engineering luôn đi kèm **cross-validation** để kiểm chứng hiệu quả.
* Không nên tạo feature tùy tiện — hãy ưu tiên **tính giải thích được** và **liên quan rõ ràng** với bài toán.
* Với mô hình phức tạp như **XGBoost, LightGBM, Neural Networks**, nhiều feature có thể không cần vì mô hình tự học representation.

---

## Kết luận

Feature Engineering là bước mang tính **đòn bẩy**, giúp mô hình cải thiện hiệu suất mà không cần thay đổi thuật toán. Dù đơn giản hay phức tạp, mục tiêu là:

* Làm đặc trưng giàu thông tin hơn
* Phản ánh tốt hơn bản chất dữ liệu
* Giảm noise
* Tăng sức mạnh mô hình
