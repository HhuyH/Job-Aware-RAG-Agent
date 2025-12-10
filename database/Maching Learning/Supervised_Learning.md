---
title: "Supervised Learning"
description: "Tổng quan về Supervised Learning, quy trình, thuật toán và ứng dụng thực tế trong Machine Learning."
tags: ["Machine Learning", "Supervised Learning"]
---

# Supervised Learning (Học có giám sát)

**Bản chất:**  
- Mô hình học từ tập dữ liệu có nhãn (labelled data), tức là mỗi mẫu đầu vào (`x`) đều đi kèm đầu ra mong muốn (`y`).  
- Mục tiêu là tìm ra hàm ánh xạ (`f(x) ≈ y`) để dự đoán nhãn của dữ liệu mới.

---

## 1. Quy trình Supervised Learning

1. **Cung cấp tập dữ liệu**: input + label  
2. **Mô hình học**: học cách khớp đầu vào với đầu ra  
3. **Đánh giá và điều chỉnh**: sử dụng dữ liệu test để giảm sai số  

---

## 2. Ví dụ thực tế

| Ứng dụng                 | Mô tả                              |
|--------------------------|------------------------------------|
| Phân loại email           | Spam / không spam                  |
| Dự đoán giá nhà           | Dựa trên các đặc trưng của căn nhà |
| Nhận diện khuôn mặt       | Xác định danh tính từ hình ảnh      |

---

## 3. Thuật toán phổ biến

- Linear Regression  
- Logistic Regression  
- Decision Tree  
- Random Forest  
- Support Vector Machine (SVM)  
- Neural Network  

---

## 4. Tóm tắt nhanh cho phỏng vấn

**Câu chốt gọn:**  
- Supervised học từ dữ liệu có nhãn để dự đoán kết quả.

| Khía cạnh         | Chi tiết                                                     |
|-------------------|--------------------------------------------------------------|
| Dữ liệu           | Có nhãn (labelled data)                                      |
| Mục tiêu          | Học quy luật từ dữ liệu đã gắn nhãn và dự đoán đầu ra mới    |
| Ví dụ điển hình   | Phân loại email, dự đoán giá, nhận diện khuôn mặt            |

---

## 5. Ghi chú thêm

- Hiệu suất mô hình cải thiện khi có nhiều dữ liệu chất lượng.  
- Việc chọn thuật toán phù hợp phụ thuộc vào loại dữ liệu và bài toán cụ thể.
