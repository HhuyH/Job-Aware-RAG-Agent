---
title: Sequence-to-Sequence (Seq2Seq) in NLP
description: Ghi chú về mô hình Sequence-to-Sequence trong NLP, cơ chế hoạt động, các biến thể, ví dụ code, và ứng dụng thực tế như dịch máy, tóm tắt văn bản, chatbot.
tags: [Deep Learning, NLP, Seq2Seq, Encoder-Decoder, Machine Translation]
---

## 1. Khái niệm

Sequence-to-Sequence (Seq2Seq) là kiến trúc mạng neural được dùng để biến đổi một chuỗi đầu vào thành một chuỗi đầu ra. Mỗi chuỗi có thể có độ dài khác nhau. Seq2Seq thường sử dụng **một encoder** để mã hóa chuỗi đầu vào thành vector ngữ nghĩa và **một decoder** để sinh chuỗi đầu ra.

Ví dụ:

$$
\text{Input sequence: } X = (x_1, x_2, ..., x_T)
$$
$$
\text{Output sequence: } Y = (y_1, y_2, ..., y_{T'})
$$

## 2. Mục đích & khi nào dùng (Use Cases)

- Machine Translation (dịch ngôn ngữ)
- Text Summarization (tóm tắt văn bản)
- Question Answering (trả lời câu hỏi)
- Chatbots
- Speech-to-Text hoặc Text-to-Speech

## 3. Cách hoạt động bên trong (Internal Logic)

### 3.1 Encoder
- Nhận chuỗi đầu vào \(X\)
- Biến đổi thành **context vector** \(c\) (vector ngữ nghĩa tóm tắt thông tin)
- Thường dùng RNN, LSTM, GRU, hoặc Transformer

$$
h_t = \text{EncoderRNN}(x_t, h_{t-1})
$$
$$
c = h_T
$$

### 3.2 Decoder
- Sinh từng token đầu ra dựa trên context vector và trạng thái trước đó
$$
s_t = \text{DecoderRNN}(y_{t-1}, s_{t-1}, c)
$$
$$
y_t = \text{softmax}(W s_t)
$$

### 3.3 Attention (nếu có)
- Giải quyết vấn đề **context vector cô đặc thông tin**
- Mỗi bước đầu ra có **trọng số attention** trên các trạng thái encoder
$$
\alpha_{t,i} = \frac{\exp(score(s_{t-1}, h_i))}{\sum_j \exp(score(s_{t-1}, h_j))}
$$
$$
c_t = \sum_i \alpha_{t,i} h_i
$$

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

Python example với `TensorFlow` / `Keras`:

```python
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense

# Encoder
encoder_inputs = Input(shape=(None, num_encoder_tokens))
encoder_lstm = LSTM(256, return_state=True)
encoder_outputs, state_h, state_c = encoder_lstm(encoder_inputs)
encoder_states = [state_h, state_c]

# Decoder
decoder_inputs = Input(shape=(None, num_decoder_tokens))
decoder_lstm = LSTM(256, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_inputs, initial_state=encoder_states)
decoder_dense = Dense(num_decoder_tokens, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

# Model
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
````

## 5. Ví dụ code (Code Examples)

* Training Seq2Seq:

```python
model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
model.fit([encoder_input_data, decoder_input_data], decoder_target_data,
          batch_size=64,
          epochs=50,
          validation_split=0.2)
```

* Sử dụng attention với TensorFlow Addons hoặc PyTorch:

```python
import torch
import torch.nn as nn

# attention score example
score = torch.bmm(decoder_hidden.unsqueeze(1), encoder_outputs.transpose(0,1).unsqueeze(0))
attention_weights = torch.softmax(score, dim=-1)
context_vector = torch.bmm(attention_weights, encoder_outputs)
```

## 6. Lỗi thường gặp (Common Pitfalls)

* Chuỗi đầu vào quá dài → thông tin cô đặc mất mát
* Không dùng attention → khó học các phụ thuộc dài
* Không chuẩn hóa tokenization → từ hiếm không học được
* Không padding hoặc masking đúng → mô hình học sai sequence

## 7. So sánh với khái niệm liên quan (Comparison)

| Kiến trúc           | Điểm mạnh                                     | Điểm yếu                                      |
| ------------------- | --------------------------------------------- | --------------------------------------------- |
| Seq2Seq cơ bản      | Đơn giản, dễ triển khai                       | Khó học phụ thuộc dài, context vector cố định |
| Seq2Seq + Attention | Giải quyết phụ thuộc dài                      | Phức tạp hơn, tính toán nặng                  |
| Transformer         | Parallelizable, capture long-range dependency | Dữ liệu & tài nguyên lớn, phức tạp            |

## 8. Ứng dụng trong thực tế (Practical Insights)

* Google Translate ban đầu dùng RNN Seq2Seq, giờ chuyển sang Transformer
* Chatbot: encoder đọc câu hỏi, decoder sinh câu trả lời
* Tóm tắt văn bản tự động: encoder đọc văn bản dài, decoder tạo summary ngắn

## 9. Câu hỏi phỏng vấn (Interview Questions)

1. Seq2Seq là gì? Giải thích cơ chế encoder-decoder.
2. Tại sao cần attention trong Seq2Seq?
3. Lợi ích của LSTM/GRU so với RNN thông thường trong Seq2Seq?
4. Khi nào nên dùng Transformer thay vì RNN Seq2Seq?
5. Padding và masking hoạt động như thế nào trong Seq2Seq?

## 10. TL;DR (Short Summary)

Seq2Seq là kiến trúc biến chuỗi đầu vào thành chuỗi đầu ra, thường dùng encoder-decoder. Attention giúp giải quyết phụ thuộc dài. Ứng dụng: dịch máy, tóm tắt, chatbot. LSTM/GRU giúp giữ thông tin sequence, Transformers giải quyết hạn chế tính toán song song và phụ thuộc dài.
