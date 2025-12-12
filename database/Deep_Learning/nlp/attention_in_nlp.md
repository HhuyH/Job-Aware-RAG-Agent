---
title: Attention Mechanism in NLP
description: Ghi chú về cơ chế Attention trong NLP, bao gồm khái niệm, cơ chế hoạt động, các loại attention phổ biến, ví dụ code, và ứng dụng trong các mô hình Seq2Seq và Transformer.
tags: [Deep Learning, NLP, Attention, Seq2Seq, Transformer]
---

## 1. Khái niệm

Attention là cơ chế cho phép mô hình **tập trung vào những phần quan trọng** của chuỗi đầu vào khi sinh ra chuỗi đầu ra. Nó giải quyết hạn chế của Seq2Seq truyền thống, nơi toàn bộ thông tin đầu vào được cô đặc vào một vector cố định.

Ví dụ: dịch câu dài, mô hình cần tập trung vào các từ quan trọng ở mỗi bước decode.

## 2. Mục đích & khi nào dùng (Use Cases)

- Giải quyết vấn đề phụ thuộc dài trong Seq2Seq.
- Cải thiện chất lượng dịch máy, tóm tắt, sinh câu trả lời.
- Sử dụng trong: 
  - Machine Translation
  - Text Summarization
  - Question Answering
  - Transformer-based models (BERT, GPT)

## 3. Cách hoạt động bên trong (Internal Logic)

### 3.1 Attention Score
Tính trọng số \( \alpha_{t,i} \) dựa trên mối quan hệ giữa decoder state \(s_{t-1}\) và encoder output \(h_i\):

$$
\alpha_{t,i} = \frac{\exp(score(s_{t-1}, h_i))}{\sum_{j} \exp(score(s_{t-1}, h_j))}
$$

Các hàm score phổ biến:

- **Dot-product:**  
$$
score(s, h) = s^T h
$$

- **General:**  
$$
score(s, h) = s^T W_a h
$$

- **Concat:**  
$$
score(s, h) = v_a^T \tanh(W_a [s; h])
$$

### 3.2 Context Vector
Tổng có trọng số các trạng thái encoder:

$$
c_t = \sum_i \alpha_{t,i} h_i
$$

Decoder sử dụng \(c_t\) để sinh token tiếp theo:

$$
s_t = \text{DecoderRNN}(y_{t-1}, s_{t-1}, c_t)
$$

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

Python example với PyTorch:

```python
import torch
import torch.nn as nn

class Attention(nn.Module):
    def __init__(self, hidden_size):
        super(Attention, self).__init__()
        self.attn = nn.Linear(hidden_size*2, hidden_size)
        self.v = nn.Parameter(torch.rand(hidden_size))

    def forward(self, hidden, encoder_outputs):
        timestep = encoder_outputs.size(0)
        h = hidden.repeat(timestep, 1, 1).transpose(0,1)
        energy = torch.tanh(self.attn(torch.cat((h, encoder_outputs), 2)))
        energy = energy.transpose(1,2)
        v = self.v.repeat(encoder_outputs.size(1),1).unsqueeze(1)
        attention_weights = torch.bmm(v, energy)
        return torch.softmax(attention_weights.squeeze(1), dim=1)
````

## 5. Ví dụ code (Code Examples)

* Tính context vector:

```python
attn_weights = attention(decoder_hidden, encoder_outputs)
context = torch.bmm(attn_weights.unsqueeze(1), encoder_outputs.transpose(0,1))
```

* Sử dụng context trong decoder:

```python
decoder_input = torch.cat((context, decoder_input), dim=2)
output, decoder_hidden = decoder_lstm(decoder_input, decoder_hidden)
```

## 6. Lỗi thường gặp (Common Pitfalls)

* Không chuẩn hóa attention → gradient exploding hoặc vanishing.
* Bỏ qua padding → attention nhầm vào các vị trí padding.
* Sử dụng attention trên dữ liệu quá dài mà không có cơ chế masking → mô hình học sai.

## 7. So sánh với khái niệm liên quan (Comparison)

| Kiến trúc           | Điểm mạnh                                         | Điểm yếu                |
| ------------------- | ------------------------------------------------- | ----------------------- |
| Seq2Seq cơ bản      | Đơn giản                                          | Khó học phụ thuộc dài   |
| Seq2Seq + Attention | Giải quyết phụ thuộc dài, tập trung từ quan trọng | Tăng chi phí tính toán  |
| Transformer         | Attention toàn phần, parallelizable               | Cần nhiều dữ liệu & GPU |

## 8. Ứng dụng trong thực tế (Practical Insights)

* Google Translate & các mô hình dịch máy hiện đại dùng attention.
* Text summarization: tập trung vào các phần quan trọng của văn bản dài.
* Transformers (BERT, GPT): attention là cơ chế trung tâm, cho phép capture mối quan hệ từ xa giữa các token.
* Question Answering: xác định phần context liên quan đến câu hỏi.

## 9. Câu hỏi phỏng vấn (Interview Questions)

1. Attention là gì? Tại sao cần attention trong Seq2Seq?
2. Phân biệt dot-product, general, concat attention.
3. Context vector được tính như thế nào?
4. Masking trong attention có vai trò gì?
5. Tại sao Transformer lại dùng attention toàn phần thay vì RNN?

## 10. TL;DR (Short Summary)

Attention cho phép mô hình tập trung vào các phần quan trọng của chuỗi đầu vào tại mỗi bước decode. Nó giải quyết hạn chế của Seq2Seq truyền thống, là nền tảng cho các mô hình Transformer và ứng dụng rộng rãi trong dịch máy, tóm tắt, QA, và chatbot.
