---
title: "Unsupervised Learning"
description: "Tổng quan về Unsupervised Learning, cơ chế, thuật toán và ứng dụng thực tế trong Machine Learning."
tags: ["Machine Learning", "Unsupervised Learning"]
---

# Unsupervised Learning (Học không giám sát)

**Bản chất:**  
- Dữ liệu **không có nhãn** (unlabelled data).  
- Mục tiêu là **khám phá cấu trúc tiềm ẩn**, mối quan hệ hoặc mẫu (pattern) trong dữ liệu.  
- Không có “đáp án đúng”; mô hình cố gắng tìm **cấu trúc hoặc nhóm dữ liệu** mô tả tốt nhất.

---

## 1. Cách hoạt động

- Mô hình cố gắng **nhóm** hoặc **biểu diễn** dữ liệu theo đặc điểm tương đồng.  
- Không yêu cầu nhãn đầu ra, thường dùng để **khám phá thông tin tiềm ẩn**.

---

## 2. Ví dụ thực tế

| Phương pháp                           | Mục đích / Ứng dụng                                   | Thuật toán phổ biến              |
|---------------------------------------|-------------------------------------------------------|----------------------------------|
| Clustering (Phân cụm)                 | Nhóm khách hàng có hành vi tương tự                   | K-means, DBSCAN                  |
| Dimensionality Reduction (Giảm chiều) | Nén dữ liệu hoặc tiền xử lý cho mô hình khác          | PCA, t-SNE                       |
| Association Rule Learning             | Phát hiện mối quan hệ kiểu “mua A thì thường mua B”   | Apriori, Eclat                   |

---

## 3. Ứng dụng thực tế

- **Phân khúc thị trường**: nhóm khách hàng theo hành vi, sở thích  
- **Gợi ý sản phẩm**: dựa trên hành vi mua hàng và mối quan hệ giữa sản phẩm  
- **Phát hiện bất thường (Anomaly Detection)**: xác định các điểm dữ liệu khác biệt hoặc lỗi

---

## 4. Tóm tắt nhanh cho phỏng vấn

**Câu chốt gọn:**  
- Unsupervised Learning khám phá cấu trúc trong dữ liệu không nhãn.

| Khía cạnh         | Chi tiết                                                      |
|-------------------|---------------------------------------------------------------|
| Dữ liệu           | Không có nhãn (unlabelled)                                    |
| Mục tiêu          | Khám phá mẫu, nhóm hoặc cấu trúc tiềm ẩn trong dữ liệu        |
| Ví dụ điển hình   | Phân cụm khách hàng, giảm chiều, phát hiện bất thường         |

---

## 5. Ghi chú thêm

- Hiệu quả phụ thuộc vào **chất lượng dữ liệu** và **số lượng đặc trưng**.  
- Thường dùng kết hợp với **Supervised Learning** cho tiền xử lý hoặc giảm chiều trước khi train mô hình dự đoán.
