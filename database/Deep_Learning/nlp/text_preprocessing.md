---
title: Text Preprocessing in NLP
description: Ghi chú về các bước tiền xử lý văn bản trong NLP, bao gồm tokenization, normalization, stemming, lemmatization, và cách xử lý đặc biệt như stopwords, punctuation, hay encoding.
tags: [Deep Learning, NLP, Text Preprocessing, Tokenization, Normalization]
---

## 1. Khái niệm

Text preprocessing là bước chuẩn bị dữ liệu văn bản trước khi đưa vào mô hình NLP. Mục đích là làm sạch, chuẩn hóa, và biến đổi văn bản thô thành dạng mà mô hình máy học hoặc deep learning có thể hiểu và xử lý hiệu quả.  

Các bước phổ biến:
- Tokenization
- Lowercasing / Normalization
- Stopword removal
- Stemming / Lemmatization
- Handling punctuation, numbers, special characters
- Encoding (One-hot, TF-IDF, embeddings)

## 2. Mục đích & khi nào dùng (Use Cases)

- Chuẩn hóa văn bản đầu vào cho các mô hình NLP: classification, sentiment analysis, machine translation, question answering.
- Giảm độ phức tạp của dữ liệu, giúp mô hình học nhanh và tránh overfitting.
- Loại bỏ các yếu tố nhiễu (noise) như dấu câu, ký tự đặc biệt, hay stopwords không mang thông tin.

## 3. Cách hoạt động bên trong (Internal Logic)

### 3.1 Tokenization
Chia văn bản thành các đơn vị nhỏ (tokens), ví dụ:
```text
"Deep Learning is fun!" → ["Deep", "Learning", "is", "fun", "!"]
````

### 3.2 Normalization

Chuyển văn bản về dạng chuẩn, ví dụ:

* Lowercasing: `"Deep"` → `"deep"`
* Unicode normalization
* Loại bỏ whitespace thừa

### 3.3 Stopword Removal

Xóa các từ không mang nhiều thông tin như: "the", "is", "and", ...

### 3.4 Stemming / Lemmatization

* **Stemming**: cắt đuôi từ về gốc cơ bản.
* **Lemmatization**: chuyển từ về dạng lemma chuẩn xác dựa trên ngữ pháp.

$$
\text{stemming}("running") \rightarrow "run"
$$

$$
\text{lemmatization}("running") \rightarrow "run"
$$

### 3.5 Encoding

Chuyển tokens thành dạng số để mô hình xử lý:

* One-hot encoding
* Bag-of-Words (BoW)
* TF-IDF
* Word embeddings: Word2Vec, GloVe, FastText

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

Ví dụ Python sử dụng `nltk` và `spacy`:

```python
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import spacy

text = "Deep Learning is fun!"
tokens = nltk.word_tokenize(text.lower())
tokens = [t for t in tokens if t.isalpha()]  # loại bỏ punctuation
tokens = [t for t in tokens if t not in stopwords.words('english')]

ps = PorterStemmer()
stemmed_tokens = [ps.stem(t) for t in tokens]

nlp = spacy.load("en_core_web_sm")
lemmatized_tokens = [token.lemma_ for token in nlp(text)]
```

## 5. Ví dụ code (Code Examples)

* TF-IDF vectorization:

```python
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = ["Deep Learning is fun", "I love NLP"]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(X.toarray())
```

* Word embeddings:

```python
import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")
vector = model["learning"]  # 50-dim vector
```

## 6. Lỗi thường gặp (Common Pitfalls)

* Loại bỏ quá nhiều thông tin khi xóa stopwords hoặc punctuation.
* Tokenization không chính xác với ngôn ngữ có dấu hoặc tiếng Việt.
* Sử dụng stemming quá nặng gây mất nghĩa từ.
* Không xử lý encoding hoặc special characters, dẫn đến lỗi khi vector hóa.

## 7. So sánh với khái niệm liên quan (Comparison)

| Bước              | Mục đích                  | Lưu ý                                         |
| ----------------- | ------------------------- | --------------------------------------------- |
| Stemming          | Giảm từ về gốc đơn giản   | Nhanh, nhưng đôi khi mất nghĩa                |
| Lemmatization     | Chuẩn hóa từ dựa ngữ pháp | Chính xác hơn nhưng chậm hơn                  |
| Stopwords removal | Loại bỏ từ dư thừa        | Không nên xóa nếu mô hình cần ngữ cảnh đầy đủ |
| Tokenization      | Chia văn bản thành đơn vị | Quan trọng với mô hình ngôn ngữ               |

## 8. Ứng dụng trong thực tế (Practical Insights)

* Sentiment analysis: làm sạch dữ liệu Twitter, review sản phẩm.
* Chatbot: chuẩn hóa câu hỏi người dùng trước khi embedding.
* Machine translation: loại bỏ noise, chuẩn hóa tokens trước khi huấn luyện mô hình seq2seq.
* Search & Information Retrieval: TF-IDF, embeddings phục vụ ranking.

## 9. Câu hỏi phỏng vấn (Interview Questions)

1. Vì sao phải tiền xử lý văn bản trong NLP?
2. Stemming khác gì Lemmatization? Khi nào dùng mỗi phương pháp?
3. Làm sao xử lý văn bản tiếng Việt khác với tiếng Anh?
4. TF-IDF là gì? Có ưu nhược điểm gì so với embeddings?
5. Khi nào nên giữ stopwords, khi nào nên loại bỏ?

## 10. TL;DR (Short Summary)

Text preprocessing là bước làm sạch và chuẩn hóa văn bản trước khi đưa vào mô hình NLP. Bao gồm tokenization, normalization, stopwords removal, stemming/lemmatization, và encoding. Giúp giảm noise, tăng hiệu quả học, và chuẩn bị dữ liệu cho mọi mô hình NLP.


