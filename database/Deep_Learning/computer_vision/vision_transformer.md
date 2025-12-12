---
title: Vision Transformer Basics
description: Ghi chú về kiến trúc Vision Transformer (ViT) cho image classification, cơ chế self-attention áp dụng trên patch, positional embedding và ứng dụng.
tags: [Vision Transformer, ViT, Computer Vision, Deep Learning, Transformer]
---

## 1. Tóm tắt khái niệm (Definition)

Vision Transformer (ViT) áp dụng kiến trúc Transformer vào hình ảnh bằng cách chia ảnh thành các patch, flatten và embed chúng, sau đó sử dụng self-attention để học mối quan hệ giữa các patch.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Image classification.
* Object detection kết hợp ViT backbone.
* Khi muốn tận dụng khả năng học phụ thuộc dài hạn của Transformer trên hình ảnh.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* Chia ảnh $I \in \mathbb{R}^{H \times W \times C}$ thành $N$ patch có kích thước $(P,P)$.
* Flatten patch và ánh xạ thành embedding:
  $$
  x_p = E \cdot flatten(patch) + E_{pos}
  $$
* Thêm token [CLS] để dự đoán class.
* Pass qua L layer Transformer encoder (multi-head self-attention + feed-forward).
* Output token [CLS] dùng cho classification.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

* Patch embedding:
  $$
  x_p = W_e \cdot patch_i + b_e
  $$
* Multi-head self-attention:
  $$
  Attention(Q,K,V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V
  $$
* Feed-forward layer:
  $$
  FFN(x) = max(0, x W_1 + b_1) W_2 + b_2
  $$
* Classification:
  $$
  y = \text{softmax}(CLS_{output} \cdot W_{class})
  $$

---

## 5. Ví dụ code (Code Examples)

```python
import tensorflow as tf
from tensorflow.keras import layers, models

# Patch embedding
patch_size = 16
num_patches = (224 // patch_size) ** 2
input_layer = tf.keras.Input(shape=(224,224,3))
patches = tf.image.extract_patches(
    images=input_layer,
    sizes=[1, patch_size, patch_size, 1],
    strides=[1, patch_size, patch_size, 1],
    rates=[1,1,1,1],
    padding='VALID'
)
patches = layers.Reshape((num_patches, patch_size*patch_size*3))(patches)

# Add [CLS] token and positional embedding, then Transformer layers ...
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Patch size quá lớn → mất chi tiết.
* Không normalize input → gradient không ổn định.
* Quên positional embedding → mất thông tin vị trí.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* ViT vs CNN:

  * ViT: self-attention, học phụ thuộc dài hạn, parallelizable.
  * CNN: convolutional, học local patterns, inductive bias cao.
* ViT vs Transformer truyền thống:

  * Input là image patches thay vì token text.
  * Patch embedding thay cho token embedding.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Image classification datasets: ImageNet.
* Backbone cho object detection, segmentation.
* Pre-trained ViT kết hợp fine-tuning cho downstream tasks.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* ViT khác CNN thế nào?
* Patch embedding và positional embedding có tác dụng gì?
* Multi-head self-attention trong ViT hoạt động ra sao?
* Khi nào nên dùng ViT thay cho CNN?

---

## 10. TL;DR (Short Summary)

* Vision Transformer chia ảnh thành patch, dùng self-attention.
* Patch embedding + positional embedding + Transformer encoder.
* Output token [CLS] dùng cho classification.
* Dùng trong image classification, object detectio
