---
title: "Lists Arrays"
description: "Tổng quan về Lists Arrays."
tags: ["DSA", "Lists Arrays"]
---

# Lists và Arrays trong Python

## 1. Khởi tạo list

```python
# Empty list
x = []

# List with initial values
y = [1, 2, 3, 4, 5]

# List with mixed types
z = [1, "hello", 3.14, True]
```

---

## 2. Thao tác cơ bản với list

```python
x = [9, 12, 7, 4, 11]

# Thêm phần tử mới
x.append(8)

# Sắp xếp tăng dần
x.sort()
```

**Kết quả:**

```
[4, 7, 8, 9, 11, 12]
```

---

## 3. Thuật toán cơ bản trên list – tìm giá trị nhỏ nhất

```python
my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

for i in my_array:
    if i < minVal:
        minVal = i

print('Lowest value:', minVal)
```

**Output:**

```
Lowest value: 4
```

Thuật toán này duyệt toàn bộ list → độ phức tạp **O(n)**.

---

## 4. Ghi chú về hiệu năng

* Với dữ liệu nhỏ: duyệt tuyến tính hoàn toàn ổn.
* Với dữ liệu lớn: cần xem xét tối ưu hóa hoặc sử dụng cấu trúc dữ liệu nhanh hơn.
* Python đã có hàm tích hợp `min()` tối ưu nội bộ.

```python
min(my_array)
```

---

## 5. Lists vs Arrays

* **List**: linh hoạt, chứa nhiều kiểu, sử dụng phổ biến.
* **Array (module array)**: tối ưu cho một kiểu dữ liệu duy nhất.
* **NumPy Array**: mạnh mẽ, dùng trong ML và xử lý tính toán lớn.