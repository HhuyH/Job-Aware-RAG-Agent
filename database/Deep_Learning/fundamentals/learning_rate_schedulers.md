---
title: Learning Rate Schedulers
description: Giải thích các kỹ thuật điều chỉnh learning rate trong Deep Learning, công thức, cơ chế hoạt động và ứng dụng thực tế.
tags: [deep-learning, optimization, fundamentals, learning-rate, scheduler]
---

# Learning Rate Schedulers

## 1. Khái niệm
Learning rate scheduler là cơ chế điều chỉnh learning rate theo thời gian huấn luyện để:
- Tránh overshoot.
- Giảm dao động gần optimum.
- Tăng tốc độ hội tụ.

---

## 2. Vì sao cần scheduler?
Learning rate cố định thường không phù hợp cho toàn bộ quá trình huấn luyện.  
Scheduler giúp **tăng–giảm LR có chủ đích** tùy từng giai đoạn.

---

## 3. Các loại Learning Rate Schedulers

---

### 3.1 Step Decay

$$
\text{lr}(t) = \text{lr}_0 \cdot \gamma^{\left\lfloor \frac{t}{s} \right\rfloor}
$$

- \( s \): số epoch mỗi lần giảm  
- \( \gamma \): hệ số decay

---

### 3.2 Exponential Decay

$$
\text{lr}(t) = \text{lr}_0 \cdot e^{-k t}
$$

- \( k \): tốc độ decay

---

### 3.3 Polynomial Decay

$$
\text{lr}(t) = \text{lr}_0 \left( 1 - \frac{t}{T} \right)^p
$$

- \( T \): tổng số bước  
- \( p \): bậc decay

---

### 3.4 Cosine Annealing

$$
\text{lr}(t) = 
\frac{1}{2}\,\text{lr}_0\left(1 + \cos\left(\frac{\pi t}{T}\right)\right)
$$

- LR giảm theo dạng cos, thường cho hội tụ mượt.

---

### 3.5 Cyclical Learning Rate (CLR)

$$
\text{lr}(t) = 
\text{lr}_{\min} + 
\left(\text{lr}_{\max} - \text{lr}_{\min}\right)
\cdot \max\left(0, 1 - |2x - 1|\right)
$$

với:

$$
x = \frac{t \bmod c}{c}
$$

- \( c \): độ dài một chu kỳ

---

### 3.6 One Cycle Policy
Gồm 3 pha:
1. LR tăng → đạt cực đại  
2. LR giảm mạnh về ~0  
3. Momentum thay đổi ngược chiều LR

Kết hợp CLR + cosine decay.

---

### 3.7 ReduceLROnPlateau
Giảm LR khi **metric không cải thiện** trong một số epoch.

---

## 4. Cách chọn scheduler

| Tình huống | Gợi ý |
|-----------|-------|
| Loss dao động mạnh | Step / Cosine |
| Training dài | Exponential / Polynomial |
| Tìm LR tối ưu | CLR / One Cycle |
| Val loss đứng im | ReduceLROnPlateau |

---

## 5. Kết luận
Scheduler quyết định mức độ ổn định và tốc độ hội tụ của quá trình huấn luyện.  
Chọn đúng scheduler giúp mô hình **hội tụ nhanh hơn, tổng quát tốt hơn**.
