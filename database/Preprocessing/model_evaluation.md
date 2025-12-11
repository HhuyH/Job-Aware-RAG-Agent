---
title: "Model Evaluation"
description: "Khái niệm, mục đích và quy trình đánh giá mô hình Machine Learning/DL."
tags: ["Model Evaluation", "Metrics", "Machine Learning"]
---

# Model Evaluation

Model evaluation là quá trình đo lường mức độ tốt – xấu của mô hình ML/DL trên dữ liệu chưa thấy trong quá trình huấn luyện. Mục tiêu chính là kiểm tra khả năng **tổng quát hóa**, phát hiện **overfitting/underfitting**, và xác định mô hình có đủ điều kiện triển khai thực tế hay không.

---

## 1. Mục đích

* Xác định mô hình có hoạt động tốt hay không so với yêu cầu bài toán.
* So sánh nhiều mô hình để chọn mô hình tối ưu.
* Theo dõi chất lượng trong quá trình training và deployment.
* Ngăn chặn mô hình chỉ học thuộc dữ liệu train (prevent memorization/leakage).

---

## 2. Các bước chính trong quy trình đánh giá

1. **Tách dữ liệu**: Train / Validation / Test (hoặc dùng cross-validation).
2. **Chọn metric phù hợp** với bản chất bài toán (classification / regression / ranking).
3. **Huấn luyện** trên train, **tuning** trên validation.
4. **Đánh giá cuối cùng** trên test set (chỉ sau khi hoàn thiện model).
5. **Phân tích lỗi (Error analysis)**: inspect false positive/negative, residuals, edge cases.
6. **Lặp lại**: điều chỉnh feature/hyperparams/kiến trúc → đánh giá lại.

---

## 3. Metric phổ biến

### 3.1. Classification

* **Accuracy** – tỉ lệ dự đoán đúng (dùng khi dữ liệu cân bằng).
* **Precision, Recall** – đánh giá trade-off giữa FP và FN.
* **F1-score** – harmonic mean giữa precision & recall.
* **Confusion Matrix** – phân tích chi tiết lỗi.
* **ROC-AUC / PR-AUC** – đánh giá model phân biệt class theo threshold.
* **Log Loss (Cross-entropy)** – đánh giá xác suất dự đoán.

### 3.2. Regression

* **MAE** (Mean Absolute Error)
* **MSE / RMSE** (sensitive to outliers)
* **R² score** – tỉ lệ phương sai được giải thích
* **Adjusted R²** – điều chỉnh khi có nhiều feature

### 3.3. Deep Learning-specific

* **Training loss vs Validation loss** gap để phát hiện overfitting.
* **Early stopping** dựa trên validation metric.

---

## 4. Các lỗi thường gặp khi đánh giá

* **Dùng metric sai** cho problem (ví dụ dùng accuracy với dữ liệu lệch lớp).
* **Data leakage**: scaling trước split, target encoding trên toàn bộ dataset, rò rỉ thông tin từ tương lai (time series).
* **Dùng test set để tune** hyperparameter → đánh giá ảo.
* **Đánh giá một lần duy nhất** thay vì dùng cross-validation khi dataset nhỏ.

---

## 5. Cross‑validation & workflow đánh giá

* **K-Fold / Stratified K-Fold**: đánh giá ổn định hơn so với single hold-out.
* **TimeSeriesSplit**: bắt buộc cho dữ liệu theo thời gian (không shuffle).
* **Repeated CV**: tăng độ tin cậy của ước lượng.
* Luôn thực hiện preprocessing (scaling, encoding, imputation) **inside pipeline** để tránh leakage.

---

## 6. Đánh giá trong môi trường thực tế

* **Imbalanced data**: dùng PR-AUC, F1, hoặc cost-sensitive metrics.
* **Cost-aware evaluation**: khi FP/FN có chi phí khác nhau, cân nhắc expected cost.
* **Stability under seeds / data drift**: kiểm tra biến động performance khi thay đổi random seed hoặc khi dữ liệu mới xuất hiện.
* **Monitoring** sau deploy: drift detection, periodic re-evaluation.

---

## 7. Khi nào coi một mô hình là “tốt”?

* Metric phù hợp đạt ngưỡng nghiệp vụ (business requirement).
* Gap train–validation nhỏ (không overfit).
* Ổn định trên cross-validation.
* Thông số hoạt động tốt trên test set (không bị tune bằng test).
* Hoạt động tốt trong điều kiện thực tế (robustness, latency, resource).

---

## 8. Ví dụ ngắn (case study)

Bài toán phân loại nhị phân với dữ liệu mất cân bằng:

* Không dùng accuracy.
* Dùng Precision–Recall AUC và F1-score; theo dõi confusion matrix để hiểu trade-off.
* Áp dụng Stratified K-Fold + pipeline (imputation → encoding → scaling → model).
* Dùng early stopping + calibrate threshold theo business cost.

---

## 9. Tóm tắt / Checklist

* Tách dữ liệu sạch (train/val/test) hoặc dùng CV đúng cách.
* Chọn metric phù hợp với business goal.
* Đặt pipeline để tránh data leakage.
* Dùng CV để ước lượng độ tin cậy.
* Ít nhất có một lần đánh giá trên test set cuối cùng.
* Giám sát performance sau deploy.