---
title: Embeddings Basics
description: Ghi chú về Embeddings trong machine learning và NLP, cách biểu diễn dữ liệu dưới dạng vector, các loại embeddings phổ biến và ứng dụng.
tags: [Embeddings, Word Embedding, NLP, Deep Learning, Representation Learning]
---

## 1. Tóm tắt khái niệm (Definition)

Embeddings là cách ánh xạ các đối tượng rời rạc (words, tokens, items) vào không gian vector liên tục, giúp máy tính hiểu và tính toán các mối quan hệ giữa chúng.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Biểu diễn từ/ngôn ngữ cho NLP.
* Recommendation system: embedding sản phẩm và người dùng.
* Graph embeddings: biểu diễn node/edge.
* Khi cần máy học hiểu mối quan hệ ngữ nghĩa hoặc similarity giữa các đối tượng.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* Học embedding dựa trên co-occurrence hoặc supervised signal.
* Mỗi từ/tokens được ánh xạ thành vector $\mathbf{v} \in \mathbb{R}^d$.
* Khoảng cách hoặc cosine similarity giữa vector phản ánh sự tương đồng.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

* One-hot vector: $\mathbf{x} \in {0,1}^V$
* Embedding lookup:
  $$
  \mathbf{v} = E \mathbf{x}
  $$
  Trong đó $E \in \mathbb{R}^{V \times d}$ là ma trận embedding, V: vocabulary size, d: embedding dimension.

Cosine similarity:
$$
\text{sim}(\mathbf{v}_1, \mathbf{v}_2) = \frac{\mathbf{v}_1 \cdot \mathbf{v}_2}{|\mathbf{v}_1| |\mathbf{v}_2|}
$$

---

## 5. Ví dụ code (Code Examples)

```python
from tensorflow.keras.layers import Embedding
import tensorflow as tf

vocab_size = 10000
dim = 128
embedding_layer = Embedding(input_dim=vocab_size, output_dim=dim)

sample_input = tf.constant([1, 5, 7])
embedded = embedding_layer(sample_input)
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Dimensionality quá thấp → mất thông tin.
* Dimensionality quá cao → overfitting.
* Không normalize vectors khi dùng cosine similarity.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* One-hot vs Embedding:

  * One-hot: sparse, không phản ánh similarity.
  * Embedding: dense, phản ánh similarity và ngữ nghĩa.
* Pre-trained embeddings (Word2Vec, GloVe, FastText) vs học từ đầu:

  * Pre-trained: tiết kiệm thời gian, transfer learning.
  * Học từ đầu: tùy dataset, task.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* NLP: text classification, machine translation, sentiment analysis.
* Recommendation: embedding user/item.
* Graph neural networks: node embeddings.
* Semantic search và retrieval.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Embedding là gì và tại sao dùng?
* One-hot vector và embedding khác nhau thế nào?
* Cosine similarity dùng để làm gì?
* Khi nào nên dùng pre-trained embeddings?

---

## 10. TL;DR (Short Summary)

* Embeddings ánh xạ đối tượng rời rạc thành vector liên tục.
* Ma trận embedding E: lookup vector từ one-hot.
* Cosine similarity đo similarity giữa vector.
* Dùng trong NLP, recommendation, graph learning.
