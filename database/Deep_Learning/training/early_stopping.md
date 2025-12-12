---
title: Early Stopping in Deep Learning
description: Ghi chú về kỹ thuật Early Stopping trong deep learning, cách hoạt động, các tham số quan trọng và ứng dụng để tránh overfitting.
tags: [Deep Learning, Training, Early Stopping, Overfitting, Optimization]
---

## 1. Tóm tắt khái niệm (Definition)

Early stopping là kỹ thuật dừng training trước khi hết số epoch để tránh overfitting, dựa trên hiệu suất trên validation set.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Giảm overfitting khi mô hình bắt đầu học noise.
* Tiết kiệm thời gian và tài nguyên khi training.
* Kết hợp với model checkpoint để lưu best model.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* Theo dõi metric trên validation set, ví dụ: loss hoặc accuracy.
* Dừng training nếu metric không cải thiện sau một số epoch (`patience`).
* Pseudocode:
$$
\text{if validation_loss_{current} > validation_loss_{best} for patience epochs: stop training}
$$

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

* Các tham số quan trọng:

  * `monitor`: metric cần theo dõi (loss/accuracy).
  * `patience`: số epoch chờ trước khi dừng.
  * `min_delta`: cải thiện tối thiểu được coi là tiến bộ.
  * `restore_best_weights`: có khôi phục weights tốt nhất không.

---

## 5. Ví dụ code (Code Examples)

```python
from tensorflow.keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=5,
    min_delta=0.001,
    restore_best_weights=True
)

history = model.fit(
    x_train, y_train,
    validation_split=0.2,
    epochs=100,
    callbacks=[early_stopping]
)
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Patience quá nhỏ → dừng quá sớm, underfitting.
* Patience quá lớn → vẫn overfitting.
* Không kết hợp với checkpoint → có thể không lưu được model tốt nhất.
* Không chuẩn hóa dữ liệu → validation metric không phản ánh đúng.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* Early Stopping vs Regular Training:

  * Early stopping: dừng sớm để tránh overfitting.
  * Regular: train đủ số epoch, có thể overfit.
* Early Stopping vs Model Checkpointing:

  * Early stopping: quyết định khi nào dừng.
  * Checkpointing: lưu trạng thái tốt nhất.
  * Kết hợp cả hai để dừng training và khôi phục best model.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Training deep network với dataset nhỏ hoặc mô hình phức tạp.
* Kết hợp với data augmentation và regularization.
* Thường sử dụng cùng model checkpoint để lưu best weights.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Early stopping là gì và khi nào dùng?
* Các tham số quan trọng của Early Stopping?
* Early stopping giúp tránh overfitting thế nào?
* Kết hợp với checkpoint ra sao để tối ưu?

---

## 10. TL;DR (Short Summary)

* Dừng training trước khi overfitting xảy ra.
* Theo dõi validation metric, dừng sau `patience` epoch không cải thiện.
* Kết hợp checkpoint để lưu best model.
* Giúp tiết kiệm thời gian và cải thiện generalization.
