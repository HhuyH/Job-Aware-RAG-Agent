---
title: "MRO"
description: "Tổng quan về MRO. Code mẫu ví dụ chức năng"
tags: ["OOP", "MRO"]
---

# Method Resolution Order (MRO) và `super()` trong Python

## 1. MRO là gì?
**MRO (Method Resolution Order)** là thứ tự Python dùng để tìm thuộc tính hoặc phương thức khi bạn gọi nó trên một đối tượng.

Python áp dụng thuật toán **C3 linearization**, đảm bảo thứ tự tìm kiếm:
- Dễ dự đoán
- Không gây vòng lặp
- Không mâu thuẫn trong multiple inheritance

Bạn có thể xem MRO bằng:
```python
ClassName.mro()
# hoặc
ClassName.__mro__
```

---

## 2. Ví dụ về multiple inheritance
```python
class A:
    def show(self):
        print("A.show")

class B(A):
    def show(self):
        print("B.show")

class C(A):
    def show(self):
        print("C.show")

class D(B, C):
    pass

d = D()
d.show()
print(D.mro())
```

### Kết quả
```
B.show
[<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
```

---

## 3. Tại sao cần MRO?
MRO giúp Python:
- Quyết định gọi phương thức của class nào trước
- Giải quyết xung đột khi nhiều class cha có cùng phương thức
- Tránh diamond problem gây rối loạn thứ tự kế thừa

---

## 4. `super()` hoạt động như thế nào?
`super()` **không** gọi trực tiếp đến class cha.

Nó gọi **class tiếp theo trong MRO**, theo thứ tự C3.

```python
class A:
    def process(self):
        print("A")

class B(A):
    def process(self):
        print("B")
        super().process()

class C(A):
    def process(self):
        print("C")
        super().process()

class D(B, C):
    def process(self):
        print("D")
        super().process()

D().process()
```

### Thứ tự gọi thực tế
```
D
B
C
A
```

Không phải D → B → A như nhiều người tưởng → đây là MRO.

---

## 5. Tóm tắt nguyên tắc MRO
1. Duyệt từ trái sang phải trong khai báo kế thừa
2. Ưu tiên class hiện tại trước class cha
3. Không vi phạm thứ tự kế thừa đã tuyên bố
4. Bảo đảm không xung đột thứ tự giữa các lớp cha

---

## 6. Khi nào nên dùng `super()`?
- Khi dùng multiple inheritance
- Khi muốn tránh gọi nhầm class cha
- Khi muốn bảo toàn thứ tự đúng theo MRO
- Khi mở rộng chức năng nhưng vẫn muốn chạy logic lớp cha

Ví dụ đúng chuẩn:
```python
class X:
    def run(self):
        print("X.run")

class Y(X):
    def run(self):
        print("Y.run")
        super().run()
```

---

## 7. Khi nào không nên dùng `super()`?
- Khi không dùng kế thừa đa lớp và cần gọi cụ thể class cha
- Khi cần logic tùy chỉnh không phụ thuộc MRO

Ví dụ gọi trực tiếp:
```python
A.process(self)
```

---

## 8. Kết luận
- MRO là nền tảng để Python xử lý kế thừa đa lớp.
- `super()` dựa trên MRO, không phải cha trực tiếp.
- Hiểu MRO giúp tránh lỗi khó debug và viết code OOP Python chuyên nghiệp hơn.