---

title: "Dimensionality Reduction"
description: "Tổng quan về các kỹ thuật giảm chiều trong Machine Learning."
tags: ["Machine Learning", "Unsupervised Learning", "Dimensionality Reduction"]
---

# Dimensionality Reduction

Dimensionality Reduction (giảm chiều dữ liệu) là tập các kỹ thuật nhằm giảm số lượng đặc trưng (features) trong dữ liệu nhưng vẫn giữ lại tối đa thông tin quan trọng.

Giảm chiều giúp mô hình nhanh hơn, giảm overfitting và dễ trực quan hóa.

---

## 1. Tại sao cần giảm chiều?

* **Tăng tốc độ huấn luyện** (ít feature hơn → tính toán nhẹ hơn).
* **Giảm noise**, loại bớt đặc trưng thừa.
* **Giảm overfitting**.
* **Trực quan hóa dữ liệu** (2D, 3D).
* **Tối ưu lưu trữ**.

Hiện tượng "lời nguyền chiều dữ liệu" (Curse of Dimensionality) khiến khoảng cách giữa các điểm trở nên kém ý nghĩa khi số chiều quá lớn, do đó giảm chiều là rất quan trọng.

---

## 2. Hai nhóm kỹ thuật chính

1. **Feature Selection** (chọn đặc trưng quan trọng).
2. **Feature Extraction** (tạo đặc trưng mới từ đặc trưng cũ) → PCA, t-SNE thuộc nhóm này.

---

## 3. Các thuật toán Dimensionality Reduction phổ biến

### 3.1. Principal Component Analysis (PCA)

**Loại**: Tuyến tính.

**Ý tưởng**:

* Tìm các trục mới (principal components) sao cho phương sai dữ liệu trên các trục này là lớn nhất.
* Thành phần đầu chứa nhiều thông tin nhất.

**Cách hoạt động**:

1. Chuẩn hóa dữ liệu.
2. Tính ma trận covariance.
3. Tính eigenvalues và eigenvectors.
4. Chọn k eigenvectors lớn nhất → tạo không gian mới.

**Ưu điểm**:

* Nhanh, hiệu quả.
* Phổ biến trong pipeline dữ liệu.

**Nhược điểm**:

* Chỉ mô hình hóa được quan hệ tuyến tính.
* Khó diễn giải component.

---

### 3.2. t-SNE (t-distributed Stochastic Neighbor Embedding)

**Loại**: Phi tuyến.

**Ý tưởng**:

* Giữ lại cấu trúc lân cận của dữ liệu khi giảm xuống 2D hoặc 3D.
* Thường dùng để trực quan hóa.

**Ưu điểm**:

* Hiển thị cụm đẹp, trực quan.
* Tốt cho dữ liệu phức tạp.

**Nhược điểm**:

* Chậm.
* Không phù hợp để làm input cho mô hình.
* Kết quả khó tái lập.

---

### 3.3. UMAP (Uniform Manifold Approximation and Projection)

**Loại**: Phi tuyến.

**Ý tưởng**:

* Bảo toàn cả quan hệ cục bộ lẫn toàn cục.
* Nhanh hơn và ổn định hơn t-SNE.

**Ưu điểm**:

* Tốc độ nhanh.
* Trực quan hóa đẹp.
* Kết quả ổn định.

**Nhược điểm**:

* Nhiều tham số cần điều chỉnh.

---

### 3.4. LDA (Linear Discriminant Analysis) – dùng khi có nhãn

**Loại**: Tuyến tính.

**Lưu ý**: LDA thuộc supervised learning, nhưng cũng được dùng để giảm chiều.

**Ý tưởng**:

* Tối đa hóa khả năng phân biệt giữa các lớp.
* Tìm không gian mới sao cho các lớp khác biệt rõ ràng.

**Ưu điểm**:

* Giúp mô hình phân loại tốt hơn khi dữ liệu nhiều chiều.

**Nhược điểm**:

* Chỉ dùng được khi có nhãn.

---

## 4. Bảng so sánh nhanh

| Thuật toán | Loại       | Ưu điểm           | Nhược điểm                          | Khi dùng                          |
| ---------- | ---------- | ----------------- | ----------------------------------- | --------------------------------- |
| **PCA**    | Tuyến tính | Nhanh, ổn định    | Không mô hình hóa quan hệ phi tuyến | Tiền xử lý, giảm nhiễu            |
| **t-SNE**  | Phi tuyến  | Trực quan hóa đẹp | Chậm, không dùng cho train          | Visualization 2D/3D               |
| **UMAP**   | Phi tuyến  | Nhanh, ổn định    | Nhiều tham số                       | Visualization, clustering         |
| **LDA**    | Supervised | Tối ưu phân lớp   | Cần nhãn                            | Khi giảm chiều cho classification |

