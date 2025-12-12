---
title: U-Net Architecture Basics
description: Ghi chú về kiến trúc U-Net trong image segmentation, cấu trúc encoder-decoder với skip connections, loss function và ứng dụng.
tags: [U-Net, Segmentation, Computer Vision, Deep Learning, CNN]
---

## 1. Tóm tắt khái niệm (Definition)

U-Net là kiến trúc mạng CNN dùng cho image segmentation, nổi bật với cấu trúc encoder-decoder và skip connections giúp giữ thông tin chi tiết của ảnh.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Medical imaging: segmentation mô bệnh, organ detection.
* Satellite imagery: phân loại vùng đất, nước, rừng.
* Robotics: phân đoạn vật thể để thao tác.
* Khi cần giữ chi tiết cục bộ và học phụ thuộc toàn cục.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* **Encoder (contracting path)**: chuỗi conv + maxpool giảm kích thước và trích xuất feature.
* **Decoder (expanding path)**: chuỗi upsampling + conv, kết hợp skip connections.
* Skip connections nối feature map tương ứng của encoder vào decoder.
* Output: segmentation map với softmax activation.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

* Input: $I \in \mathbb{R}^{H \times W \times C}$
* Encoder:
  $$
  F_{enc}^l = Conv(Pool(F_{enc}^{l-1}))
  $$
* Decoder:
  $$
  F_{dec}^l = Conv(Up(F_{dec}^{l+1}) \oplus F_{enc}^l)
  $$
* Output:
  $$
  S = \text{softmax}(F_{dec}^0)
  $$

---

## 5. Ví dụ code (Code Examples)

```python
import tensorflow as tf
from tensorflow.keras import layers, models

inputs = tf.keras.Input(shape=(128,128,3))
# Encoder
c1 = layers.Conv2D(64, (3,3), activation='relu', padding='same')(inputs)
p1 = layers.MaxPooling2D((2,2))(c1)
# Decoder
u1 = layers.Conv2DTranspose(64, (3,3), strides=(2,2), padding='same')(p1)layers.Concatenate()([u1, c1])
outputs = layers.Conv2D(3, (1,1), activation='softmax')(u1)
model = models.Model(inputs=inputs, outputs=outputs)
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Không dùng skip connections → mất chi tiết cục bộ.
* Input không chuẩn hóa → gradient không ổn định.
* Upsampling quá nhiều → ảnh ra mờ, mất chi tiết.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* U-Net vs Encoder-Decoder bình thường:

  * U-Net: skip connections giữ thông tin cục bộ.
  * Encoder-Decoder bình thường: mất chi tiết cục bộ.
* U-Net vs Segmentation truyền thống:

  * Truyền thống: patch-based, chậm và mất thông tin.
  * U-Net: end-to-end, học toàn cục và cục bộ.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Medical imaging: MRI, CT scan segmentation.
* Satellite imagery: land cover mapping.
* Robotics: object segmentation for grasping.
* End-to-end training với small dataset nhờ data augmentation.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* U-Net khác encoder-decoder bình thường thế nào?
* Skip connections có tác dụng gì?
* Output của U-Net có dạng gì?
* Loss function thường dùng cho U-Net?

---

## 10. TL;DR (Short Summary)

* U-Net: encoder-decoder + skip connections cho segmentation.
* Giữ chi tiết cục bộ và học phụ thuộc toàn cục.
* Loss: cross-entropy hoặc dice loss.
* Dùng rộng rãi trong medical imaging, satellite, r
