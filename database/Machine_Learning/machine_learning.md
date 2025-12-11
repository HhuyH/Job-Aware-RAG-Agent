---
title: "Machine Learning"
description: "Tổng quan về Machine Learning."
tags: ["Machine Learning"]
---

# Machine Learning

Machine Learning là một nhánh của trí tuệ nhân tạo, trong đó hệ thống học từ dữ liệu để đưa ra dự đoán hoặc quyết định mà không cần lập trình rõ từng quy tắc.  
Thay vì viết từng logic thủ công, mô hình sẽ tự rút ra mẫu (pattern) từ dữ liệu, tối ưu tham số và cải thiện hiệu suất khi lượng dữ liệu tăng lên.

---

## 1. Hiểu workflow Machine Learning

### 1.1. Phân biệt Supervised / Unsupervised / Reinforcement Learning

#### Supervised Learning (Học có giám sát)

**Bản chất:**
- Mô hình học từ tập dữ liệu có nhãn (labelled data), tức là mỗi mẫu đầu vào (`x`) đều đi kèm đầu ra mong muốn (`y`).
- Mục tiêu là tìm ra hàm ánh xạ (`f(x) ≈ y`) để dự đoán nhãn của dữ liệu mới.

**Quy trình:**
1. Cung cấp tập dữ liệu (input + label).  
2. Mô hình học cách khớp đầu vào với đầu ra.  
3. Đánh giá trên dữ liệu test và điều chỉnh để giảm sai số.  

**Ví dụ:**
- Phân loại email: spam / không spam  
- Dự đoán giá nhà, dự đoán nhiệt độ, nhận diện khuôn mặt  

**Thuật toán thường dùng:**  
Linear/Logistic Regression, Decision Tree, Random Forest, SVM, Neural Network

---

#### Unsupervised Learning (Học không giám sát)

**Bản chất:**
- Dữ liệu không có nhãn (unlabelled data).  
- Mục tiêu là khám phá cấu trúc tiềm ẩn, mối quan hệ hoặc mẫu (pattern) trong dữ liệu.

**Cách hoạt động:**
- Mô hình cố gắng nhóm hoặc biểu diễn dữ liệu theo đặc điểm tương đồng.  
- Không có “đáp án đúng”, mà chỉ tìm mô hình mô tả tốt nhất dữ liệu.

**Ví dụ:**
- **Clustering (phân cụm):** nhóm khách hàng có hành vi tương tự (K-means, DBSCAN)  
- **Dimensionality Reduction (giảm chiều):** PCA, t-SNE — dùng để nén dữ liệu hoặc tiền xử lý cho mô hình khác  
- **Association Rule Learning:** phát hiện mối quan hệ kiểu “mua A thì thường mua B”

**Ứng dụng thực tế:**  
Phân khúc thị trường, gợi ý sản phẩm, phát hiện bất thường (anomaly detection)

---

#### Reinforcement Learning (Học tăng cường)

**Bản chất:**
- Hệ thống học thông qua tương tác với môi trường.  
- Gồm Agent (người học) và Environment (môi trường).  
- Mục tiêu: học chính sách hành động (policy) để tối đa hóa tổng phần thưởng (reward) theo thời gian.

**Cơ chế học:**
1. Agent thực hiện hành động (`a_t`) trong trạng thái (`s_t`).  
2. Môi trường phản hồi bằng phần thưởng (`r_t`) và trạng thái mới (`s_{t+1}`).  
3. Agent điều chỉnh chiến lược để nhận nhiều reward hơn trong dài hạn.

**Ví dụ và ứng dụng:**
- AlphaGo (DeepMind) – học cách chơi cờ vây thông qua tự chơi  
- Robot tự hành – học cách di chuyển an toàn  
- Trading algorithm – tối ưu lợi nhuận  
- Quảng cáo – tối ưu lựa chọn hiển thị quảng cáo  

**Thuật toán tiêu biểu:**  
Q-Learning, Deep Q-Network (DQN), Policy Gradient, Actor-Critic, PPO

---

### Tóm tắt nhanh khi phỏng vấn

| Loại học       | Dữ liệu có nhãn?         | Mục tiêu                     | Ví dụ điển hình                     |
|----------------|--------------------------|------------------------------|-------------------------------------|
| Supervised     | Có                       | Dự đoán đầu ra (label)       | Phân loại email, dự đoán giá        |
| Unsupervised   | Không                    | Tìm cấu trúc hoặc nhóm ẩn    | Phân cụm khách hàng                 |
| Reinforcement  | Không (học qua tương tác)| Tối đa hóa phần thưởng       | Game, robot, trading                |

**Câu chốt gọn khi trả lời phỏng vấn:**  
- Supervised học từ dữ liệu có nhãn để dự đoán  
- Unsupervised khám phá cấu trúc trong dữ liệu không nhãn  
- Reinforcement học bằng cách thử – sai và tối ưu phần thưởng qua tương tác môi trường

---

### 1.2. Quy trình ML cơ bản
1. Thu thập & tiền xử lý dữ liệu (data cleaning, normalization, encoding)  
2. Chia dữ liệu: train / validation / test  
3. Chọn mô hình (linear regression, tree, v.v.)  
4. Train model → predict → evaluate (accuracy, precision, recall, v.v.)  
5. Fine-tune (hyperparameter tuning, cross-validation)  

---

### 1.3. Tổng quan toàn bộ Machine Learning

#### 1.3.1. Mục tiêu chung của Machine Learning
Cho máy tự học từ dữ liệu để rút ra quy luật và dự đoán hoặc phân loại trong tương lai.  
Cách máy “học” phụ thuộc vào dạng dữ liệu đầu vào (input) và điều ta muốn dự đoán (output).  
→ Từ đó chia thành 3 nhánh chính.

#### 1.3.2. Ba nhánh chính của Machine Learning

| Nhánh                     | Output                        | Có nhãn không? | Mục tiêu                                | Ví dụ thực tế                       |
|---------------------------|-------------------------------|----------------|-----------------------------------------|-------------------------------------|
| Supervised Learning       | Có output (label)             | Có             | Học quy luật từ dữ liệu đã gắn nhãn     | Dự đoán, phân loại                  |
| Unsupervised Learning     | Không có output (label)       | Không          | Khám phá cấu trúc ẩn trong dữ liệu      | Phân cụm, giảm chiều                |
| Reinforcement Learning    | Phản hồi (reward/punishment)  | Tự sinh        | Học cách hành động tối ưu qua thử–sai   | Robot, game, trading                |
