---
title: "Decision Tree"
description: "Thuật toán Decision Tree trong Machine Learning."
tags: ["Machine Learning", "Decision Tree"]
---

# Decision Tree

## 1. Khái niệm

Decision Tree là thuật toán thuộc nhóm **Supervised Learning**, dùng cho cả **Classification** và **Regression**. Mô hình hoạt động bằng cách chia dữ liệu thành các nhánh dựa trên điều kiện, tạo thành cấu trúc giống cây gồm **node**, **branch**, và **leaf**.

---

## 2. Cấu trúc cây quyết định

* **Root Node**: điểm bắt đầu, chứa toàn bộ dữ liệu.
* **Internal Node**: nút kiểm tra điều kiện (feature).
* **Leaf Node**: nút kết luận → class label hoặc giá trị dự đoán.
* **Branch**: đường nối thể hiện lựa chọn theo điều kiện.

---

## 3. Cách hoạt động

1. Chọn feature tốt nhất để chia dữ liệu.
2. Tạo một node với điều kiện rẽ nhánh.
3. Lặp lại cho từng nhánh đến khi đạt điều kiện dừng.
4. Node cuối trở thành leaf node.

---

## 4. Tiêu chí chọn feature (Split Criteria)

### Đối với Classification

* **Gini Impurity**
* **Entropy / Information Gain**

### Đối với Regression

* **MSE (Mean Squared Error)**
* **MAE (Mean Absolute Error)**

---

## 5. Ưu điểm

* Dễ hiểu, trực quan.
* Không cần chuẩn hóa dữ liệu.
* Xử lý được dữ liệu dạng số và dạng phân loại.
* Hoạt động tốt khi quan hệ phi tuyến.

---

## 6. Nhược điểm

* Dễ overfitting nếu không cắt tỉa (pruning).
* Nhạy với nhiễu và outlier.
* Thay đổi nhỏ trong dữ liệu có thể làm thay đổi cấu trúc cây.

---

## 7. Kỹ thuật cải thiện

* **Pruning (Cắt tỉa)**: giảm độ sâu cây để tránh overfitting.
* **Max Depth**: giới hạn chiều cao cây.
* **Min Samples Split / Leaf**: yêu cầu số mẫu tối thiểu để split.
* **Feature Importance**: đánh giá độ quan trọng của từng feature.

---

## 8. Ứng dụng thực tế

* Phân loại khách hàng.
* Chẩn đoán bệnh.
* Dự đoán rủi ro tín dụng.
* Hệ thống hỗ trợ ra quyết định.

---

## 9. Cách nhận biết khi nào dùng Decision Tree

Dùng khi:

* Cần mô hình dễ diễn giải.
* Dữ liệu có quan hệ phi tuyến.
* Không muốn chuẩn hóa dữ liệu.
* Cần giải thích quyết định cho stakeholder.

---

## 10. Metric đánh giá

### Đối với Classification

* Accuracy
* Precision / Recall / F1
* Confusion Matrix

### Đối với Regression

* MSE / RMSE
* MAE
* R² Score

---

## 11. Cách trả lời phỏng vấn (chốt gọn)

* Decision Tree là mô hình phân loại hoặc hồi quy dựa trên việc chia dữ liệu thành các nhánh theo điều kiện.
* Dễ hiểu, trực quan, nhưng dễ overfit nếu không cắt tỉa.
* Tiêu chí split: Gini / Entropy cho classification, MSE cho regression.
