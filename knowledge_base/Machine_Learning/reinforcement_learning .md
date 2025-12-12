---
title: "Reinforcement Learning"
description: "Tổng quan về Reinforcement Learning, cơ chế học, thuật toán và ứng dụng thực tế trong Machine Learning."
tags: ["Machine Learning", "Reinforcement Learning"]
---

# Reinforcement Learning (Học tăng cường)

**Bản chất:**  
- Hệ thống học thông qua **tương tác với môi trường**.  
- Bao gồm **Agent** (người học) và **Environment** (môi trường).  
- Mục tiêu: học **chính sách hành động (policy)** để tối đa hóa tổng **phần thưởng (reward)** theo thời gian.

---

## 1. Cơ chế học

1. Agent thực hiện hành động (`a_t`) trong trạng thái (`s_t`)  
2. Môi trường phản hồi bằng phần thưởng (`r_t`) và trạng thái mới (`s_{t+1}`)  
3. Agent điều chỉnh chiến lược để **nhận nhiều reward hơn trong dài hạn**

> Đây là quá trình **thử – sai (trial-and-error)**, khác với supervised/unsupervised vì không cần nhãn dữ liệu.

---

## 2. Ví dụ và ứng dụng

| Ứng dụng                   | Mô tả                                                  |
|----------------------------|--------------------------------------------------------|
| AlphaGo (DeepMind)         | Học cách chơi cờ vây thông qua tự chơi                 |
| Robot tự hành              | Học cách di chuyển an toàn và tối ưu hành vi           |
| Trading algorithm          | Tối ưu lợi nhuận trong giao dịch                       |
| Quảng cáo                  | Tối ưu lựa chọn hiển thị quảng cáo                     |

---

## 3. Thuật toán tiêu biểu

- **Q-Learning**  
- **Deep Q-Network (DQN)**  
- **Policy Gradient**  
- **Actor-Critic**  
- **Proximal Policy Optimization (PPO)**  

---

## 4. Tóm tắt nhanh cho phỏng vấn

**Câu chốt gọn:**  
- Reinforcement Learning học bằng cách thử – sai và tối ưu phần thưởng qua tương tác với môi trường.

| Khía cạnh         | Chi tiết                                                       |
|-------------------|----------------------------------------------------------------|
| Dữ liệu           | Không nhãn, học qua tương tác với môi trường                   |
| Mục tiêu          | Tối đa hóa tổng reward dài hạn                                 |
| Ví dụ điển hình   | Game, robot, trading, hệ thống tối ưu quảng cáo                |

---

## 5. Ghi chú thêm

- Hiệu quả phụ thuộc vào **cách thiết kế reward** và **môi trường mô phỏng**.  
- Thường kết hợp với **Deep Learning** để học **policy phức tạp** trong môi trường lớn (Deep Reinforcement Learning).
