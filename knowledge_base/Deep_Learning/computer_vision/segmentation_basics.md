---
title: Segmentation Basics
description: Ghi chú cơ bản về image segmentation trong computer vision, các loại segmentation, loss function, evaluation metrics và ứng dụng.
tags: [Segmentation, Computer Vision, Deep Learning, Semantic Segmentation, Instance Segmentation]
---

## 1. Tóm tắt khái niệm (Definition)

Image segmentation là bài toán phân loại từng pixel trong ảnh, chia ảnh thành các region hoặc đối tượng có ý nghĩa.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Medical imaging: phân đoạn mô bệnh.
* Autonomous driving: phát hiện làn đường, xe, người đi bộ.
* Satellite imagery: phân loại đất, nước, rừng.
* Robotics: nhận dạng vật thể cho grasping.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* **Semantic segmentation**: phân loại mỗi pixel thuộc class nào.
* **Instance segmentation**: phân đoạn từng đối tượng riêng biệt.
* **Model**: CNN encoder-decoder, U-Net, DeepLab.
* **Loss function**: cross-entropy hoặc dice loss.
  $$
  L_{dice} = 1 - \frac{2 \sum_i p_i g_i}{\sum_i p_i + \sum_i g_i}
  $$
* **Evaluation metrics**: IoU, pixel accuracy, mean IoU.
  $$
  IoU = \frac{|Prediction \cap GroundTruth|}{|Prediction \cup GroundTruth|}
  $$

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

* Input: image tensor $I \in \mathbb{R}^{H \times W \times C}$
* Encoder: CNN trích xuất feature maps.
* Decoder: upsampling, skip connections.
* Output: segmentation map $S \in \mathbb{R}^{H \times W \times Classes}$

---

## 5. Ví dụ code (Code Examples)

```python
import tensorflow as tf
from tensorflow.keras import layers, models

inputs = tf.keras.Input(shape=(128,128,3))
x = layers.Conv2D(64, (3,3), activation='relu', padding='same')(inputs)
x = layers.MaxPooling2D()(x)
# ... encoder layers
x = layers.Conv2DTranspose(64, (3,3), strides=2, activation='relu', padding='same')(x)
# ... decoder layers
outputs = layers.Conv2D(3, (1,1), activation='softmax')(x)  # 3 classes
model = models.Model(inputs=inputs, outputs=outputs)
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Class imbalance → bias về class phổ biến.
* Không normalize input → gradient không ổn định.
* Upsampling quá nhiều → mất chi tiết.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* Semantic vs Instance segmentation:

  * Semantic: phân loại pixel theo class.
  * Instance: phân loại pixel theo đối tượng riêng.
* Segmentation vs Detection:

  * Detection: bounding box + class.
  * Segmentation: pixel-level classification.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Medical imaging: tumor detection, organ segmentation.
* Autonomous driving: lane detection, object mask.
* Satellite images: land cover classification.
* Robotics: object grasping, manipulation.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Semantic segmentation khác instance segmentation thế nào?
* Dice loss tính ra sao?
* Khi nào dùng cross-entropy vs dice loss?
* Các kiến trúc phổ biến cho segmentation?

---

## 10. TL;DR (Short Summary)

* Segmentation: phân loại từng pixel trong ảnh.
* Loss: cross-entropy hoặc dice loss.
* Metrics: IoU, pixel accuracy, mean IoU.
* Dùng trong medical imaging, autonomous driving, satellite imagery, robotics.
