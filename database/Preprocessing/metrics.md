---
title: "Evaluation Metrics"
description: "Các chỉ số đánh giá mô hình Machine Learning cho bài toán Classification và Regression."
tags: ["Metrics", "Model Evaluation", "Machine Learning"]
---

# Evaluation Metrics

Việc đánh giá mô hình cần sử dụng các chỉ số phù hợp với loại bài toán.  
Tài liệu này tổng hợp các metric quan trọng nhất cho **Classification** và **Regression**.

---

# 1. Classification Metrics

Áp dụng cho bài toán phân loại (binary hoặc multi-class).

---

## 1.1. Accuracy

**Định nghĩa**  
Tỉ lệ dự đoán đúng trên tổng số mẫu.

\[
Accuracy = \frac{TP + TN}{TP + FP + FN + TN}
\]

**Khi dùng**  
- Khi dữ liệu cân bằng.

**Không nên dùng**  
- Khi dữ liệu lệch lớp (imbalanced).

---

## 1.2. Precision

\[
Precision = \frac{TP}{TP + FP}
\]

**Ý nghĩa:** Trong các mẫu mô hình dự đoán là *positive*, bao nhiêu mẫu là đúng?

**Khi dùng:**  
- Muốn giảm false positive (ví dụ: nhận diện spam).

---

## 1.3. Recall

\[
Recall = \frac{TP}{TP + FN}
\]

**Ý nghĩa:** Trong tất cả mẫu *positive thật*, mô hình tìm đúng bao nhiêu?

**Khi dùng:**  
- Muốn giảm false negative (ví dụ: bệnh nhân mắc bệnh không bị bỏ sót).

---

## 1.4. F1-Score

\[
F1 = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}
\]

**Ý nghĩa:** Trung hòa precision và recall.  
**Khi dùng:**  
- Dataset mất cân bằng.  
- Cần trade-off giữa precision và recall.

---

## 1.5. Confusion Matrix

Ma trận 2×2 thể hiện:
- TP: dự đoán đúng positive  
- TN: dự đoán đúng negative  
- FP: dự đoán nhầm thành positive  
- FN: bỏ sót positive  

**Dùng để:**  
- Hiểu chi tiết mô hình sai ở đâu.

---

## 1.6. ROC Curve & AUC

- ROC vẽ **TPR vs FPR** theo nhiều threshold khác nhau.  
- AUC = diện tích dưới đường ROC.  

**Ý nghĩa:**  
Khả năng phân biệt giữa positive và negative.

**Khi dùng:**  
- Binary classification  
- Dữ liệu không quá mất cân bằng.

---

## 1.7. Precision–Recall Curve & AUC

**Ý nghĩa:**  
Hữu ích khi dataset **imbalanced**.

- PR AUC nhạy hơn ROC AUC trong trường hợp positive rất ít.

---

## 1.8. Specificity

\[
Specificity = \frac{TN}{TN + FP}
\]

**Khi dùng:**  
- Trường hợp cần giảm false positive.

---

## 1.9. Log Loss

\[
LogLoss = -\frac{1}{N}\sum (y\log(p) + (1-y)\log(1-p))
\]

**Ý nghĩa:**  
Đánh giá chất lượng **xác suất dự đoán**.

**Khi dùng:**  
- Khi mô hình output **probability**.

---

---

# 2. Regression Metrics

Áp dụng cho bài toán dự đoán giá trị liên tục.

---

## 2.1. MAE — Mean Absolute Error

\[
MAE = \frac{1}{N}\sum |y - \hat{y}|
\]

**Ý nghĩa:**  
Sai số trung bình tuyệt đối.

**Ưu điểm:**  
- Dễ hiểu  
- Không bị ảnh hưởng mạnh bởi outlier như MSE

---

## 2.2. MSE — Mean Squared Error

\[
MSE = \frac{1}{N}\sum (y - \hat{y})^2
\]

**Ý nghĩa:**  
Phạt sai số lớn mạnh hơn.

---

## 2.3. RMSE — Root Mean Squared Error

\[
RMSE = \sqrt{MSE}
\]

**Ý nghĩa:**  
Sai số trung bình tính theo **đơn vị gốc của biến** → dễ diễn giải hơn MSE.

---

## 2.4. R² Score

\[
R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
\]

**Ý nghĩa:**  
Tỉ lệ biến thiên trong dữ liệu được mô hình giải thích.

- 1.0 → hoàn hảo  
- 0 → mô hình tệ như dự đoán trung bình  
- < 0 → mô hình tệ hơn baseline  

---

## 2.5. Adjusted R²

Điều chỉnh R² khi số lượng feature tăng.

\[
Adjusted\ R^2 = 1 - (1-R^2)\frac{n-1}{n-k-1}
\]

**Khi dùng:**  
- Khi so sánh mô hình với số lượng biến khác nhau.

---

## 2.6. MAPE — Mean Absolute Percentage Error

\[
MAPE = \frac{100}{N}\sum \left|\frac{y - \hat{y}}{y}\right|
\]

**Ý nghĩa:**  
Sai số trung bình dưới dạng phần trăm.

**Nhược điểm:**  
- Không dùng được khi y = 0  
- Nhạy với outlier

---

## 2.7. SMAPE — Symmetric MAPE

Khắc phục một phần điểm yếu của MAPE.

\[
SMAPE = \frac{100}{N}\sum \frac{|y-\hat{y}|}{(|y| + |\hat{y}|)/2}
\]

**Khi dùng:**  
- Time series  
- Khi cần metric ổn định hơn MAPE

---

# Recommended usage summary

| Loại | Metric khuyến nghị |
|------|--------------------|
| Classification | F1-score, ROC AUC, PR AUC |
| Regression | MAE, RMSE, R² |
