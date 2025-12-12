---
title: Image Preprocessing Basics
description: Ghi chú về các kỹ thuật tiền xử lý ảnh trong computer vision, bao gồm chuẩn hóa, resizing, augmentation và các công thức liên quan.
tags: [Computer Vision, Image Preprocessing, Deep Learning, Data Augmentation]
---

## 1. Tóm tắt khái niệm (Definition)

Image preprocessing là bước chuẩn hóa dữ liệu ảnh đầu vào để cải thiện hiệu quả học và độ ổn định của mô hình deep learning.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Chuẩn hóa kích thước ảnh cho mô hình CNN.
* Cân bằng dữ liệu qua augmentation.
* Loại bỏ nhiễu hoặc tăng độ tương phản.
* Khi cần cải thiện chất lượng dữ liệu, tốc độ học và tránh overfitting.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* **Resizing**: đưa tất cả ảnh về cùng kích thước $H \times W$.
* **Normalization**: chuyển pixel về khoảng [0,1] hoặc chuẩn hóa zero-mean.
  $$
  I_{norm} = \frac{I - \mu}{\sigma}
  $$
* **Augmentation**: xoay, lật, dịch, thay đổi brightness, zoom.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

* Resize:
  $$
  I_{resized} = \text{resize}(I, (H, W))
  $$
* Normalization:
  $$
  I_{norm} = \frac{I - \mu}{\sigma}
  $$
* Augmentation ví dụ horizontal flip:
  $$
  I_{flipped} = \text{flip}(I_{resized})
  $$

---

## 5. Ví dụ code (Code Examples)

```python
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Normalization and augmentation
datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True
)

# Load example image
image = tf.random.uniform(shape=(256,256,3))
image = tf.expand_dims(image, 0)  # batch dimension
aug_iter = datagen.flow(image)
augmented_image = next(aug_iter)
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Không chuẩn hóa input → learning chậm hoặc gradient không ổn định.
* Augmentation quá mạnh → ảnh giả tạo sai, gây overfitting.
* Kích thước ảnh không đồng nhất → lỗi input vào CNN.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* Preprocessing vs Augmentation:

  * Preprocessing: chuẩn hóa, resizing, denoising.
  * Augmentation: tăng số lượng và đa dạng dữ liệu.
* Normalization vs Standardization:

  * Normalization: pixel về [0,1].
  * Standardization: zero-mean, unit variance.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Chuẩn bị dataset cho CNN, ResNet, EfficientNet.
* Data augmentation giúp cải thiện generalization.
* Tiền xử lý là bước quan trọng trong pipeline computer vision.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Tại sao phải chuẩn hóa ảnh?
* Các phương pháp augmentation phổ biến?
* Normalization khác standardization thế nào?
* Lý do resize ảnh trước khi đưa vào CNN?

---

## 10. TL;DR (Short Summary)

* Image preprocessing: resize, normalization, augmentation.
* Chuẩn hóa pixel để gradient ổn định.
* Augmentation tăng cường dữ liệu và tránh overfitting.
* Bước quan trọng trong pipeline computer vision.
