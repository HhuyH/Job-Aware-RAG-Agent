---

title: CNN Convolution Basics
description: Tài liệu ghi chú cơ bản về Convolutional Neural Networks, các layer, convolution, pooling, activation và ứng dụng thực tế.
tags: [CNN, Convolution, Deep Learning, Neural Network]
-------------------------------------------------------

## 1. Tóm tắt khái niệm (Definition)

CNN là loại mạng neural network đặc biệt hiệu quả trong xử lý dữ liệu có cấu trúc dạng lưới, ví dụ như hình ảnh. CNN sử dụng **convolutional layers** để tự động học đặc trưng không gian từ dữ liệu.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Phân loại ảnh và video.
* Nhận diện đối tượng và detection.
* Phân tích chuỗi dữ liệu có tính không gian (time-series, sensor).
* Khi cần giảm số lượng tham số so với MLP với cùng dữ liệu ảnh.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* **Convolutional layer**: nhân kernel/filter với input để phát hiện đặc trưng.
* **Activation function**: ReLU hoặc các hàm phi tuyến khác.
* **Pooling layer**: giảm chiều dữ liệu, giữ thông tin quan trọng.
* **Fully connected layer**: dùng để tổng hợp đặc trưng và dự đoán output.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

$$
Z^{[l]} = X * W^{[l]} + b^{[l]}
A^{[l]} = f(Z^{[l]})
$$
Trong đó:

* `*` là phép convolution.
* `W^{[l]}` là filter/kernel.
* `b^{[l]}` là bias.
* `f` là hàm kích hoạt (ReLU, Sigmoid, Tanh).

---

## 5. Ví dụ code (Code Examples)

```python
import tensorflow as tf
from tensorflow.keras import layers, models

model = models.Sequential()
model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Kernel/filter quá lớn → mất thông tin chi tiết.
* Quá nhiều pooling layers → giảm quá mức resolution.
* Không chuẩn hóa input → learning chậm hoặc gradient biến đổi bất thường.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* CNN vs MLP:

  * Giống: đều là neural network.
  * Khác: CNN dùng convolution, parameter sharing, giảm số lượng tham số.
* Khi nào dùng CNN: dữ liệu có tính chất không gian, ví dụ hình ảnh hoặc tín hiệu.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Nhận diện chữ số (MNIST), nhận diện khuôn mặt.
* Phân loại hình ảnh trong y tế (MRI, X-ray).
* Object detection trong video và xe tự lái.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* CNN khác gì với MLP?
* Convolution operation hoạt động thế nào?
* Lý do dùng pooling layer?
* Parameter sharing có tác dụng gì?

---

## 10. TL;DR (Short Summary)

* CNN hiệu quả cho dữ liệu dạng lưới, nhất là hình ảnh.
* Convolutional layer học đặc trưng không gian.
* Pooling giảm chiều dữ liệu, giữ thông tin quan trọng.
* Fully connected layer tổng hợp đặc trưng để dự đoán.
* Parameter sharing giúp giảm số lượng trọng số và tránh overfitting.
