---
title: "Data Cleaning"
description: "Các kỹ thuật làm sạch dữ liệu trong Machine Learning."
tags: ["Preprocessing", "Data Cleaning", "Machine Learning"]
---

# Data Cleaning

Làm sạch dữ liệu là bước đầu tiên và quan trọng nhất trong quy trình Machine Learning. Mục tiêu là đảm bảo dữ liệu nhất quán, hợp lệ và có chất lượng đủ tốt để mô hình học được quy luật đúng.

---

## 1. Loại bỏ dữ liệu trùng lặp (Remove Duplicates)

### Khi nào cần?
- Khi dữ liệu thu thập từ nhiều nguồn khác nhau.
- Khi quá trình crawl hoặc merge gây ra bản ghi lặp.

### Cách xử lý:
- Xác định bản ghi trùng theo **toàn bộ cột** hoặc **một tập tiêu chí**.
- Giữ bản ghi đầu tiên hoặc bản ghi mới nhất tùy mục đích.

### Ví dụ (Pandas):
```python
df = df.drop_duplicates()
````

---

## 2. Xử lý dữ liệu không nhất quán (Inconsistency Handling)

### Dấu hiệu inconsistency:

* Giá trị cùng nghĩa nhưng được ghi khác nhau:
  `"USA"`, `"U.S.A"`, `"United States"`.
* Kiểu dữ liệu không đồng nhất:
  `"25"` (string) và `25` (int).
* Format ngày tháng không thống nhất:
  `"2024-01-01"` vs `"01/01/2024"`.

### Cách xử lý:

* Chuẩn hóa text (lowercase, strip, xóa ký tự thừa).
* Chuẩn hóa đơn vị đo (kg ↔ g, cm ↔ m).
* Map các giá trị tương đương về một chuẩn.
* Convert kiểu dữ liệu về dạng thống nhất.

### Ví dụ:

```python
df["country"] = df["country"].str.lower().str.strip()
df["date"] = pd.to_datetime(df["date"])
```

---

## 3. Phát hiện giá trị không hợp lệ (Invalid Values)

### Dấu hiệu invalid:

* Giá trị không thể xảy ra:
  `age = -5`, `score = 9999`.
* Giá trị vượt range hợp lý:
  `temperature > 60°C` đối với dữ liệu thời tiết VN.
* Giá trị sai định dạng:
  `"abc"` trong cột số.

### Kỹ thuật phát hiện:

* Kiểm tra điều kiện logic (rule-based).
* Kiểm tra range (min/max).
* Phân phối thống kê (z-score).
* Dùng mô hình anomaly detection khi cần.

### Hướng xử lý:

* Loại bỏ bản ghi vi phạm nặng.
* Sửa bằng rule (ví dụ: âm → abs).
* Gắn missing rồi xử lý ở bước imputation.

### Ví dụ:

```python
df = df[df["age"].between(0, 120)]
df["income"] = pd.to_numeric(df["income"], errors="coerce")
```

---

## Tóm tắt

| Vấn đề         | Mục tiêu           | Kỹ thuật                         |
| -------------- | ------------------ | -------------------------------- |
| Duplicates     | Loại bỏ bản ghi dư | `drop_duplicates()`              |
| Inconsistency  | Chuẩn hóa dữ liệu  | lowercase, strip, unify format   |
| Invalid values | Giữ dữ liệu hợp lệ | rule-based, range check, anomaly |

---

Data Cleaning là bước nền tảng trước khi thực hiện encoding, scaling, feature engineering hoặc training mô hình.


