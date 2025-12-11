---
title: "Tuple"
description: "Tổng quan về Tuple."
tags: ["Python", "Tuple"]
---

# **Unpacking — Ghi chú nhanh & Câu hỏi phỏng vấn**

## 1. **Khái niệm**

* Unpacking là quá trình **giải nén** các phần tử từ list, tuple, hoặc dictionary và gán vào từng biến riêng.
* Dùng `*` và `**` để “mở rộng” cấu trúc dữ liệu khi:

  * gán biến,
  * truyền tham số,
  * hợp nhất/ghép list hoặc dict.

---

## 2. **Unpacking cơ bản**

### List / Tuple

```python
a, b, c = [1, 2, 3]
```

### Dư phần tử → dùng `*`

```python
a, *b = [10, 20, 30, 40]
print(a)  # 10
print(b)  # [20, 30, 40]
```

### Lấy cuối danh sách

```python
*head, tail = [1, 2, 3, 4]
# head = [1, 2, 3], tail = 4
```

---

## 3. **Unpacking khi truyền tham số**

### Dùng `*` để mở list/tuple

```python
nums = [1, 2, 3]
print(*nums)    # 1 2 3
```

### Dùng `**` để mở dict

```python
info = {"name": "Alice", "age": 25}

def show(name, age):
    print(name, age)

show(**info)  # Alice 25
```

---

## 4. **Unpacking trong cấu trúc dữ liệu**

### Ghép list nhanh

```python
a = [1, 2]
b = [3, 4]
c = [*a, *b]      # [1, 2, 3, 4]
```

### Ghép dict

```python
d1 = {"a": 1}
d2 = {"b": 2}
merged = {**d1, **d2}   # {'a': 1, 'b': 2}
```

---

## 5. **Quy tắc quan trọng**

* Mỗi assignment chỉ được dùng **tối đa 1 dấu `*`**.
* `*` luôn trả về **list**.
* `**` chỉ dùng cho dictionary có key dạng chuỗi hợp lệ với tên tham số.

---

## 6. **Use-case thực tế**

* Tách tham số đầu/cuối của list.
* Tạo function wrapper, forward tham số:

```python
def wrapper(*args, **kwargs):
    return target(*args, **kwargs)
```

* Nối dữ liệu nhanh trong ETL.
* Chuyển list/dict thành tham số cho function bất kỳ.

---

## 7. **Lỗi phổ biến**

### Unpack sai số phần tử

```python
a, b = [1, 2, 3]  # lỗi: quá nhiều giá trị
```

### Dùng `**` cho dữ liệu không phải dict

```python
show(**[1,2])     # lỗi
```

### Key dict không hợp lệ với tên tham số

```python
show(**{"name": "A", "Age": 10})  # lỗi vì ‘Age’ != ‘age’
```

---

## 8. **Câu hỏi phỏng vấn thường gặp**

1. Sự khác nhau giữa `*args` và unpacking bằng `*`?

**`*args` trong định nghĩa hàm**

* Thu gom **mọi positional arguments** còn lại thành một **tuple**.
* Chỉ xuất hiện trong *function signature*.

**Unpacking bằng `*` khi gọi hàm hoặc khi gán**

* Trải phẳng (unpack) **một iterable** thành từng phần tử riêng lẻ.
* Dùng ở cả **function call**, **assignment**, **list literal**, **tuple literal**,…

**Tóm lại:**

* `*args` = gom vào
* `*` unpacking = trải ra

2. Tại sao assignment chỉ được chứa một dấu `*`?

Vì Python phải phân giải **rõ ràng số phần tử còn lại** trong phép gán.
Ví dụ:

```python
a, *b, c = iterable
```

Python biết:

* `a` nhận phần tử đầu
* `c` nhận phần tử cuối
* `b` nhận toàn bộ phần dư

**Nếu có nhiều dấu `*`**, Python sẽ không thể xác định phần dư thuộc về biến nào ⇒ **cú pháp nhập nhằng** ⇒ bị cấm.

3. Tại sao `**` chỉ dùng được với dict?
Vì `**` yêu cầu đối số phải:

* có **key-value**
* key phải là **string** hợp lệ để dùng làm keyword argument

Keyword argument của Python là dạng:

```python
func(a=1, b=2)
```

→ Chỉ có **dict** (hoặc dict-like mapping) cung cấp cấu trúc này.
Iterable bình thường (list, tuple) **không có key**, nên không thể dùng `**`.

4. Khi nào nên dùng unpacking thay vì truyền list/dict nguyên khối?
Dùng unpacking khi:
* Hàm **expect positional arguments** hoặc **keyword arguments** riêng lẻ
* Bạn đang có dữ liệu dạng list/tuple/dict và muốn truyền **tự động** từng phần

Ví dụ điển hình:

```python
def add(a, b, c):
    ...

nums = [1, 2, 3]
add(*nums)     # đúng → truyền 3 tham số
add(nums)      # sai → truyền 1 tham số
```

**Unpacking** giúp:
* gọn
* rõ ràng
* tránh code thủ công tách phần tử

5. Có thể unpack generator không?
**Có**, vì generator là iterable:

```python
gen = (x for x in range(3))
print(*gen)  
# Kết quả: 0 1 2
```

Lưu ý:

* Generator **bị tiêu thụ** sau khi unpack
* Unpacking **về list/tuple** có thể tốn bộ nhớ nếu generator lớn

6. Sự khác nhau giữa `*` trong định nghĩa hàm và `*` khi gọi hàm?
### **Trong định nghĩa hàm (`def`)**
`*` dùng để:
* thu gom positional args → `*args`
* hoặc đánh dấu bắt đầu của **keyword-only arguments**

Ví dụ:
```python
def func(a, b, *, c, d):
    ...
```

### **Khi gọi hàm**
`*` dùng để:

* unpack một iterable thành từng positional argument

```python
func(*[1, 2], c=3, d=4)
```

## **Tóm tắt nhanh (câu trả lời ngắn cho phỏng vấn)**

* `*args` thu gom, còn `*` unpack.
* Assignment chỉ có 1 dấu `*` để tránh nhập nhằng.
* `**` chỉ dùng cho dict vì keyword arguments cần key-value.
* Unpacking nên dùng khi dữ liệu dạng iterable/mapping cần tách ra truyền.
* Generator unpack được vì nó là iterable.
* `*` trong định nghĩa hàm dùng để gom args hoặc tạo keyword-only args; khi gọi hàm dùng để trải iterable.

---

## 9. **Code minh họa**

### Tách đầu – giữa – cuối

```python
first, *middle, last = [1, 2, 3, 4, 5]
```

### Forward toàn bộ tham số

```python
def log_and_run(func, *args, **kwargs):
    print("Run:", func.__name__)
    return func(*args, **kwargs)
```

### Unpack dict vào class constructor

```python
params = {"x": 1, "y": 2}
p = Point(**params)
```

---

## 10. **Ghi chú thêm**

* Unpacking xuất hiện nhiều trong:

  * decorators,
  * function forwarding,
  * pipeline xử lý dữ liệu,
  * merge dữ liệu động,
  * lập trình functional.

---

Nếu bạn muốn, mình có thể làm tiếp cho:
**tuple / list comprehension / generators / decorators / exception / class / OOP / module / file I/O** …
Chỉ cần nói tên mục tiếp theo.
