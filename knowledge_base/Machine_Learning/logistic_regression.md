--- 
title: "Logistic Regression" 
description: "Thuật toán Logistic Regression trong Machine Learning." 
tags: ["Machine Learning", "Logistic Regression"] 
---

# Logistic Regression

## 1. Khái niệm

Logistic Regression là thuật toán **Classification**, dùng để dự đoán xác suất một mẫu thuộc về một lớp cụ thể. Dù tên có chữ "Regression", thuật toán này **không** dùng cho dự đoán giá trị liên tục mà dùng để phân loại.

Cốt lõi của nó là mô hình hóa xác suất bằng hàm sigmoid:

$$
( \sigma(z) = \frac{1}{1 + e^{-z}} )
$$

Trong đó 

$$
(z = w^T x + b).
$$

---

## 2. Bản chất hoạt động

1. Tính giá trị tuyến tính: (z = w^T x + b).
2. Đưa qua hàm sigmoid để thu được xác suất từ 0–1.
3. Chọn lớp dựa trên ngưỡng (thường là 0.5).
4. Tối ưu các tham số bằng **Gradient Descent** để giảm hàm mất mát Log-loss.

---

## 3. Các loại Logistic Regression

### 3.1. Binary Classification

Phân loại 2 lớp, ví dụ:

* Spam / Không spam
* Có bệnh / Không bệnh
* Chấp nhận / Từ chối

### 3.2. Multi-class (One-vs-Rest)

Chia nhiều lớp bằng cách huấn luyện nhiều mô hình nhị phân.

### 3.3. Multi-label

Một mẫu có thể mang nhiều nhãn.

---

## 4. Hàm mất mát (Loss Function)

Sử dụng **Binary Cross Entropy**:

$$
L = -[y \log(\hat{y}) + (1 - y) \log(1 - \hat{y})]
$$

Trong đó:

* (y): nhãn thật
* 
$$
(\hat{y})
$$

xác suất dự đoán

---

## 5. Ưu điểm

* Đơn giản, dễ hiểu, dễ triển khai.
* Training nhanh, hiệu quả với dữ liệu tuyến tính.
* Xác suất dễ diễn giải.
* Ít overfitting khi kết hợp Regularization.

---

## 6. Nhược điểm

* Khó xử lý quan hệ phi tuyến mạnh.
* Nhạy với outlier.
* Cần dữ liệu tách biệt được theo ranh giới tuyến tính.

---

## 7. Regularization trong Logistic Regression

* **L1 (Lasso)** → làm thưa mô hình (feature selection).
* **L2 (Ridge)** → giảm overfitting.

Dùng trong sklearn:

* penalty="l1", penalty="l2", penalty="elasticnet".

---

## 8. Ứng dụng thực tế

* Phân loại email.
* Dự đoán khách hàng rời bỏ (churn prediction).
* Chẩn đoán bệnh.
* Phát hiện gian lận.
* Scoring risk trong tài chính.

---

## 9. Cách nhận biết khi nào dùng Logistic Regression

Dùng khi:

* Bài toán phân loại 2 lớp hoặc nhiều lớp.
* Dữ liệu không quá phức tạp.
* Muốn mô hình dễ giải thích.
* Cần xác suất đầu ra rõ ràng.

---

## 10. Metric đánh giá

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC
* Confusion Matrix

---

## 11. Cách trả lời phỏng vấn (chốt gọn)

* Logistic Regression là mô hình phân loại dựa trên xác suất nhờ hàm sigmoid.
* Đơn giản, hiệu quả, dễ diễn giải.
* Dùng Binary Cross Entropy để tối ưu.
* Hoạt động tốt khi dữ liệu tuyến tính và không quá ồn.
