---
title: Word Embeddings in NLP
description: Ghi chú về word embeddings trong NLP, bao gồm khái niệm, cách biểu diễn từ, các phương pháp phổ biến như Word2Vec, GloVe, FastText, và ứng dụng trong deep learning.
tags: [Deep Learning, NLP, Word Embeddings, Vectorization, Word2Vec, GloVe, FastText]
---

## 1. Khái niệm

Word embeddings là kỹ thuật biểu diễn từ (words) dưới dạng vector số thực trong không gian nhiều chiều sao cho các từ có nghĩa tương tự sẽ gần nhau về mặt hình học. Khác với one-hot encoding, embeddings thể hiện **ngữ nghĩa**, giúp mô hình học ngôn ngữ hiệu quả hơn.

Ví dụ:
$$
\text{vector}("king") - \text{vector}("man") + \text{vector}("woman") \approx \text{vector}("queen")
$$

## 2. Mục đích & khi nào dùng (Use Cases)

- Biểu diễn từ thành dạng số để mô hình Deep Learning có thể xử lý.
- Giữ thông tin ngữ nghĩa và mối quan hệ giữa các từ.
- Sử dụng trong:
  - Text classification
  - Named Entity Recognition
  - Machine Translation
  - Question Answering
  - Similarity & Recommendation

## 3. Cách hoạt động bên trong (Internal Logic)

### 3.1 Word2Vec
- **CBOW (Continuous Bag of Words)**: dự đoán từ trung tâm dựa trên context.
- **Skip-gram**: dự đoán context dựa trên từ trung tâm.
  
Mục tiêu tối ưu hàm mất mát:

$$
\text{maximize } \sum_{t=1}^{T} \sum_{-c \le j \le c, j \ne 0} \log P(w_{t+j} | w_t)
$$

### 3.2 GloVe (Global Vectors)
- Sử dụng ma trận đồng xuất hiện từ (co-occurrence matrix) để học embeddings.
- Mục tiêu tối ưu:

$$
J = \sum_{i,j=1}^V f(X_{ij}) \left( w_i^T \tilde{w}_j + b_i + \tilde{b}_j - \log X_{ij} \right)^2
$$

### 3.3 FastText
- Biểu diễn từ bằng n-grams, giúp xử lý từ hiếm và morphology.
- Vector từ = tổng vector các n-gram của từ đó.

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

Python example với `gensim`:

```python
import gensim
from gensim.models import Word2Vec

sentences = [["deep", "learning", "is", "fun"], ["nlp", "with", "embeddings"]]
model = Word2Vec(sentences, vector_size=50, window=2, min_count=1, sg=1)  # sg=1 -> skip-gram

vector_king = model.wv["king"]
similar_words = model.wv.most_similar("king", topn=5)
print(similar_words)
````

Với GloVe, tải pre-trained embeddings:

```python
import gensim.downloader as api

glove_model = api.load("glove-wiki-gigaword-100")  # 100-dim vector
vector_queen = glove_model["queen"]
```

## 5. Ví dụ code (Code Examples)

* Tìm từ tương tự:

```python
similar = model.wv.most_similar("woman", topn=3)
print(similar)
# [('girl', 0.89), ('lady', 0.85), ('queen', 0.82)]
```

* Phép tính ngữ nghĩa:

```python
result = model.wv.most_similar(positive=["king", "woman"], negative=["man"])
print(result[0][0])  # Output: 'queen'
```

## 6. Lỗi thường gặp (Common Pitfalls)

* Chỉ dùng one-hot encoding thay vì embeddings sẽ làm mất ngữ nghĩa.
* Không xử lý từ hiếm hoặc typo → embeddings không đầy đủ.
* Sử dụng embeddings sai ngữ cảnh (word sense disambiguation).
* Chưa chuẩn hóa tokenization và lowercase trước khi training embeddings.

## 7. So sánh với khái niệm liên quan (Comparison)

| Phương pháp | Điểm mạnh                    | Điểm yếu                               |
| ----------- | ---------------------------- | -------------------------------------- |
| One-hot     | Đơn giản                     | Không giữ ngữ nghĩa, vector rất sparse |
| Word2Vec    | Hiệu quả, capture context    | Không handle từ hiếm tốt               |
| GloVe       | Capture global co-occurrence | Cần nhiều dữ liệu, static embeddings   |
| FastText    | Xử lý morphology & từ hiếm   | Vector lớn hơn, training chậm hơn      |

## 8. Ứng dụng trong thực tế (Practical Insights)

* Chatbot: biểu diễn câu hỏi và câu trả lời thành embeddings.
* Search engines & recommendation: tính similarity giữa từ, câu hoặc document.
* Machine translation: embeddings làm input cho seq2seq hoặc transformer.
* Sentiment analysis: vector hóa review sản phẩm.

## 9. Câu hỏi phỏng vấn (Interview Questions)

1. Word embeddings là gì? Tại sao không dùng one-hot encoding?
2. So sánh Word2Vec, GloVe và FastText.
3. Phép tính `king - man + woman ≈ queen` hoạt động như thế nào?
4. Khi nào cần dùng pre-trained embeddings, khi nào train từ đầu?
5. Embeddings có nhược điểm gì?

## 10. TL;DR (Short Summary)

Word embeddings chuyển từ thành vector số thực giữ thông tin ngữ nghĩa. Các phương pháp phổ biến: Word2Vec (CBOW/Skip-gram), GloVe (co-occurrence), FastText (n-grams). Giúp mô hình NLP hiểu từ, cải thiện chất lượng dự đoán, tìm từ tương tự, và ứng dụng trong nhiều task NLP.