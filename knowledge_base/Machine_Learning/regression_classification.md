--- 
title: "Regression vs Classification" 
description: "Khái niệm về Classification và Regression trong Machine Learning." 
tags: ["Machine Learning", "Classification", "Regression"] 
---

# Regression vs Classification

## 1. Khái niệm tổng quan

Machine Learning được chia thành hai nhóm bài toán chính khi làm việc với dữ liệu có nhãn (Supervised Learning): **Regression** và **Classification**. Hai nhóm này khác nhau ở bản chất đầu ra (output), cách đánh giá, và ứng dụng thực tế.

---

## 2. Regression

### 2.1. Định nghĩa

Regression dự đoán **giá trị liên tục** (continuous value). Mục tiêu là tìm hàm ánh xạ từ input sang một số thực.

### 2.2. Đặc điểm

* Output là số thực (real-valued).
* Không chia thành lớp (class).
* Dự đoán xu hướng, giá trị, mức độ.

### 2.3. Ví dụ thực tế

* Dự đoán giá nhà.
* Dự đoán nhiệt độ.
* Dự đoán doanh thu.
* Dự đoán độ ẩm, lượng mưa.

### 2.4. Thuật toán phổ biến

* Linear Regression
* Polynomial Regression
* Ridge/Lasso Regression
* SVR (Support Vector Regression)
* Random Forest Regressor
* KNN Regressor

### 2.5. Metric đánh giá

* MAE (Mean Absolute Error)
* MSE (Mean Squared Error)
* RMSE (Root Mean Squared Error)
* R² Score

---

## 3. Classification

### 3.1. Định nghĩa

Classification dự đoán **nhãn rời rạc** (discrete classes). Mục tiêu là phân loại input vào một trong nhiều nhóm.

### 3.2. Đặc điểm

* Output là class label.
* Có thể là binary hoặc multi-class.
* Sometimes multi-label (nhiều nhãn một lúc).

### 3.3. Ví dụ thực tế

* Phân loại email: spam / không spam.
* Nhận diện khuôn mặt.
* Dự đoán bệnh từ hình ảnh.
* Phân loại khách hàng.

### 3.4. Thuật toán phổ biến

* Logistic Regression
* SVM (SVC)
* Decision Tree / Random Forest Classifier
* KNN Classifier
* Naive Bayes

### 3.5. Metric đánh giá

* Accuracy
* Precision / Recall / F1-score
* Confusion Matrix
* ROC-AUC

---

## 4. So sánh Regression vs Classification

| Tiêu chí   | Regression               | Classification            |
| ---------- | ------------------------ | ------------------------- |
| Output     | Giá trị liên tục         | Nhãn rời rạc              |
| Mục tiêu   | Dự đoán số               | Gán lớp                   |
| Thuật toán | Linear Reg, SVR, RF Regr | Logistic Reg, SVC, RF Clf |
| Metric     | MSE, RMSE, R²            | Accuracy, F1, AUC         |
| Ứng dụng   | Giá nhà, dự báo          | Nhận diện, phân loại      |

---

## 5. Cách trả lời phỏng vấn (chốt gọn)

* **Regression** dự đoán giá trị liên tục → dùng khi output là một số.
* **Classification** dự đoán lớp → dùng khi output là nhãn.

Chỉ nhìn vào dạng **y** (label) là biết bài toán thuộc loại nào.
