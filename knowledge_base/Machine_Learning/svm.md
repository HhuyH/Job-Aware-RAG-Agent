---
title: "Support Vector Machine (SVM)"
description: "Thuật toán SVM cho Classification và Regression."
tags: ["Machine Learning", "SVM", "SVC", "SVR"]
---

# Support Vector Machine (SVM)

## 1. Khái niệm

Support Vector Machine (SVM) là thuật toán **Supervised Learning** dùng cho cả:

* **Classification** → SVC
* **Regression** → SVR

Mục tiêu của SVM: tìm **siêu phẳng tối ưu (optimal hyperplane)** để phân tách dữ liệu sao cho **margin** lớn nhất.

---

## 2. Bản chất hoạt động của SVM

SVM tìm đường phân cách sao cho:

* Khoảng cách từ siêu phẳng tới điểm gần nhất ở mỗi lớp (support vectors) là **lớn nhất**.
* Điều này giúp mô hình ổn định, ít overfitting.

### **Hard Margin**

* Dữ liệu phân tách tuyến tính hoàn hảo.
* Không linh hoạt, nhạy với noise.

### **Soft Margin**

* Cho phép một số điểm sai lệch.
* Dùng thực tế nhiều nhất.

---

## 3. Kernel Trick (điểm mạnh lớn nhất)

Khi dữ liệu **không tuyến tính**, SVM dùng kernel để "đưa dữ liệu vào không gian mới" tuyến tính hơn.

Các kernel phổ biến:

* **Linear Kernel** → dữ liệu gần tuyến tính
* **RBF Kernel** → mạnh nhất, mặc định
* **Polynomial Kernel** → dữ liệu có quan hệ đa thức
* **Sigmoid Kernel** → ít dùng

*Ý tưởng:* thay vì transform dữ liệu thủ công, kernel tính toán trực tiếp inner product trong không gian cao chiều → nhanh và hiệu quả.

---

## 4. Ứng dụng SVM

* Phân loại văn bản (text classification)
* Nhận diện khuôn mặt
* Phân loại spam
* Phân loại hình ảnh
* Dự đoán regression với dữ liệu phi tuyến (SVR)

---

## 5. Hyperparameters quan trọng

### **1. C (regularization)**

* C nhỏ → margin rộng, chấp nhận nhiều sai lệch → giảm overfitting.
* C lớn → margin hẹp, ít chấp nhận sai → dễ overfit.

### **2. Kernel**

* linear, rbf, poly, sigmoid.

### **3. Gamma (với RBF)**

* Gamma nhỏ → ảnh hưởng rộng → mô hình mượt.
* Gamma lớn → ảnh hưởng hẹp → dễ overfit.

### **4. Degree (poly kernel)**

* Độ bậc của đa thức.

---

## 6. Ưu điểm

* Rất mạnh trong không gian chiều cao.
* Hoạt động tốt với dữ liệu phi tuyến nhờ kernel trick.
* Ít bị overfitting.
* Là lựa chọn tốt khi dữ liệu không quá lớn.

---

## 7. Nhược điểm

* Training chậm với dữ liệu rất lớn.
* Nhạy với lựa chọn kernel.
* Không phù hợp với tập dữ liệu triệu mẫu.

---

## 8. Metric đánh giá

### Classification (SVC)

* Accuracy
* Precision / Recall / F1-score
* ROC-AUC

### Regression (SVR)

* MSE / RMSE
* MAE
* R²

---

## 9. Cách trả lời phỏng vấn (chốt gọn)

* SVM tìm siêu phẳng tối ưu để phân tách dữ liệu với margin lớn nhất.
* Kernel Trick là điểm mạnh nhất giúp xử lý dữ liệu phi tuyến.
* Strong khi dữ liệu không quá lớn và có cấu trúc phức tạp.
* Có hai dạng: **SVC** cho classification và **SVR** cho regression.
