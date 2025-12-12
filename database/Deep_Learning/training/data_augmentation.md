---
title: Data Augmentation in Deep Learning
description: Ghi chú về kỹ thuật Data Augmentation trong deep learning, các phương pháp phổ biến, công thức, và ứng dụng thực tế.
tags: [Deep Learning, Training, Data Augmentation, Computer Vision, Overfitting]
---

## 1. Tóm tắt khái niệm (Definition)

Data augmentation là kỹ thuật tạo ra các biến thể mới của dữ liệu huấn luyện hiện có nhằm tăng số lượng dữ liệu và cải thiện khả năng generalization của mô hình.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Giảm overfitting bằng cách cung cấp nhiều dữ liệu hơn.
* Tăng khả năng generalization cho mô hình.
* Thường dùng trong computer vision và NLP.
* Khi dataset nhỏ hoặc không đa dạng.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* Áp dụng các **transformations** trên dữ liệu gốc:

  * Images: rotation, flipping, scaling, cropping, brightness adjustment.
  * Text: synonym replacement, random insertion, back translation.
* Mỗi transformation tạo ra **dữ liệu mới giả lập** nhưng vẫn giữ nhãn.
* Khi training, mô hình học từ dữ liệu mở rộng.
* Kỹ thuật phổ biến:
  $$
  x_{aug} = T(x), \quad y_{aug} = y
  $$
  trong đó $T$ là transformation.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

* Input: dữ liệu huấn luyện $(x_i, y_i)$
* Transformation $T$: áp dụng trên từng sample hoặc batch.
* Output: $(x_i', y_i')$ tăng số lượng dữ liệu.

---

## 5. Ví dụ code (Code Examples)

```python
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True,
    brightness_range=[0.8,1.2]
)

for x_batch, y_batch in datagen.flow(x_train, y_train, batch_size=32):
    # dùng x_batch, y_batch để training
    break
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Quá nhiều augmentation → dữ liệu không thực tế.
* Không áp dụng augmentation đều cho train/validation → bias.
* Một số transformation thay đổi nhãn (vd. rotation với text).

---

## 7. So sánh với khái niệm liên quan (Comparison)

* Data augmentation vs synthetic data generation:

  * Augmentation: biến thể từ dữ liệu gốc.
  * Synthetic data: tạo dữ liệu hoàn toàn mới.
* Overfitting vs underfitting:

  * Augmentation giúp giảm overfitting.
  * Không tác động nhiều đến underfitting.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Computer vision: image classification, object detection, segmentation.
* NLP: text classification, translation.
* Medical imaging: MRI, CT scan dataset nhỏ.
* Robotics: tăng dữ liệu huấn luyện cho perception.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Data augmentation là gì và mục đích của nó?
* Các phương pháp phổ biến trong hình ảnh là gì?
* Data augmentation giúp giảm overfitting như thế nào?
* Khi nào không nên dùng data augmentation?

---

## 10. TL;DR (Short Summary)

* Tạo biến thể dữ liệu từ dataset gốc.
* Mục đích: tăng dữ liệu, giảm overfitting, cải thiện generalization.
* Methods: rotation, flipping, scaling, brightness, synonym replacement.
* Áp dụng phổ biến trong vision, NLP, medical imaging, robotics.
