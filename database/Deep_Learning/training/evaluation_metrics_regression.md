---
title: Regression Evaluation Metrics in Deep Learning
description: Ghi chú về các metric đánh giá mô hình regression trong deep learning, công thức, ý nghĩa và cách áp dụng.
tags: [Deep Learning, Training, Evaluation, Regression, Metrics]
---

## 1. Tóm tắt khái niệm (Definition)

Các metric đánh giá regression đo lường mức độ gần đúng giữa giá trị dự đoán và giá trị thực tế, giúp cải thiện mô hình.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Đánh giá hiệu suất mô hình regression.
* So sánh các thuật toán và hyperparameter.
* Lựa chọn model tốt nhất cho deployment.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* Dựa trên sai số giữa giá trị dự đoán $\hat{y}$ và giá trị thực $y$.
* Các metric phổ biến:

  * Mean Squared Error (MSE):
    $$
    MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
    $$
  * Root Mean Squared Error (RMSE):
    $$
    RMSE = \sqrt{MSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
    $$
  * Mean Absolute Error (MAE):
    $$
    MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
    $$
  * R-squared ($R^2$):
    $$
    R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}*i)^2}{\sum*{i=1}^{n} (y_i - \bar{y})^2}
    $$
* Lựa chọn metric dựa trên mục tiêu và sensitivity của mô hình với outlier.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

* Input: predicted values $\hat{y}$ và true values $y$.
* Output: MSE, RMSE, MAE, R-squared.
* Optional: weighted errors hoặc normalized metrics.

---

## 5. Ví dụ code (Code Examples)

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

y_true = [3.0, -0.5, 2.0, 7.0]
y_pred = [2.5, 0.0, 2.1, 7.8]

mse = mean_squared_error(y_true, y_pred)
rmse = mean_squared_error(y_true, y_pred, squared=False)
mae = mean_absolute_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)

print(f"MSE: {mse}, RMSE: {rmse}, MAE: {mae}, R2: {r2}")
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Chọn metric không phù hợp với outlier (ví dụ MSE nhạy với outlier).
* Không chuẩn hóa dữ liệu → metric không phản ánh đúng hiệu suất.
* Không tính R-squared cho multi-output regression.

---

## 7. So sánh với khái niệm liên quan (Comparison)

* MSE vs MAE:

  * MSE: nhạy với outlier, phạt sai số lớn.
  * MAE: ít nhạy với outlier, dễ hiểu.
* RMSE vs MSE: cùng thông tin nhưng RMSE cùng đơn vị với y.
* R-squared: đo mức độ giải thích biến thiên dữ liệu, giá trị 1 là tốt nhất.

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Dự báo tài chính, thời tiết, giá nhà: chọn metric phù hợp với outlier.
* Tuning hyperparameters dựa trên MSE/MAE.
* So sánh nhiều mô hình regression để chọn best model.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Các metric đánh giá regression phổ biến là gì?
* Khi nào nên dùng MAE thay vì MSE?
* R-squared tính ra sao và ý nghĩa?
* RMSE khác MSE thế nào?

---

## 10. TL;DR (Short Summary)

* Các metric: MSE, RMSE, MAE, R-squared.
* MSE nhạy với outlier, MAE bền hơn.
* RMSE cùng đơn vị với target, dễ interpret.
* Chọn metric phù hợp với
