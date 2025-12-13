---
title: Deep Learning là gì?
description: Ghi chú tổng quan về Deep Learning, khái niệm cốt lõi, cách hoạt động, cấu trúc mô hình, ví dụ code, lỗi thường gặp và ứng dụng thực tế.
tags: [Deep Learning, Neural Networks, Machine Learning, AI]
---

## 1. Khái niệm

**Deep Learning (DL)** là một nhánh của **Machine Learning**, tập trung vào việc học **biểu diễn dữ liệu theo nhiều mức trừu tượng** thông qua **mạng nơ-ron nhân tạo nhiều tầng (deep neural networks)**.

Mỗi tầng trong mạng học một dạng biểu diễn:

* Tầng thấp: học **đặc trưng đơn giản** (ví dụ: cạnh trong ảnh, n-gram trong văn bản)
* Tầng cao: học **khái niệm trừu tượng hơn** (vật thể, ngữ nghĩa, ngữ cảnh)

### Điểm khác biệt cốt lõi so với Machine Learning truyền thống

* **Machine Learning truyền thống**:

  * Phụ thuộc mạnh vào **feature engineering thủ công**
  * Hiệu quả bị giới hạn bởi chất lượng feature do con người thiết kế
* **Deep Learning**:

  * Thực hiện **representation learning end-to-end**
  * Tự động trích xuất feature trực tiếp từ **dữ liệu thô** (raw data)
  * Giảm phụ thuộc vào tri thức miền (domain knowledge) ở bước tiền xử lý

### Vì sao “deep” lại quan trọng?

* Nhiều tầng cho phép mô hình:

  * Biểu diễn các **hàm phi tuyến rất phức tạp**
  * Mô hình hóa **quan hệ phân cấp (hierarchical structure)** trong dữ liệu
* Một mạng nông khó biểu diễn hiệu quả những cấu trúc này dù có nhiều neuron

### Khi nào Deep Learning đặc biệt hiệu quả?

Deep Learning phát huy sức mạnh khi:

* Có **dữ liệu lớn** (large-scale datasets)
* Dữ liệu **phi cấu trúc**, khó mô tả bằng feature thủ công:

  * Ảnh
  * Âm thanh
  * Văn bản
  * Video

Ngược lại, với dữ liệu nhỏ hoặc có cấu trúc rõ ràng, DL **không phải lúc nào cũng là lựa chọn tối ưu**.

---

## 2. Mục đích & Khi nào dùng (Use Cases)

### Mục đích
- Mô hình hóa các quan hệ **phi tuyến phức tạp**
- Trích xuất đặc trưng ở nhiều mức trừu tượng

### Khi nên dùng Deep Learning
- Dataset đủ lớn (hàng chục nghìn mẫu trở lên)
- Bài toán có cấu trúc phức tạp:
  - Image / Speech / NLP
- Feature khó thiết kế bằng tay

### Khi KHÔNG nên dùng
- Dataset nhỏ
- Bài toán tuyến tính, đơn giản
- Yêu cầu giải thích mô hình cao (interpretability)

---

## 3. Cách hoạt động bên trong (Internal Logic)

Một mô hình Deep Learning gồm nhiều tầng:

- **Input layer**
- **Hidden layers**
- **Output layer**

Mỗi neuron thực hiện:

$$
z = w^T x + b
$$

$$
a = f(z)
$$

Trong đó:
- \( w \): trọng số
- \( b \): bias
- \( f \): hàm kích hoạt (ReLU, Sigmoid, Softmax...)

### Quá trình huấn luyện
1. Forward propagation
2. Tính loss
3. Backpropagation
4. Cập nhật trọng số (Gradient Descent)

---

## 4. Cấu trúc / Cú pháp (Structure)

Một pipeline Deep Learning tiêu chuẩn:

1. Chuẩn bị dữ liệu
2. Định nghĩa model
3. Chọn loss function
4. Chọn optimizer
5. Training
6. Evaluation
7. Inference

---

## 5. Ví dụ code (Code Examples)

### Ví dụ đơn giản với PyTorch

```python
import torch
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64, 1)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        return self.fc2(x)

model = SimpleNN()
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
````

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Dataset quá nhỏ → overfitting
* Không chuẩn hóa dữ liệu
* Chọn learning rate không phù hợp
* Mạng quá sâu nhưng không regularization
* Nhầm lẫn giữa:

  * training loss thấp
  * generalization tốt

---

## 7. So sánh với khái niệm liên quan (Comparison)

| Tiêu chí            | Machine Learning | Deep Learning |
| ------------------- | ---------------- | ------------- |
| Feature engineering | Thủ công         | Tự động       |
| Dữ liệu             | Nhỏ–vừa          | Lớn           |
| Độ phức tạp         | Thấp–trung bình  | Cao           |
| Tài nguyên          | Ít               | GPU / TPU     |

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Computer Vision: CNN
* NLP: RNN, LSTM, Transformer
* Speech Recognition
* Recommendation Systems
* Autonomous Driving
* AI Agent / RAG (embedding, encoder models)

Trong thực tế, **DL hiếm khi đứng một mình**, mà là một phần của hệ thống lớn hơn.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

1. Deep Learning khác gì Machine Learning?
2. Tại sao cần hàm activation?
3. Vai trò của backpropagation?
4. Khi nào nên dùng DL thay vì ML truyền thống?
5. Vì sao DL cần nhiều dữ liệu?
6. Overfitting trong DL xảy ra khi nào?

---

## 10. TL;DR

* Deep Learning = Neural Network nhiều tầng
* Tự học feature, xử lý tốt dữ liệu phức tạp
* Mạnh nhưng tốn tài nguyên
* Không phải bài toán nào cũng cần DL
* Hiểu bản chất > chạy model
