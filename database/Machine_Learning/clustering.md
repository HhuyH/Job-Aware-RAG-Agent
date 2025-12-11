---

title: "Clustering"
description: "Tổng quan và các thuật toán Clustering trong Machine Learning."
tags: ["Machine Learning", "Unsupervised Learning", "Clustering"]
-----------------------------------------------------------------

# Clustering

Clustering (phân cụm) là kỹ thuật học không giám sát nhằm nhóm các điểm dữ liệu thành các cụm (cluster) dựa trên mức độ tương đồng. Mỗi cụm đại diện cho một nhóm có đặc điểm chung, không cần nhãn đầu vào.

---

## 1. Mục tiêu

* Tìm cấu trúc ẩn trong dữ liệu.
* Gom nhóm các điểm có đặc tính tương tự.
* Hỗ trợ phân tích, tiền xử lý và khám phá dữ liệu.

---

## 2. Ứng dụng thực tế

* Phân khúc khách hàng.
* Gợi ý sản phẩm.
* Phát hiện bất thường (anomaly detection).
* Tối ưu mạng, phân tích hành vi người dùng.

---

## 3. Các thuật toán Clustering phổ biến

### 3.1. K-Means

**Ý tưởng**: Tìm (k) tâm cụm (centroid) sao cho tổng bình phương khoảng cách các điểm tới tâm gần nhất là nhỏ nhất.

**Quy trình**:

1. Chọn số cụm (k).
2. Khởi tạo ngẫu nhiên (k) centroid.
3. Gán mỗi điểm vào centroid gần nhất.
4. Cập nhật lại centroid.
5. Lặp cho đến khi hội tụ.

**Ưu điểm**:

* Nhanh, đơn giản, dễ triển khai.

**Nhược điểm**:

* Nhạy với outlier.
* Phải chọn (k) trước.
* Chỉ tìm được cụm có dạng hình cầu.

---

### 3.2. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

**Ý tưởng**: Nhóm các điểm có mật độ dày đặc, tách biệt bởi vùng mật độ thấp.

**Thành phần**:

* `eps`: bán kính lân cận.
* `minPts`: số điểm tối thiểu để tạo cụm.

**Ưu điểm**:

* Phát hiện cụm có hình dạng bất kỳ.
* Tốt với dữ liệu có nhiễu.

**Nhược điểm**:

* Khó chọn tham số `eps` và `minPts`.
* Hoạt động kém khi mật độ không đồng đều.

---

### 3.3. Hierarchical Clustering

**Ý tưởng**: Xây dựng cây phân cấp (dendrogram) để biểu diễn sự tương đồng.

**Phương pháp**:

* *Agglomerative* (từ dưới lên): bắt đầu từ từng điểm, hợp nhất dần.
* *Divisive* (từ trên xuống): bắt đầu từ một cụm lớn rồi chia nhỏ.

**Ưu điểm**:

* Không cần chọn số cụm trước.
* Nhìn dendrogram để hiểu cấu trúc dữ liệu.

**Nhược điểm**:

* Tốn chi phí tính toán.

---

### 3.4. Gaussian Mixture Model (GMM)

**Ý tưởng**: Giả định dữ liệu được tạo thành từ nhiều phân phối Gaussian.

**Cách hoạt động**:

* Dùng thuật toán Expectation-Maximization (EM) để ước lượng tham số.
* Cho phép mỗi điểm thuộc nhiều cụm với xác suất khác nhau.

**Ưu điểm**:

* Linh hoạt hơn K-Means.
* Mô hình hóa cụm không hình cầu.

**Nhược điểm**:

* Nhạy với khởi tạo.
* Tốn chi phí tối ưu.

---

### 3.5. K-Means++

**Ý tưởng**: Cải thiện bước khởi tạo centroid của K-Means nhằm giảm nguy cơ rơi vào nghiệm kém.

**Cách hoạt động**:

1. Chọn ngẫu nhiên 1 centroid đầu tiên.
2. Với mỗi điểm còn lại, tính xác suất chọn làm centroid mới tỉ lệ thuận với bình phương khoảng cách đến centroid gần nhất.
3. Lặp cho đến khi có đủ (k) centroid.
4. Chạy K-Means như bình thường.

**Ưu điểm**:

* Hội tụ nhanh hơn.
* Ít rủi ro rơi vào local minima.
* Chất lượng cụm tốt hơn K-Means thường.

**Nhược điểm**:

* Tốn thời gian khởi tạo hơn.

---

## 4. Bảng so sánh nhanh

| Thuật toán       | Ưu điểm                                | Nhược điểm                       | Khi dùng                                |
| ---------------- | -------------------------------------- | -------------------------------- | --------------------------------------- |
| **K-Means**      | Nhanh, đơn giản                        | Chỉ cho cụm hình cầu, nhạy noise | Dữ liệu lớn, cụm rõ ràng                |
| **DBSCAN**       | Tìm cụm mọi hình dạng, xử lý noise tốt | Khó chọn tham số                 | Phát hiện outlier, cụm phức tạp         |
| **Hierarchical** | Không cần chọn k, trực quan            | Chậm                             | Phân tích dữ liệu nhỏ/ trung bình       |
| **GMM**          | Cụm mềm, linh hoạt                     | Tốn chi phí                      | Khi muốn mô hình hóa phân phối xác suất |