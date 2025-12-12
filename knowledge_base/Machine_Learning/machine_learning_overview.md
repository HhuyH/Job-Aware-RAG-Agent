---
title: "Machine Learning Overview"
description: "Tổng quan toàn diện về Machine Learning, bao gồm Supervised, Unsupervised và Reinforcement Learning."
tags: ["Machine Learning", "Supervised Learning", "Unsupervised Learning", "Reinforcement Learning"]
---

# Machine Learning Overview

Machine Learning là một nhánh của trí tuệ nhân tạo, trong đó hệ thống học từ dữ liệu để rút ra quy luật và đưa ra dự đoán/ quyết định mà không cần lập trình thủ công từng quy tắc.

ML chia thành ba nhánh chính dựa trên dạng dữ liệu và mục tiêu học:

- **Supervised Learning**
- **Unsupervised Learning**
- **Reinforcement Learning**

---

# Table of Contents

1. [Supervised Learning](#supervised-learning)
2. [Unsupervised Learning](#unsupervised-learning)
3. [Reinforcement Learning](#reinforcement-learning)
4. [Comparison Summary](#comparison-summary)

---

# Supervised Learning

## 1. Bản chất

- Dữ liệu **có nhãn** (labelled data)  
- Mục tiêu: học hàm ánh xạ `f(x) ≈ y` để dự đoán cho dữ liệu mới  

## 2. Quy trình

1. Chuẩn bị dữ liệu (input + label)  
2. Train mô hình  
3. Đánh giá – tinh chỉnh  

## 3. Ví dụ

| Bài toán       | Ứng dụng                        |
|----------------|---------------------------------|
| Classification | Spam vs. không spam             |
| Regression     | Dự đoán giá nhà                 |
| Recognition    | Nhận diện khuôn mặt             |

## 4. Thuật toán phổ biến

- Linear / Logistic Regression  
- Decision Tree, Random Forest  
- SVM  
- Neural Network  

## 5. Tóm tắt phỏng vấn

> Supervised Learning học từ dữ liệu có nhãn để dự đoán đầu ra.

---

# Unsupervised Learning

## 1. Bản chất

- Dữ liệu **không có nhãn**  
- Mục tiêu: khám phá **cấu trúc, nhóm, mẫu ẩn** trong dữ liệu  
- Không có “đáp án đúng”  

## 2. Ví dụ chính

| Phương pháp                   | Mục đích                             | Thuật toán tiêu biểu  |
|-------------------------------|--------------------------------------|-----------------------|
| Clustering                    | Nhóm khách hàng                      | K-means, DBSCAN       |
| Dimensionality Reduction      | Giảm chiều, nén dữ liệu              | PCA, t-SNE            |
| Association Rule Learning     | Tìm luật “mua A hay mua B”           | Apriori, Eclat        |

## 3. Ứng dụng thực tế

- Phân khúc thị trường  
- Gợi ý sản phẩm  
- Anomaly Detection  

## 4. Tóm tắt phỏng vấn

> Unsupervised Learning khám phá cấu trúc trong dữ liệu không nhãn.

---

# Reinforcement Learning

## 1. Bản chất

- Agent tương tác với Environment  
- Nhận reward → cải thiện policy để tối đa hóa **tổng phần thưởng dài hạn**  
- Học bằng cơ chế **trial-and-error**  

## 2. Chu trình RL

1. Agent ở trạng thái `s_t`  
2. Thực hiện hành động `a_t`  
3. Nhận reward `r_t` và trạng thái mới `s_{t+1}`  
4. Điều chỉnh chính sách  

## 3. Ứng dụng điển hình

| Ứng dụng       | Mô tả                                  |
|----------------|----------------------------------------|
| AlphaGo        | Tự học chơi cờ vây                     |
| Robot control  | Điều khiển robot tự hành               |
| Trading        | Tối ưu chiến lược giao dịch            |
| Advertising    | Tối ưu phân phối quảng cáo             |

## 4. Thuật toán tiêu biểu

- Q-Learning  
- Deep Q-Network (DQN)  
- Policy Gradient  
- Actor-Critic  
- PPO  

## 5. Tóm tắt phỏng vấn

> Reinforcement Learning học qua tương tác và tối ưu phần thưởng.

---

# Comparison Summary

| Loại học              | Dữ liệu nhãn | Mục tiêu                             | Ví dụ thực tế                 |
|-----------------------|--------------|--------------------------------------|-------------------------------|
| Supervised Learning   | Có           | Dự đoán đầu ra                       | Dự đoán giá, phân loại email  |
| Unsupervised Learning | Không        | Khám phá cấu trúc ẩn                 | Phân cụm khách hàng           |
| Reinforcement Learning|  Reward      | Tối đa hóa phần thưởng dài hạn       | Game, robot, trading          |

---

# Câu chốt gọn cho phỏng vấn

- **Supervised**: học từ dữ liệu có nhãn để dự đoán.  
- **Unsupervised**: tìm cấu trúc tiềm ẩn trong dữ liệu không nhãn.  
- **Reinforcement**: học bằng thử–sai, tối ưu phần thưởng qua tương tác môi trường.  
