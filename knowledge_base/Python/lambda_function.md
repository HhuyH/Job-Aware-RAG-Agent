---
title: "Lambda Function"
description: "Tổng quan về Lambda Function."
tags: ["Python", "Lambda Function"]
---

# **Lambda Function**

## 1. **Khái niệm**

* `lambda` là **anonymous function** (hàm không tên).
* Dùng cho các tác vụ **ngắn, đơn giản**, truyền vào các hàm bậc cao (`map`, `filter`, `sorted`…).
* Cú pháp:

```python
lambda args: expression
```

* Chỉ chứa **một biểu thức**, **không có câu lệnh** (no statements).

---

## 2. **Ví dụ cơ bản**

```python
add = lambda x, y: x + y
square = lambda x: x * x
```

---

## 3. **Dùng trong các hàm built-in**

### `map`

```python
result = list(map(lambda x: x*2, [1,2,3]))

# Kết quả
[2, 4, 6]
```

### `filter`

```python
evens = list(filter(lambda x: x % 2 == 0, [1,2,3,4]))

# Kết quả
[2, 4]
```

### `sorted` với key

```python
students = [("A", 3), ("B", 1), ("C", 2)]
sorted_students = sorted(students, key=lambda x: x[1])

# Két quả
[('B', 1), ('C', 2), ('A', 3)]
```

---

## 4. **Dùng trong list comprehension**

```python
funcs = [lambda x: x+i for i in range(3)]
# Lỗi thường gặp — all lambdas capture the same i
[<function <lambda> at 0x000002ADA4601440>, <function <lambda> at 0x000002ADA4914040>, <function <lambda> at 0x000002ADA49140E0>]
```

---

## 5. **Hạn chế của lambda**

* Không được chứa nhiều dòng.
* Không có annotation (type hints).
* Khó đọc nếu lạm dụng.
* Không thể chứa câu lệnh như:

  * `return`
  * `try/except`
  * `assert`
  * `for`, `while`, `if` (dạng statement)

---

## 6. **Các lỗi phổ biến**

### Lỗi capture biến `i`

```python
funcs = [lambda x: x+i for i in range(3)]
funcs  # ra 12, không phải 10
```

### Dùng lambda ở nơi không phù hợp

* Những đoạn code dài → nên dùng `def`.

---

## 7. **So sánh với `def`**

| Tiêu chí     | lambda          | def          |
| ------------ | --------------- | ------------ |
| Tên          | Không tên       | Có tên       |
| Dòng code    | 1 dòng          | Nhiều dòng   |
| Khả năng đọc | Thấp            | Cao          |
| Use-case     | Hàm nhỏ, inline | Hàm phức tạp |

---

## 8. **Câu hỏi phỏng vấn thường gặp**

1. Khi nào nên dùng lambda thay vì `def`?
Dùng khi cần một **hàm nhỏ, đơn giản, dùng tại chỗ**, thường truyền vào các hàm bậc cao như `sorted()`, `map()`, `filter()`.
Ưu tiên khi hàm quá ngắn để đặt tên riêng là không cần thiết.

2. Tại sao lambda không dùng cho logic nhiều dòng?
Vì cú pháp Python thiết kế `lambda` chỉ được phép chứa **biểu thức đơn (single expression)**.
Nó không hỗ trợ câu lệnh nhiều dòng (như `for`, `if/else` dạng block, `try/except`). Lý do là để giữ lambda **nhẹ, gọn, dễ đọc**, tránh biến thành một dạng `def` viết tắt nhưng khó bảo trì.

3. Tại sao lambda chỉ cho phép expression, không cho phép statement?
Do lựa chọn thiết kế của Python:

* **Expression** luôn trả về một giá trị → phù hợp cho hàm ẩn danh.
* **Statement** có tác dụng phụ, nhiều dòng, khó đọc → đi ngược triết lý của lambda là “hàm nhỏ, thuần biểu thức”.
  Python muốn tránh việc lạm dụng lambda để nhét logic phức tạp.

4. Giải thích việc lambda capture biến `i` trong vòng for.
Lambda trong Python dùng **late binding**: biến được bắt (captured) theo **giá trị tại thời điểm lambda được gọi**, không phải thời điểm nó được tạo.

Ví dụ lỗi kinh điển:
```python
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])  
# -> [2, 2, 2]
```

Tất cả lambda đều tham chiếu **cùng một biến `i`**, và khi vòng for kết thúc, `i = 2`.

Muốn đúng phải dùng default argument:

```python
funcs = [lambda i=i: i for i in range(3)]
```

5. `lambda` có tạo closure không?
**Có.**
Lambda hoạt động giống hệt hàm định nghĩa bằng `def`:

* Có lexical scope
* Có thể capture biến bên ngoài
* Có thể tạo closure

Điểm khác biệt chỉ là cú pháp, không phải cơ chế.


6. Sự khác nhau giữa:

```python
key=lambda x: x[1]
```

và viết một hàm thường?

Không có khác biệt về bản chất — **cả hai đều tạo ra một hàm**.
Khác nhau nằm ở tính thực dụng:

* `lambda`: ngắn gọn, dùng tại chỗ, không cần đặt tên.
* `def`: rõ ràng hơn khi logic phức tạp, dễ debug, dễ tái sử dụng, có docstring.

`def` tốt hơn khi hàm dài; `lambda` tốt hơn khi hàm rất ngắn.

7. Ưu – nhược điểm của lambda trong Python.

#### **Ưu điểm**

* Ngắn gọn, tiện dùng inline.
* Dễ kết hợp với hàm bậc cao (`map`, `sorted`, `filter`).
* Không cần đặt tên → code gãy gọn hơn.

#### **Nhược điểm**

* Chỉ hỗ trợ single expression → không dùng cho logic phức tạp.
* Khó debug, không có docstring.
* Dễ gây khó đọc khi lạm dụng.
* Dính lỗi **late binding** trong vòng lặp nếu không cẩn thận.

---

## 9. **Code minh họa**

```python
# lambda function trong Python là một hàm nhỏ ẩn danh được định nghĩa bằng từ khóa lambda.
square = lambda x: x**2
print(square(5))  # 25

# Dùng khi cần hàm ngắn, truyền vào hàm khác (map/filter/sort...).

# ----- Hàm map(func, iterable) -----
# Áp dụng func cho từng phần tử
map(lambda x: x**2, [1,2,3])

# ----- Hàm filter(func, iterable) -----
# Lọc phần tử thỏa func(x)==True
filter(lambda x: x>2, [1,2,3,4])

# ----- Hàm reduce(func, iterable) -----
from functools import reduce

# Gộp dần 2 phần tử lại → 1 kết quả
reduce(lambda a,b: a+b, [1,2,3])

# ----- Bài tập -----
# Dùng map để bình phương list [1,2,3,4].
print(list(map(lambda x: x**2, [1,2,3,4])))
# Kết quả
[1, 4, 9, 16]

# Dùng filter để lọc số chẵn.
print(list(filter(lambda x: x%2==0, [1,2,3,4,5,6])))
# Kết quả
[2, 4, 6]

# Dùng reduce để tính tích của list [1,2,3,4].
print(reduce(lambda a,b: a*b, [1,2,3,4]))
# Kết quả
24
```

---

## 10. **Ghi chú thêm**

* Lambda vẫn tuân theo lexical scope như các hàm bình thường.
* Không mang lại hiệu năng tốt hơn `def`; chỉ giúp code ngắn gọn.
