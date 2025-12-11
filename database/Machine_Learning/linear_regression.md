---

title: "Linear Regression"
description: "Thuật toán Linear Regression trong Machine Learning (Regressor & Classifier)."
tags: ["Machine Learning", "Linear Regression"]
---

# Linear Regression

## 1. Khái niệm

Linear Regression là thuật toán thuộc nhóm **Supervised Learning**, dùng để mô hình hóa mối quan hệ tuyến tính giữa **feature** và **output**. Đây là thuật toán nền tảng nhất trong hồi quy.

Mục tiêu: tìm đường thẳng (hoặc siêu phẳng) tối ưu mô tả dữ liệu.

---

## 2. Công thức tổng quát
$$
y = w_1 x_1 + w_2 x_2 + \dots + w_n x_n + b
$$


Trong đó:

* ( w ): trọng số
* ( b ): bias
* ( y ): giá trị dự đoán

---

## 3. Loss Function

Thuật toán tối ưu hóa dựa trên:

### **MSE – Mean Squared Error**
$$
\text{MSE} = \frac{1}{N} \sum_{i=1}^{N} (y_{true}^{(i)} - y_{pred}^{(i)})^2
$$

---

## 4. Linear Regression dùng để làm gì?

### **Regression (chuẩn)**

Dự đoán giá trị liên tục:

* Giá nhà
* Lương
* Nhiệt độ
* Doanh thu

### **Classification (biến thể: Linear Regression Classifier – KHÔNG khuyến nghị)**

Có thể dùng linear regression để phân loại nhị phân bằng cách:

1. Fit mô hình như bài toán regression
2. Lấy ngưỡng (threshold) để phân loại, ví dụ: ( $$
y > 0.5 \Rightarrow 1
$$
 ), ngược lại 0.

Tuy nhiên:

* Không ổn định
* Không tối ưu cho classification
* Dễ bị outlier làm méo

→ Thực tế dùng **Logistic Regression** cho classification.

---

## 5. Linear Regression có những loại nào?

### **1. Simple Linear Regression**

1 feature duy nhất.

### **2. Multiple Linear Regression**

Nhiều feature.

### **3. Regularized Regression** (ổn định hơn)

* **Ridge Regression (L2)**
* **Lasso Regression (L1)**
* **ElasticNet (L1 + L2)**

---

## 6. Ưu điểm

* Dễ hiểu, đơn giản.
* Tốc độ rất nhanh, huấn luyện nhẹ.
* Dễ diễn giải trọng số feature.
* Hiệu quả khi dữ liệu gần tuyến tính.

---

## 7. Nhược điểm

* Không xử lý dữ liệu phi tuyến.
* Rất nhạy với outlier.
* Giả định phân phối phần dư (residual) phải chuẩn.
* Không phù hợp cho classification.

---

## 8. Khi nào nên dùng Linear Regression?

Dùng khi:

* Dữ liệu có xu hướng tuyến tính.
* Cần mô hình giải thích được.
* Không cần mô hình phức tạp.

Không dùng khi:

* Nhiều outlier.
* Dữ liệu phi tuyến.
* Bài toán classification.

---

## 9. Metric đánh giá

### Regression

* MSE
* RMSE
* MAE
* R² score

### Classification (nếu dùng dạng classifier – KHÔNG khuyến nghị)

* Accuracy
* Precision / Recall
* F1-score

---

## 10. Cách trả lời phỏng vấn (chốt gọn)

* Linear Regression là thuật toán mô hình hóa quan hệ tuyến tính giữa input và output.
* Dùng MSE để tối ưu hóa.
* Dùng tốt cho regression; không phù hợp cho classification.
* Có các biến thể Ridge, Lasso, ElasticNet để xử lý overfitting và multicollinearity.
