---
title: "Association Rule Learning"
description: "Tổng quan về luật kết hợp trong Machine Learning."
tags: ["Machine Learning", "Unsupervised Learning", "Association Rule Learning"]
---

# Association Rule Learning

Association Rule Learning là nhóm thuật toán dùng để tìm ra các mối liên hệ tiềm ẩn giữa các mục (items) trong một tập dữ liệu lớn. Kỹ thuật này đặc biệt phổ biến trong phân tích thị trường (Market Basket Analysis).

Ví dụ: "Khách mua **A** thường mua thêm **B**".

Mục tiêu là phát hiện các luật (rules) hữu ích dạng:
[ A \rightarrow B ]

---

## 1. Các khái niệm nền tảng

### 1.1. Itemset

Tập các items được mua hoặc xuất hiện cùng nhau.

### 1.2. Support

Tần suất itemset xuất hiện trong toàn bộ dữ liệu.

$$
Support(A) = \frac{\text{số giao dịch chứa A}}{\text{tổng giao dịch}}
$$

### 1.3. Confidence

Xác suất xảy ra B khi A xảy ra.

$$
Confidence(A \rightarrow B) = \frac{Support(A \cup B)}{Support(A)}
$$

### 1.4. Lift

Đo lường độ mạnh của mối quan hệ.

$$
Lift(A \rightarrow B) = \frac{Confidence(A \rightarrow B)}{Support(B)}
$$

* Lift > 1: A và B có tương quan dương.
* Lift = 1: Độc lập.
* Lift < 1: Tương quan âm.

---

## 2. Các thuật toán phổ biến

### 2.1. Apriori

**Ý tưởng**:

* Tạo itemset từ nhỏ → lớn.
* Loại bỏ sớm các itemset có support thấp (downward closure property).

**Ưu điểm**:

* Dễ hiểu.

**Nhược điểm**:

* Chậm khi dữ liệu lớn.
* Tốn nhiều lần quét database.

---

### 2.2. FP-Growth

**Ý tưởng**:

* Không tạo candidate nhiều như Apriori.
* Dùng cấu trúc FP-Tree để nén dữ liệu thành dạng cây.
* Khai thác trực tiếp các mẫu thường xuyên.

**Ưu điểm**:

* Nhanh hơn Apriori rất nhiều.
* Phù hợp dữ liệu lớn.

**Nhược điểm**:

* Khó cài đặt hơn.

---

## 3. Ví dụ thực tế

* Gợi ý sản phẩm: mua laptop → gợi ý túi chống sốc.
* Phát hiện gian lận: các pattern bất thường.
* Retail: phân tích hành vi mua sắm.

---

## 4. Bảng so sánh

| Thuật toán    | Cơ chế                   | Tốc độ | Ưu điểm               | Nhược điểm       |
| ------------- | ------------------------ | ------ | --------------------- | ---------------- |
| **Apriori**   | Sinh candidate           | Chậm   | Dễ hiểu               | Tốn quét dữ liệu |
| **FP-Growth** | Nén dữ liệu bằng FP-tree | Nhanh  | Hiệu quả với big data | Cài đặt phức tạp |
