---
title: Multilayer Perceptron (MLP)
description: Tài liệu ghi chú chi tiết về Multilayer Perceptron, bao gồm kiến thức cơ bản, forward/backward propagation, gradient, activation functions và áp dụng thực tế.
tags: [MLP, Neural Network, Deep Learning, Backpropagation]
---

# Multilayer Perceptron (MLP)

## 1. Tóm tắt khái niệm (Definition)

Multilayer Perceptron (MLP) là một loại neural network cơ bản gồm nhiều lớp fully connected, dùng cho dự đoán, phân loại và regression.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Dự đoán dữ liệu có dạng vector.
* Phân loại hình ảnh, văn bản, dữ liệu tabular.
* Là nền tảng để hiểu các kiến trúc deep learning phức tạp hơn.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* Forward propagation: tính toán output của từng lớp qua hàm kích hoạt.
* Backward propagation: dùng chain rule để tính gradient và cập nhật trọng số.
* Fully connected: mỗi neuron kết nối với tất cả neuron lớp tiếp theo.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

```latex
$$
z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]}
$$

$$
a^{[l]} = f(z^{[l]})
$$
```

---

## 5. Ví dụ code (Code Examples)

```python
# Forward propagation example
import numpy as np

def relu(z):
    return np.maximum(0, z)

W = np.random.randn(3, 2)
b = np.random.randn(3, 1)
a_prev = np.random.randn(2, 1)

z = np.dot(W, a_prev) + b
a = relu(z)
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Vanishing gradient: khi ||W|| < 1 và f'(z) < 1.
* Exploding gradient: khi ||W|| > 1 hoặc f'(z) > 1.
* Sử dụng hàm sigmoid cho mạng sâu dễ gặp vanishing gradient.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* Điểm giống: MLP vs Perceptron đều là neural network.
* Điểm khác: MLP có hidden layer, Perceptron chỉ có input-output.
* Khi nào dùng: Dùng MLP khi dữ liệu phức tạp, cần ẩn lớp xử lý.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Phân loại ảnh, nhận diện chữ số (MNIST).
* Dự đoán dữ liệu tabular.
* Nền tảng để xây dựng các mạng CNN, RNN phức tạp hơn.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* MLP khác gì với Perceptron?
* Chain rule hoạt động thế nào trong backpropagation?
* Khi nào xảy ra vanishing/exploding gradient và cách khắc phục?

---

## 10. TL;DR (Short Summary)

* MLP là mạng neural network nhiều lớp fully connected.
* Forward: z = W a + b, a = f(z).
* Backward: dùng chain rule tính gradient.
* Gradient quá nhỏ → vanishing, quá lớn → exploding.
* Activation functions: ReLU, Sigmoid, Tanh.
