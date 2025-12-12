---
title: Batch Size Effects in Deep Learning
description: Ghi chú về ảnh hưởng của batch size trong training deep learning, tác động đến gradient, convergence, generalization và cách lựa chọn batch size.
tags: [Deep Learning, Training, Batch Size, Optimization, Gradient Descent]
---

## 1. Tóm tắt khái niệm (Definition)

Batch size là số lượng mẫu dữ liệu được dùng để tính gradient và cập nhật trọng số trong mỗi bước training của mô hình.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Điều chỉnh tốc độ học và ổn định của gradient descent.
* Tác động đến memory usage và thời gian training.
* Khi muốn cân bằng giữa convergence và generalization.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* Gradient được tính trên batch:
  $$

\theta = \theta - \eta \cdot \frac{1}{m} \sum_{i=1}^{m} \nabla_\theta L(x_i, y_i)
$$

* Với $m$ là batch size, $\eta$ là learning rate, $L$ là loss function.
* **Mini-batch gradient descent**: batch size >1 và < dataset size.
* Batch size lớn → gradient ổn định nhưng memory cao.
* Batch size nhỏ → gradient noisy nhưng có thể giúp escape local minima.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

* Options:

  * Stochastic Gradient Descent (SGD): batch size = 1.
  * Mini-batch SGD: 1 < batch size < dataset size.
  * Full-batch: batch size = dataset size.

---

## 5. Ví dụ code (Code Examples)

```python
import tensorflow as tf

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Training with different batch sizes
history_small = model.fit(x_train, y_train, epochs=20, batch_size=16, validation_split=0.2)
history_large = model.fit(x_train, y_train, epochs=20, batch_size=128, validation_split=0.2)
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Batch size quá nhỏ → gradient noisy, training chậm.
* Batch size quá lớn → memory overflow, kém generalization.
* Không điều chỉnh learning rate tương ứng với batch size → không tối ưu.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* Small batch vs Large batch:

  * Small batch: noisy gradient, tốt cho generalization, training chậm.
  * Large batch: gradient ổn định, training nhanh, có thể bị overfitting.
* Relation with learning rate:

  * Large batch thường cần learning rate lớn hơn.
  * Small batch có thể dùng learning rate nhỏ hơn.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Tùy thuộc vào memory của GPU/TPU.
* Batch size nhỏ + augmentation + regularization → giảm overfitting.
* Batch size lớn khi dataset lớn, cần training nhanh với hardware mạnh.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Batch size là gì và ảnh hưởng đến training ra sao?
* Mini-batch gradient descent khác gì với SGD và full-batch?
* Tác động của batch size đến generalization và convergence?
* Khi nào nên chọn batch size nhỏ, khi nào nên chọn lớn?

---

## 10. TL;DR (Short Summary)

* Batch size quyết định số mẫu mỗi bước gradient.
* Nhỏ → noisy gradient, tốt cho generalization.
* Lớn → gradient ổn định, training nhanh, memory cao.
* Lựa chọn batch size kết hợp learning rate và hardware constraints.
