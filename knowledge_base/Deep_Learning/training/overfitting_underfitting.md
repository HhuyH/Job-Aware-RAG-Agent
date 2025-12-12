---
title: Overfitting and Underfitting in Deep Learning
description: Ghi chú về hiện tượng overfitting và underfitting trong deep learning, nguyên nhân, dấu hiệu nhận biết, và cách khắc phục.
tags: [Deep Learning, Training, Overfitting, Underfitting, Model Generalization]
---

## 1. Tóm tắt khái niệm (Definition)

* **Overfitting**: mô hình học quá kỹ dữ liệu huấn luyện, dẫn đến khả năng generalization kém trên dữ liệu mới.
* **Underfitting**: mô hình chưa học đủ dữ liệu, hiệu suất thấp cả trên train và test.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Hiểu vấn đề generalization trong deep learning.
* Phát hiện và khắc phục để cải thiện accuracy trên dữ liệu unseen.
* Khi training model, cần cân bằng giữa underfitting và overfitting.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* **Bias-Variance Trade-off**:
  $$
  Error = Bias^2 + Variance + IrreducibleError
  $$
* Overfitting: bias thấp, variance cao.
* Underfitting: bias cao, variance thấp.
* Khi training, loss trên train giảm nhưng loss trên validation tăng → overfitting.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

* Biểu đồ learning curves:

  * Train loss vs epochs
  * Validation loss vs epochs
* Nhận biết:

  * Train loss giảm, validation loss tăng → overfitting.
  * Cả train và validation loss cao → underfitting.

---

## 5. Ví dụ code (Code Examples)

```python
import matplotlib.pyplot as plt

# Giả lập learning curves
epochs = range(1, 21)
train_loss = [0.9,0.7,0.5,0.3,0.2,0.15,0.12,0.10,0.08,0.07,0.06,0.05,0.05,0.04,0.04,0.03,0.03,0.03,0.02,0.02]
val_loss = [1.0,0.9,0.8,0.7,0.6,0.5,0.45,0.40,0.38,0.36,0.35,0.34,0.36,0.38,0.40,0.42,0.45,0.48,0.50,0.52]

plt.plot(epochs, train_loss, 'b-', label='Train Loss')
plt.plot(epochs, val_loss, 'r-', label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Quá nhiều epochs → overfitting.
* Mạng quá nhỏ / quá ít layers → underfitting.
* Không chuẩn hóa dữ liệu → ảnh hưởng convergence.
* Feature quá ít hoặc quá nhiễu → underfitting.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* Overfitting vs Underfitting:

  * Overfitting: train accuracy cao, test accuracy thấp.
  * Underfitting: train accuracy thấp, test accuracy thấp.
* Bias vs Variance:

  * High bias → underfitting
  * High variance → overfitting

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Theo dõi learning curves để phát hiện overfitting.
* Dùng regularization, dropout, data augmentation để giảm overfitting.
* Tăng model capacity hoặc feature để giảm underfitting.
* Early stopping kết hợp validation loss giúp cân bằng.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Hiện tượng overfitting là gì và làm sao nhận biết?
* Biện pháp giảm overfitting trong deep learning?
* Underfitting khác overfitting thế nào?
* Bias-Variance trade-off liên quan ra sao đến over/underfitting?

---

## 10. TL;DR (Short Summary)

* Overfitting: học quá kỹ, variance cao, generalization kém.
* Underfitting: chưa học đủ, bias cao, accuracy thấp.
* Bias-variance trade-off quyết định cân bằng.
* Giải pháp: regularization, dropout, data augmentation, early stopping, tăng/decrease model capacity.
