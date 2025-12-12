---

title: CNN Architectures
description: Ghi chú chi tiết về các kiến trúc CNN phổ biến như VGG, ResNet, Inception, bao gồm cấu trúc layer, skip connection, batch normalization và ứng dụng thực tế.
tags: [CNN, ResNet, VGG, Inception, Deep Learning, Neural Network]
------------------------------------------------------------------

## 1. Tóm tắt khái niệm (Definition)

Các kiến trúc CNN là các thiết kế mạng convolution khác nhau, tối ưu cho các loại dữ liệu và nhiệm vụ khác nhau. Bao gồm việc sắp xếp layer, kernel size, pooling, skip connection, normalization.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Nhận diện và phân loại ảnh phức tạp.
* Object detection và segmentation.
* Khi muốn cải thiện hiệu suất hoặc giảm overfitting so với CNN cơ bản.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* Layer nối tiếp hoặc có skip connections.
* Normalization layer (BatchNorm) giúp ổn định learning.
* Pooling layer giảm chiều dữ liệu, giữ thông tin quan trọng.
* Fully connected layer cuối cùng để dự đoán.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

$$
Z^{[l]} = X * W^{[l]} + b^{[l]}
$$
$$
A^{[l]} = f(Z^{[l]})
$$
Với skip connection (ResNet):
$$
A^{[l+1]} = f(Z^{[l+1]} + A^{[l]})
$$

---

## 5. Ví dụ code (Code Examples)

```python
import tensorflow as tf
from tensorflow.keras import layers, models

# Example ResNet block
inputs = tf.keras.Input(shape=(32,32,3))
x = layers.Conv2D(64, (3,3), activation='relu', padding='same')(inputs)
x = layers.BatchNormalization()(x)
x_res = layers.Conv2D(64, (3,3), padding='same')(x)
x = layers.Add()([x, x_res])
x = layers.ReLU()(x)
model = models.Model(inputs, x)
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Overfitting khi mạng quá sâu.
* Vanishing gradient nếu không dùng skip connections cho mạng sâu.
* Pooling quá mức → mất thông tin chi tiết.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* Basic CNN vs ResNet vs VGG vs Inception:

  * Basic CNN: layer nối tiếp, đơn giản.
  * VGG: nhiều layer nhỏ 3x3, đơn giản nhưng sâu.
  * ResNet: skip connections, giảm vanishing gradient.
  * Inception: multi-scale filter, giảm tham số mà giữ hiệu suất.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* VGG/ResNet/Inception dùng trong ImageNet competition.
* ResNet thường dùng cho các dự án detection/segmentation.
* Inception hoặc EfficientNet tối ưu tốc độ và accuracy.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Các kiến trúc CNN khác nhau điểm gì?
* Skip connection giúp gì trong ResNet?
* BatchNorm hoạt động thế nào?
* Khi nào chọn VGG thay vì ResNet?

---

## 10. TL;DR (Short Summary)

* CNN architectures khác nhau tùy mục tiêu, độ sâu, hiệu suất.
* ResNet dùng skip connections giảm vanishing gradient.
* VGG sâu, simple 3x3 conv layers.
* Inception dùng multi-scale filter tối ưu performance.
* BatchNorm giúp ổn định learning.
