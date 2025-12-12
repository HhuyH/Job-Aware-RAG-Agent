---
title: RNN & LSTM in NLP
description: Ghi chú về RNN và LSTM trong NLP, bao gồm khái niệm, cơ chế hoạt động, công thức, ví dụ code, ưu nhược điểm, và ứng dụng thực tế.
tags: [Deep Learning, NLP, RNN, LSTM, Sequence Modeling, Text Processing]
---

## 1. Khái niệm

- **RNN (Recurrent Neural Network):** mạng neural xử lý dữ liệu tuần tự, giữ thông tin qua các bước thời gian bằng **hidden state**.
- **LSTM (Long Short-Term Memory):** biến thể RNN giúp giải quyết vấn đề **vanishing/exploding gradient**, giữ thông tin dài hạn bằng **cell state** và các cổng điều khiển (input, forget, output).

RNN thích hợp cho:
- Dịch máy, sinh văn bản, dự đoán chuỗi thời gian

## 2. Mục đích & khi nào dùng (Use Cases)

- Sequence Modeling: dự đoán từ tiếp theo, POS tagging, NER
- Machine Translation (kết hợp Seq2Seq)
- Text Generation, Chatbot
- Sentiment Analysis (trích xuất thông tin từ chuỗi)
- Speech-to-Text / Audio Modeling

## 3. Cách hoạt động bên trong (Internal Logic)

### 3.1 RNN
Hidden state cập nhật theo:

$$
h_t = \tanh(W_h h_{t-1} + W_x x_t + b)
$$

Output:

$$
y_t = \text{softmax}(W_y h_t + c)
$$

Vấn đề: **vanishing/exploding gradient** khi chuỗi dài.

### 3.2 LSTM
Các cổng chính:

1. **Forget gate:** quyết định giữ lại thông tin cũ
$$
f_t = \sigma(W_f [h_{t-1}, x_t] + b_f)
$$

2. **Input gate:** quyết định cập nhật thông tin mới
$$
i_t = \sigma(W_i [h_{t-1}, x_t] + b_i)
$$
$$
\tilde{C}_t = \tanh(W_C [h_{t-1}, x_t] + b_C)
$$

3. **Cell state cập nhật**
$$
C_t = f_t * C_{t-1} + i_t * \tilde{C}_t
$$

4. **Output gate:** tạo hidden state mới
$$
o_t = \sigma(W_o [h_{t-1}, x_t] + b_o)
$$
$$
h_t = o_t * \tanh(C_t)
$$

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

Python example với `PyTorch`:

```python
import torch
import torch.nn as nn

class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers=1):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, (h_n, c_n) = self.lstm(x)
        out = self.fc(out[:, -1, :])  # dùng hidden cuối cùng
        return out
```

## 5. Ví dụ code (Code Examples)

* Training RNN/LSTM cho text classification:

```python
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for epoch in range(epochs):
    for x_batch, y_batch in dataloader:
        optimizer.zero_grad()
        outputs = model(x_batch)
        loss = criterion(outputs, y_batch)
        loss.backward()
        optimizer.step()
```

## 6. Lỗi thường gặp (Common Pitfalls)

* Gradient vanishing/exploding trong RNN
* Sequence dài → mất thông tin đầu
* Batch chưa padding đúng → lỗi training
* Overfitting với dữ liệu nhỏ
* Không normalize input → khó converge

## 7. So sánh với khái niệm liên quan (Comparison)

| Kiến trúc | Điểm mạnh                             | Điểm yếu                                            |
| --------- | ------------------------------------- | --------------------------------------------------- |
| RNN       | Đơn giản, xử lý tuần tự               | Vanishing/exploding gradient, khó capture long-term |
| LSTM      | Giữ thông tin dài hạn tốt             | Nặng, training chậm                                 |
| GRU       | Nhẹ hơn LSTM, performance tương đương | Ít linh hoạt hơn LSTM                               |

## 8. Ứng dụng trong thực tế (Practical Insights)

* Seq2Seq: LSTM encoder-decoder cho dịch máy
* Text Generation: sinh văn bản, chatbot
* Speech recognition: model chuỗi âm thanh
* Sentiment Analysis: dự đoán cảm xúc từ review
* Time Series Prediction: dự đoán stock, weather

## 9. Câu hỏi phỏng vấn (Interview Questions)

1. Giải thích cơ chế RNN và vấn đề vanishing gradient.
2. LSTM giải quyết vấn đề RNN như thế nào?
3. Các cổng trong LSTM có vai trò gì?
4. Khi nào dùng GRU thay vì LSTM?
5. Làm thế nào để xử lý sequence dài trong RNN/LSTM?

## 10. TL;DR (Short Summary)

RNN xử lý dữ liệu tuần tự nhưng gặp vanishing gradient với chuỗi dài. LSTM giải quyết bằng cell state và cổng điều khiển (input, forget, output). Ứng dụng trong NLP: Seq2Seq, text generation, sentiment analysis, machine translation.
