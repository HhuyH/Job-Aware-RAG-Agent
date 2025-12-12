---
title: Classification Evaluation Metrics in Deep Learning
description: Ghi chú về các metric đánh giá mô hình classification trong deep learning, công thức, ý nghĩa và cách áp dụng.
tags: [Deep Learning, Training, Evaluation, Classification, Metrics]
---

## 1. Tóm tắt khái niệm (Definition)

Các metric đánh giá classification đo lường khả năng dự đoán của mô hình, giúp so sánh và cải thiện performance.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Đánh giá mô hình classification.
* So sánh các thuật toán và hyperparameter.
* Lựa chọn model tốt nhất cho deployment.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* Dựa trên **confusion matrix**:
  $$
  CM = \begin{bmatrix} TP & FP \ FN & TN \end{bmatrix}
  $$
* Từ CM, tính các metric phổ biến:

  * Accuracy: $$\frac{TP + TN}{TP + TN + FP + FN}$$
  * Precision: $$\frac{TP}{TP + FP}$$
  * Recall: $$\frac{TP}{TP + FN}$$
  * F1-score: $$2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}$$
* Multi-class: tính macro, micro hoặc weighted average.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

* Input: predicted labels $\hat{y}$ và true labels $y$.
* Output: các metric như Accuracy, Precision, Recall, F1.
* Multi-class: tính trung bình macro/micro/weighted.

---

## 5. Ví dụ code (Code Examples)

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

y_true = [0, 1, 1, 0, 1, 0]
y_pred = [0, 1, 0, 0, 1, 1]

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print(f"Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1: {f1}")
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Accuracy misleading với dataset imbalanced.
* Không phân biệt micro/macro/weighted cho multi-class.
* Không kiểm tra metric phù hợp với business objective.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* Precision vs Recall:

  * Precision: tỷ lệ dự đoán đúng trên tổng dự đoán dương.
  * Recall: tỷ lệ dự đoán đúng trên tổng thực sự dương.
* F1-score kết hợp precision và recall, tốt cho dataset imbalanced.
* Accuracy phù hợp dataset cân bằng, đơn giản.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Spam detection, medical diagnosis, fraud detection: cần precision/recall cao.
* Multi-class classification: sử dụng macro/micro F1.
* Model selection và hyperparameter tuning dựa trên metric phù hợp.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Các metric đánh giá classification phổ biến là gì?
* Khi nào nên dùng F1-score thay vì accuracy?
* Precision và recall khác nhau thế nào?
* Multi-class metric tính như thế nào?

---

## 10. TL;DR (Short Summary)

* Dựa trên confusion matrix để tính Accuracy, Precision, Recall, F1.
* Accuracy tốt với dataset cân bằng.
* F1-score phù hợp với imbalanced dataset.
* Lựa chọn metric dựa trên yêu cầu thực tế.
