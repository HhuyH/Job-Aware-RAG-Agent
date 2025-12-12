---
title: YOLO Architecture Basics
description: Ghi chú về kiến trúc YOLO (You Only Look Once) trong object detection, cơ chế one-stage detection, bounding box prediction và loss function.
tags: [YOLO, Object Detection, Computer Vision, Deep Learning, CNN]
---

## 1. Tóm tắt khái niệm (Definition)

YOLO là kiến trúc one-stage object detector, dự đoán bounding box và class trực tiếp từ toàn bộ ảnh mà không cần region proposal, giúp tăng tốc độ inference.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Real-time object detection.
* Autonomous driving, video surveillance.
* Khi cần mô hình nhanh, có thể deploy trên thiết bị với tốc độ cao.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* Chia ảnh thành S x S lưới.
* Mỗi cell dự đoán B bounding boxes với confidence và class probabilities.
* Bounding box prediction:
  $$
  B = (x, y, w, h, confidence)
  $$
* Class probability:
  $$
  P(Class_i | Object) = \text{softmax}(F)
  $$
* Loss function kết hợp localization, confidence, và classification.
  $$
  L = \lambda_{coord} \sum_{i=0}^{S^2} \sum_{j=0}^{B} 1_{obj}^{ij}[(x_i - \hat{x}_i)^2 + (y_i - \hat{y}_i)^2] + ...
  $$

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

* Backbone CNN trích xuất feature maps.
* Detection head dự đoán bounding box và class.
* Output tensor shape: $(S, S, B*5 + C)$, với C là số class.

---

## 5. Ví dụ code (Code Examples)

```python
import tensorflow as tf
from tensorflow.keras import layers, models

inputs = tf.keras.Input(shape=(416,416,3))
x = layers.Conv2D(32, (3,3), activation='relu', padding='same')(inputs)
x = layers.Conv2D(64, (3,3), activation='relu', padding='same')(x)
# ... add more conv layers for backbone
output = layers.Conv2D(3*(5+80), (1,1), activation='linear')(x)  # 3 anchors, 80 classes
model = models.Model(inputs=inputs, outputs=output)
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Không chuẩn hóa input ảnh → gradient không ổn định.
* Anchor boxes không phù hợp với dataset.
* Không cân bằng các class → bias về class phổ biến.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* YOLO vs SSD vs Faster R-CNN:

  * YOLO: nhanh, one-stage, inference real-time.
  * SSD: one-stage, nhiều feature map, trade-off speed/accuracy.
  * Faster R-CNN: two-stage, chính xác hơn, chậm hơn.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Real-time detection: CCTV, drone footage.
* Autonomous vehicles: detect pedestrians, cars, traffic signs.
* Robotics: real-time object detection for manipulation.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* YOLO hoạt động khác SSD và Faster R-CNN thế nào?
* Output tensor của YOLO có dạng gì?
* Loss function của YOLO gồm những thành phần nào?
* Tại sao YOLO phù hợp với real-time detection?

---

## 10. TL;DR (Short Summary)

* YOLO: one-stage, real-time object detection.
* Dự đoán bounding box và class trực tiếp từ toàn ảnh.
* Output shape: (S, S, B*5 + C).
* Dùng rộng rãi trong autonomous driving, surveillance, robotics.
