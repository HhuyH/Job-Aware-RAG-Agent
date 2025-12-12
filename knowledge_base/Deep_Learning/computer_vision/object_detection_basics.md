---
title: Object Detection Basics
description: Ghi chú cơ bản về object detection trong computer vision, các phương pháp, anchor boxes, IoU, loss functions và ứng dụng.
tags: [Object Detection, Computer Vision, Deep Learning, YOLO, Faster R-CNN]
---

## 1. Tóm tắt khái niệm (Definition)

Object detection là bài toán xác định vị trí (bounding box) và phân loại các đối tượng trong ảnh, kết hợp cả localization và classification.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Nhận dạng người, xe, vật thể trong video surveillance.
* Autonomous driving: phát hiện xe, người đi bộ, biển báo.
* Robotics: nhận dạng vật thể và tương tác.
* Khi cần mô hình xác định vị trí và loại đối tượng cùng lúc.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* **Anchor boxes / prior boxes**: dự đoán offset so với các box cố định.
* **IoU (Intersection over Union)**: đánh giá overlap giữa box dự đoán và ground truth.
  $$
  IoU = \frac{area(B_{pred} \cap B_{gt})}{area(B_{pred} \cup B_{gt})}
  $$
* **Loss function**: kết hợp localization loss và classification loss.
  $$
  L = L_{cls} + \lambda L_{loc}
  $$
* Mô hình CNN trích xuất feature maps, head network dự đoán box và class.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

* Input: image tensor $I \in \mathbb{R}^{H \times W \times 3}$
* Feature extraction: CNN → feature map $F$
* Prediction head: bounding box offsets $t_x, t_y, t_w, t_h$ và class probabilities $p_c$
  $$
  B_{pred} = (t_x, t_y, t_w, t_h), \quad p_c = \text{softmax}(F)
  $$

---

## 5. Ví dụ code (Code Examples)

```python
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models

base_model = MobileNetV2(input_shape=(224,224,3), include_top=False)
feature_map = base_model.output
x = layers.Conv2D(5*4, (1,1))(feature_map)  # 5 anchors, 4 coords each
class_pred = layers.Conv2D(5*80, (1,1))(feature_map)  # 5 anchors, 80 classes
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Anchor boxes không phù hợp với dataset → phát hiện kém.
* Không normalize bounding box → gradient không ổn định.
* Không balance class → bias về class phổ biến.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* Object detection vs Image classification:

  * Classification: chỉ dự đoán class của toàn ảnh.
  * Detection: dự đoán class và bounding box.
* Two-stage vs one-stage detectors:

  * Two-stage (Faster R-CNN): chính xác hơn, chậm hơn.
  * One-stage (YOLO, SSD): nhanh hơn, có thể ít chính xác hơn.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Surveillance: phát hiện người/xe trong video.
* Autonomous driving: nhận dạng đối tượng xung quanh.
* Retail: tracking sản phẩm, đếm khách.
* Robotics: grasping và interaction.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Anchor boxes là gì và tại sao dùng?
* IoU được tính như thế nào?
* Two-stage vs one-stage detector khác nhau ra sao?
* Loss function của object detection gồm những gì?

---

## 10. TL;DR (Short Summary)

* Object detection kết hợp localization và classification.
* Công thức quan trọng: IoU, loss = L_cls + lambda * L_loc.
* Anchor boxes giúp dự đoán vị trí tốt hơn.
* Dùng trong video surveillance, autonomous driving, robotics.
