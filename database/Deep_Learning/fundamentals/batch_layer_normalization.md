---
title: Batch Normalization & Layer Normalization
description: Giải thích hai kỹ thuật chuẩn hóa phổ biến trong Deep Learning, cơ chế hoạt động, công thức, ứng dụng, lỗi thường gặp và so sánh.
tags: [deep-learning, normalization, training-techniques, fundamentals]
---

## Mô tả cách mình đang xây dựng hệ thống file `.md`
(Để trống hoặc giữ nguyên trong repo — phần này bạn đã chuẩn hóa rồi)

---

# Batch Normalization & Layer Normalization

## 1. Tóm tắt khái niệm (Definition)

**Batch Normalization (BN):** Chuẩn hóa giá trị kích hoạt theo từng batch trong quá trình training, giúp mô hình hội tụ nhanh hơn và ổn định hơn.  
**Layer Normalization (LN):** Chuẩn hóa theo từng sample trên toàn bộ chiều feature, không phụ thuộc batch size.

---

## 2. Mục đích & khi nào dùng (Use Cases)

- Giảm hiện tượng internal covariate shift.  
- Tăng tốc độ hội tụ khi training deep networks.  
- Giúp gradient ổn định hơn.  
- Với mô hình có batch nhỏ (transformer, RNN): ưu tiên **LayerNorm**.  
- Với CNN, batch lớn: ưu tiên **BatchNorm**.

---

## 3. Cách hoạt động bên trong (Internal Logic)

### Batch Normalization  
Chuẩn hóa từng feature dựa trên thống kê của *cả batch*.

Công thức chuẩn hóa:

$$
\mu_B = \frac{1}{m} \sum_{i=1}^{m} x_i
$$

$$
\sigma_B^2 = \frac{1}{m} \sum_{i=1}^{m} (x_i - \mu_B)^2
$$

$$
\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}
$$

Thêm scale & shift học được:

$$
y_i = \gamma \hat{x}_i + \beta
$$

---

### Layer Normalization  
Chuẩn hóa theo vector feature của từng sample:

$$
\mu = \frac{1}{H} \sum_{j=1}^{H} x_j
$$

$$
\sigma^2 = \frac{1}{H} \sum_{j=1}^{H} (x_j - \mu)^2
$$

$$
\hat{x}_j = \frac{x_j - \mu}{\sqrt{\sigma^2 + \epsilon}}
$$

$$
y_j = \gamma \hat{x}_j + \beta
$$

LN luôn nhất quán vì không phụ thuộc batch size.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

### PyTorch – BatchNorm
```python
torch.nn.BatchNorm1d(num_features)
torch.nn.BatchNorm2d(num_features)
torch.nn.BatchNorm3d(num_features)
````

### PyTorch – LayerNorm

```python
torch.nn.LayerNorm(normalized_shape)
```

---

## 5. Ví dụ code (Code Examples)

### BatchNorm trong CNN

```python
import torch.nn as nn

model = nn.Sequential(
    nn.Conv2d(32, 64, kernel_size=3, padding=1),
    nn.BatchNorm2d(64),
    nn.ReLU()
)
```

### LayerNorm trong Transformer

```python
import torch.nn as nn

model = nn.TransformerEncoderLayer(
    d_model=512,
    nhead=8,
    norm_first=True,  # sử dụng LayerNorm trước attention
)
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Batch size quá nhỏ → BatchNorm hoạt động kém ổn định.
* Quên chuyển model sang `eval()` khi inference → BN dùng sai running mean/var.
* Dùng BN cho dữ liệu tuần tự (RNN) → không phù hợp.
* LayerNorm chậm hơn BN trên CNN vì tính toán theo từng sample.

---

## 7. So sánh với khái niệm liên quan (Comparison)

### BatchNorm vs LayerNorm

| Tiêu chí              | BatchNorm          | LayerNorm               |
| --------------------- | ------------------ | ----------------------- |
| Dựa vào batch         | Có                 | Không                   |
| Phổ biến trong        | CNN                | Transformer, RNN        |
| Phụ thuộc batch size  | Có                 | Không                   |
| Ổn định khi batch nhỏ | Kém                | Tốt                     |
| Inference             | Dùng running stats | Không cần running stats |

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* BN phù hợp với training **CNN trên GPU** với batch lớn.
* LN là tiêu chuẩn trong **Transformer**, **LLM**, **GPT**, **BERT**.
* LN giúp mô hình ổn định khi batch size nhỏ hoặc biến động.
* Kết hợp normalization đúng cách → giảm nhu cầu learning rate nhỏ.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Vì sao batch size nhỏ làm BatchNorm kém hiệu quả?
* Giải thích sự khác nhau trong cách tính mean/variance giữa BN và LN?
* Tại sao Transformer không dùng BatchNorm?
* BN có hoạt động khác nhau giữa training và inference như thế nào?
* Vì sao LayerNorm không cần running mean/var?

---

## 10. TL;DR (Short Summary)

* BN chuẩn hóa theo batch; LN chuẩn hóa theo features của từng sample.
* BN nhanh và hiệu quả cho CNN; LN ổn định và phù hợp cho Transformer.
* LN không phụ thuộc batch size — quan trọng với mô hình tuần tự.
* Cả BN và LN đều có tham số học được: γ và β.

