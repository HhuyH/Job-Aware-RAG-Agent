---
title: "Naive Bayes"
description: "Thuật toán Naive Bayes trong Machine Learning — nguyên lý, công thức, quy trình, ưu nhược điểm và ứng dụng."
tags: ["Machine Learning", "Supervised Learning", "Classification", "Naive Bayes"]
---

# Naive Bayes

Naive Bayes là nhóm thuật toán phân loại (classification) dựa trên định lý Bayes và giả định độc lập có điều kiện giữa các đặc trưng (features). Mặc dù giả định này đơn giản, mô hình vẫn hoạt động rất hiệu quả trong thực tế, đặc biệt với dữ liệu văn bản.

---

## 1. Ý tưởng chính

* Áp dụng công thức Bayes để tính xác suất một mẫu thuộc vào mỗi lớp.
* Chọn lớp có xác suất hậu nghiệm (posterior probability) cao nhất:
  [
  \hat{y} = \arg\max_y P(y|x)
  ]

Dựa trên công thức Bayes:

$$
P(y|x) = \frac{P(x|y)P(y)}{P(x)}
$$

Vì (P(x)) là hằng số cho mọi lớp nên ta tối ưu:

$$
\hat{y} = \arg\max_y P(x|y)P(y)
$$

**"Naive"**: Giả định các đặc trưng độc lập điều kiện:
$$
P(x|y) = \prod_{i=1}^{n} P(x_i|y)
$$

---

## 2. Các biến thể phổ biến

### 2.1. Gaussian Naive Bayes

Dùng cho dữ liệu liên tục.
Giả định mỗi feature theo phân phối chuẩn:

$$
P(x_i|y) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x_i - \mu)^2}{2\sigma^2}}
$$

### 2.2. Multinomial Naive Bayes

Dùng cho dữ liệu đếm (count-based) như Bag-of-Words, TF-IDF.
Rất phổ biến trong phân loại văn bản.

### 2.3. Bernoulli Naive Bayes

Dùng khi feature dạng nhị phân (0/1).
Ví dụ: một từ có xuất hiện trong văn bản hay không.

---

## 3. Quy trình huấn luyện

1. Tính **prior**: (P(y)) của từng lớp.
2. Tính **likelihood**: (P(x_i|y)) dựa trên kiểu dữ liệu (Gaussian / Multinomial / Bernoulli).
3. Với mỗi mẫu mới, tính posterior (P(y|x)).
4. Chọn lớp có xác suất lớn nhất.

---

## 4. Ưu điểm

* Rất nhanh, thậm chí nhanh hơn SVM và Logistic Regression.
* Hoạt động tốt với dữ liệu lớn và sparse (TF-IDF, BoW).
* Không cần nhiều dữ liệu để train.
* Tránh overfitting tốt.
* Dễ triển khai và giải thích.

---

## 5. Nhược điểm

* Giả định độc lập giữa các feature thường không đúng trong thực tế.
* Không phù hợp với dữ liệu có tương quan mạnh.
* Đối với Gaussian NB, phân phối không chuẩn ⇒ giảm chất lượng.

---

## 6. Ứng dụng thực tế

* Lọc spam email.
* Phân loại văn bản (news classification, sentiment analysis).
* Hệ thống gợi ý đơn giản.
* Phân tích tài liệu y tế, pháp lý.

---

## 7. Tóm tắt phỏng vấn

| Câu hỏi                      | Trả lời nhanh                         |
| ---------------------------- | ------------------------------------- |
| Tại sao gọi là "Naive"?      | Vì giả định độc lập giữa các feature. |
| Khi nào dùng Multinomial NB? | Khi dữ liệu dạng đếm (text).          |
| Gaussian NB phù hợp khi nào? | Khi feature liên tục.                 |
| Ưu điểm lớn nhất?            | Nhanh, hiệu quả, ít overfitting.      |
| Nhược điểm?                  | Giả định độc lập thiếu thực tế.       |