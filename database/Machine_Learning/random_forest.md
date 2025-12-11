---

title: "Random Forest"
description: "Thuật toán Random Forest trong Machine Learning."
tags: ["Machine Learning", "Random Forest"]
---

# Random Forest

## 1. Khái niệm

Random Forest là thuật toán **Ensemble Learning** thuộc nhóm **Supervised Learning**, kết hợp nhiều Decision Tree để tạo ra mô hình mạnh hơn, ổn định hơn và ít overfitting hơn.

Nó hoạt động dựa trên ý tưởng: "Nhiều mô hình yếu → tạo thành một mô hình mạnh".

---

## 2. Bản chất hoạt động

Random Forest xây dựng nhiều Decision Tree độc lập và kết hợp kết quả:

* **Classification** → dùng **voting** (đa số phiếu).
* **Regression** → dùng **average** (trung bình).

---

## 3. Quy trình Random Forest

1. Lấy nhiều mẫu ngẫu nhiên từ dữ liệu gốc (bootstrap sampling).
2. Với mỗi mẫu bootstrap → xây một Decision Tree.
3. Tại mỗi node, chọn ngẫu nhiên một tập con feature → giảm tương quan giữa các cây.
4. Kết hợp kết quả của tất cả các cây.

---

## 4. Tại sao Random Forest mạnh hơn Decision Tree?

* Cây đơn → dễ overfit.
* Random Forest dùng nhiều cây → giảm phương sai (variance).
* Random sampling giúp các cây đa dạng → tăng khả năng tổng quát.

---

## 5. Ưu điểm

* Giảm overfitting hiệu quả.
* Làm việc tốt với dữ liệu phức tạp.
* Xử lý cả classification và regression.
* Ít yêu cầu tuning.
* Có thể tính **feature importance**.

---

## 6. Nhược điểm

* Mất tính diễn giải (giải thích) so với Decision Tree.
* Training tốn thời gian nếu số cây lớn.
* Khó triển khai real-time với mô hình rất lớn.

---

## 7. Hyperparameters quan trọng

* `n_estimators`: số lượng cây.
* `max_depth`: giới hạn chiều cao mỗi cây.
* `max_features`: số lượng feature được chọn ngẫu nhiên tại mỗi split.
* `min_samples_split`: số mẫu tối thiểu để tách.
* `min_samples_leaf`: số mẫu tối thiểu trong mỗi leaf.

---

## 8. Ứng dụng thực tế

* Dự đoán rủi ro tín dụng.
* Phát hiện gian lận.
* Phân loại khách hàng.
* Dự đoán giá nhà hoặc doanh thu.
* Phân tích đặc trưng và chọn feature.

---

## 9. Cách nhận biết khi nào dùng Random Forest

Dùng khi:

* Decision Tree bị overfit.
* Dữ liệu có nhiều feature.
* Muốn có mô hình mạnh, ít tuning.
* Không yêu cầu giải thích chi tiết.

---

## 10. Metric đánh giá

### Classification

* Accuracy
* Precision / Recall / F1
* ROC-AUC

### Regression

* MSE / RMSE
* MAE
* R²

---

## 11. Cách trả lời phỏng vấn (chốt gọn)

* Random Forest là tập hợp nhiều Decision Tree để giảm variance và tránh overfitting.
* Dùng bootstrap sampling và random feature selection để tạo mô hình mạnh và ổn định.
* Hoạt động tốt với nhiều bài toán và thường outperform Decision Tree.
