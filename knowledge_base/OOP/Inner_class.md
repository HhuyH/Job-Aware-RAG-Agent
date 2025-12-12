---
title: "Inner Class"
description: "Tổng quan về Inner Class. Code mẫu ví dụ chức năng"
tags: ["OOP", "Inner Class"]
---

# Inner Class (Lớp bên trong) trong Python

## 1. Khái niệm
**Inner Class** là lớp được định nghĩa *bên trong* một lớp khác. Mục đích:
- Nhóm các lớp chỉ dùng trong phạm vi một lớp lớn hơn.
- Tổ chức mã rõ ràng, tránh để những class không cần thiết xuất hiện ở phạm vi toàn cục.
- Cho phép lớp bên trong truy cập lớp bên ngoài (nếu được truyền tham chiếu).

---

## 2. Ví dụ cơ bản về Inner Class

```python
class Outer:
    def __init__(self):
        self.name = "Outer Class"

    class Inner:
        def __init__(self):
            self.name = "Inner Class"

        def display(self):
            print("This is the inner class")

# Sử dụng
outer = Outer()
print(outer.name)

inner = outer.Inner()
inner.display()
```

---

## 3. Inner Class KHÔNG tự truy cập được Outer Class
Inner class không thể tự truy cập thuộc tính của Outer class.

Sai lầm phổ biến: nghĩ rằng Inner có thể gọi trực tiếp biến của Outer.

---

## 4. Truyền tham chiếu Outer vào Inner để truy cập dữ liệu
```python
class Outer:
    def __init__(self):
        self.name = "Emil"

    class Inner:
        def __init__(self, outer):  # nhận outer instance
            self.outer = outer

        def display(self):
            print(f"Outer class name: {self.outer.name}")

# Sử dụng
outer = Outer()
inner = outer.Inner(outer)
inner.display()
```

---

## 5. Khi nào nên dùng Inner Class?
- Khi lớp bên trong chỉ có ý nghĩa trong phạm vi lớp bên ngoài.
- Khi muốn đóng gói logic liên quan giúp code gọn và dễ kiểm soát.
- Khi muốn mô phỏng cấu trúc giống Java nhưng linh hoạt theo Python.

---
