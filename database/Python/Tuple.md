---
title: "Tuple"
description: "Tổng quan về Tuple."
tags: ["Python", "Tuple"]
---

# **Tuple — Ghi chú nhanh & Câu hỏi phỏng vấn**

## 1. **Khái niệm**

* Tuple dùng để lưu trữ nhiều phần tử trong **một biến duy nhất**.
* Là một trong 4 cấu trúc dữ liệu tích hợp của Python: **List, Tuple, Set, Dict**.
* Đặc điểm:

  * **Có thứ tự (ordered)**
  * **Không thể thay đổi (immutable)**
  * Viết bằng **dấu ngoặc tròn** `()`

```python
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
```

---

## 2. **Tuple với một phần tử**

* Phải có **dấu phẩy** để Python hiểu đó là tuple.

```python
thistuple = ("apple",)
print(type(thistuple))   # tuple

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))   # str
```

---

## 3. **Truy cập phần tử**

Hoạt động giống `list`:

```python
t = ("apple", "banana", "cherry")
print(t[0])     # apple
print(t[-1])    # cherry
```

---

## 4. **Tuple là immutable → muốn update phải convert sang list**

```python
x = ("apple", "banana", "cherry")

y = list(x)
y[1] = "kiwi"

x = tuple(y)
print(x)
```

---

## 5. **Thêm phần tử vào tuple**

### Cách 1: Chuyển sang list

```python
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
```

### Cách 2: Nối tuple

```python
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
```

---

## 6. **Xóa phần tử**

### Chuyển sang list rồi xóa

```python
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
```

### Xóa toàn bộ tuple

```python
del thistuple
# print(thistuple)  # lỗi: biến không còn tồn tại
```

---

## 7. **Tuple unpacking**

### Unpacking cơ bản

```python
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
```

### Unpacking với `*`

```python
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
print(red)    # ['cherry', 'strawberry', 'raspberry']

(green, *tropic, red) = fruits
print(tropic) # ['banana', 'cherry', 'strawberry']
```

---

## 8. **Loop qua tuple**

### Cơ bản

```python
for x in ("apple", "banana", "cherry"):
    print(x)
```

### Duyệt bằng index

```python
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
```

### Dùng while

```python
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1
```

---

## 9. **Join / Merge tuple**

```python
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
```

---

## 10. **Nhân tuple**

```python
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)  # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
```

---

## 11. **Các method hữu ích**

| Method         | Mô tả                                 |
| -------------- | ------------------------------------- |
| `count(value)` | Số lần phần tử xuất hiện              |
| `index(value)` | Vị trí xuất hiện đầu tiên của phần tử |

---

## 12. **Use-case thực tế**

* Dùng làm dữ liệu **bất biến** (immutable) trong hệ thống.
* Lưu các giá trị **cấu hình**, **tọa độ**, **RGB**, **record cố định**.
* Dùng trong **unpacking nhiều giá trị trả về**:

```python
def get_user():
    return ("Huy", 22)

name, age = get_user()
```

---

## 13. **Câu hỏi phỏng vấn thường gặp**

1. Tại sao tuple lại immutable? Lợi ích?

**Lý do:**

* Tuple được thiết kế để lưu **dữ liệu cố định**, không thay đổi trong suốt vòng đời.
* Python tối ưu tuple cho **tốc độ**, **bộ nhớ**, và **hashability**.

**Lợi ích:**

* **Nhanh hơn** list (do cấu trúc cố định, dễ tối ưu nội bộ).
* **Tiết kiệm bộ nhớ** hơn list.
* **Hashable**, dùng được làm key trong dict hoặc phần tử của set.
* **An toàn logic**: tránh thay đổi dữ liệu ngoài ý muốn.

2. Khác biệt giữa list và tuple ở:
   * tốc độ,
   * bộ nhớ,
   * cách dùng?

### **Tốc độ**

* **Tuple nhanh hơn** khi:

  * duyệt
  * truy cập phần tử
  * tạo object
* Do không cần quản lý cơ chế thay đổi kích thước như list.

### **Bộ nhớ**

* **Tuple dùng ít bộ nhớ hơn** list.
* List phải duy trì **con trỏ động** để mở rộng — tốn bộ nhớ hơn.

### **Cách dùng**

* **List**:

  * dữ liệu thay đổi
  * cần thêm/xóa/sửa
  * cấu trúc động, linh hoạt

* **Tuple**:

  * dữ liệu cố định
  * dùng làm key của dict
  * dữ liệu bất biến, an toàn chia sẻ giữa các hàm

3. Khi nào nên dùng tuple thay vì list?

Dùng tuple khi:

* Dữ liệu **không thay đổi** (immutable data).
* Cần **hiệu năng tốt** hơn.
* Muốn đảm bảo data **không bị sửa nhầm**.
* Làm **key của dict** hoặc phần tử set.
* Trả nhiều giá trị từ hàm (tuple unpacking tự nhiên hơn).
* Cần **struct-like**, “record” nhẹ mà không cần class.

4. Tại sao tuple hashable còn list thì không?

**Hash yêu cầu object phải immutable**.

* Tuple **không thay đổi** → hash cố định → an toàn làm key.
* List **thay đổi được** → hash sẽ không ổn định → không thể dùng làm key.

**Nguyên tắc:**
Hash của object mà có thể thay đổi ⇒ phá vỡ cấu trúc của hash table ⇒ Python cấm.

5. Giải thích tuple unpacking với `*`.

Ở assignment, dấu `*` cho phép “thu phần còn lại”:

```python
a, *b, c = (1, 2, 3, 4, 5)
```

Kết quả:

```python
a = 1
b = [2, 3, 4]
c = 5
```

* `*b` luôn trở thành **list**, dù unpack từ tuple.
* Chỉ được phép dùng **một** dấu `*` để tránh nhập nhằng.

6. Có thể chứa list bên trong tuple không? Nếu có thì thay đổi được không?

**Có thể**, vì tuple chỉ yêu cầu bản thân nó immutable,
**nhưng phần tử bên trong có thể mutable**.

Ví dụ:

```python
t = (1, 2, [3, 4])
t[2][0] = 99
print(t)
```

Kết quả:

```
(1, 2, [99, 4])
```

**Giải thích:**

* Tuple immutable **theo cấu trúc** (không thêm/xóa/thay phần tử).
* Nhưng nếu phần tử bên trong là mutable (list), ta vẫn có thể sửa nội dung list.

**Lưu ý:**

* Nếu tuple chứa list → tuple **không còn hashable**.

---

Nếu muốn, mình có thể làm tiếp cho:
**list comprehension / generator / exception / OOP / decorator / module / file I/O / class / dataclass**…
Chỉ cần nói mục tiếp theo.
