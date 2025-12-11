---
title: "Gradient Boosting (XGBoost | LightGBM | CatBoost)"
description: "Tổng quan kỹ thuật về Gradient Boosting và ba triển khai phổ biến: XGBoost, LightGBM, CatBoost."
tags: ["Machine Learning", "Gradient Boosting", "XGBoost", "LightGBM", "CatBoost", "Ensemble"]
---

# Gradient Boosting (XGBoost | LightGBM | CatBoost)

Gradient Boosting là phương pháp **ensemble** theo hướng **boosting tuần tự**, nơi mỗi base learner (thường là cây quyết định nhỏ) học để sửa lỗi (residual) của tổng mô hình trước đó. Kết quả là một mô hình mạnh, ưu thế đặc biệt trên dữ liệu bảng (tabular data).

---

## 1. Ý tưởng cốt lõi

* Mô hình được xây dựng tuần tự: (F_m(x) = F_{m-1}(x) + \eta \cdot h_m(x)), với (h_m) là learner mới học gradient của loss.
* Sử dụng gradient (và đôi khi là Hessian — gradient bậc hai) để tối ưu hóa hàm mất mát.
* Thích hợp cho các bài toán regression và classification (binary / multiclass).

---

## 2. Các thành phần chung

* **Weak learner:** thường là Decision Tree nông (shallow tree).
* **Learning rate ((\eta))**: bước cập nhật, nhỏ hơn giúp mô hình tổng quát tốt hơn nhưng cần nhiều estimator.
* **n_estimators**: số cây/rounds.
* **Regularization**: giảm overfitting (L1/L2, subsample, colsample).

---

## 3. XGBoost (Extreme Gradient Boosting)

### 3.1. Đặc điểm

* Sử dụng **second-order gradient** (gradient + hessian) để tối ưu hiệu quả.
* Hỗ trợ **regularization (L1, L2)** ngay trong objective.
* Xử lý dữ liệu **sparse/missing** tốt (sparse-aware split).
* Tree building: histogram / optimized algorithms.

### 3.2. Ưu / Nhược

* **Ưu:** ổn định, mạnh mẽ trên tabular data, kiểm soát overfitting tốt.
* **Nhược:** chậm hơn LightGBM trên data rất lớn; cần tuning nhiều tham số.

### 3.3. Hyperparameters quan trọng

`eta`, `max_depth`, `subsample`, `colsample_bytree`, `lambda`, `alpha`, `n_estimators`.

---

## 4. LightGBM

### 4.1. Đặc điểm

* Tối ưu cho tốc độ và hiệu quả bộ nhớ.
* **Leaf-wise growth** (grow deepest leaf first) thay vì level-wise → độ giảm loss nhanh hơn.
* Kỹ thuật: **GOSS (Gradient-based One-Side Sampling)** và **EFB (Exclusive Feature Bundling)** để tăng tốc và giảm chiều.

### 4.2. Ưu / Nhược

* **Ưu:** rất nhanh trên dataset lớn, dùng ít RAM, hiệu quả với nhiều feature.
* **Nhược:** leaf-wise có thể dẫn đến overfitting nếu không điều chỉnh; nhạy với noisy data.

### 4.3. Hyperparameters quan trọng

`num_leaves`, `max_depth`, `learning_rate`, `feature_fraction`, `bagging_fraction`, `min_data_in_leaf`, `lambda_l1`, `lambda_l2`.

---

## 5. CatBoost

### 5.1. Đặc điểm

* Thiết kế đặc biệt để xử lý **categorical features** hiệu quả (ordered target statistics, permutations).
* Dùng **oblivious trees** (symmetric trees) trong nhiều cấu hình.
* Thường cần ít preprocessing (encoding) cho categorical data.

### 5.2. Ưu / Nhược

* **Ưu:** làm việc xuất sắc với categorical features, ít cần tuning, ổn định trong nhiều trường hợp.
* **Nhược:** đôi khi chậm hơn LightGBM; cấu trúc tree đặc trưng có thể hạn chế một số tuỳ biến.

### 5.3. Hyperparameters quan trọng

`learning_rate`, `depth`, `iterations`, `l2_leaf_reg`, `bagging_temperature`, `one_hot_max_size`.

---

## 6. So sánh tóm tắt

| Tiêu chí             |         XGBoost |           LightGBM |     CatBoost |
| -------------------- | --------------: | -----------------: | -----------: |
| Tốc độ trên data lớn |             Tốt |       **Tốt nhất** |   Trung bình |
| Xử lý categorical    | Manual encoding |    Manual encoding | **Tốt nhất** |
| Dễ overfit           |      Trung bình | Dễ hơn (leaf-wise) |       Ít hơn |
| Cần tuning           |              Có |                 Có |       Ít hơn |
| Memory               |      Trung bình |          Tiết kiệm |   Trung bình |

---

## 7. Khi chọn công cụ nào?

* Nếu dataset rất lớn và cần tốc độ → **LightGBM**.
* Nếu nhiều categorical và muốn ít preprocessing → **CatBoost**.
* Nếu cần ổn định, kiểm soát overfitting tốt và muốn tận dụng second-order info → **XGBoost**.

---

## 8. Những lưu ý khi thực tế

* Luôn **tune learning_rate + n_estimators** cùng nhau (small lr + many estimators hoặc ngược lại).
* Dùng **early stopping** trên validation set để tránh overfitting.
* Thử **subsample / colsample** để giảm tương quan giữa cây và variance.
* Với categorical large-cardinality, dùng CatBoost hoặc careful encoding.

---

## 9. Câu trả lời phỏng vấn mẫu (ngắn)

> Gradient Boosting là boosting tuần tự, mỗi cây sửa lỗi của mô hình trước. XGBoost mạnh nhờ regularization và hessian; LightGBM nhanh nhờ leaf-wise growth và sampling; CatBoost xuất sắc với categorical nhờ ordered target encoding.

---

## 10. Tham khảo nhanh

* XGBoost docs, LightGBM docs, CatBoost docs (tham khảo trực tiếp khi cần chi tiết hyperparameter).