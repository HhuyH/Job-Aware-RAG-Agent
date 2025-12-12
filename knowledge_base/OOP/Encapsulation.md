---
title: "Encapsulation"
description: "Tổng quan về Encapsulation. Code mẫu ví dụ chức năng"
tags: ["OOP", "Encapsulation"]
---

## encapsulation.md

````md
# Encapsulation trong Python OOP

## 1. Khái niệm
Encapsulation là kỹ thuật:
- Đóng gói dữ liệu và hành vi vào cùng một lớp.
- Kiểm soát truy cập vào dữ liệu nhằm bảo vệ tính toàn vẹn.
- Ẩn chi tiết nội bộ, chỉ cung cấp các phương thức cần thiết ra bên ngoài.

Trong Python:
- Mặc định mọi thuộc tính đều public.
- Quy ước:
  - `_variable` → protected (không nên truy cập trực tiếp).
  - `__variable` → private (được name-mangling).

---

## 2. Public / Protected / Private

### Public
```python
class Person:
    def __init__(self, name, age):
        self.name = name        # Public
        self.__age = age        # Private
````

`self.name` truy cập bình thường.
`self.__age` không thể truy cập trực tiếp từ bên ngoài.

---

## 3. Private Attribute + Getter/Setter

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

p = Person("Tobias", 25)
p.set_age(30)
print(p.get_age())
```

---

## 4. Ví dụ encapsulation thực tế

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")

    def get_grade(self):
        return self.__grade

    def get_status(self):
        return "Passed" if self.__grade >= 60 else "Failed"
```

Ý nghĩa:

* Kiểm soát giá trị hợp lệ (0–100).
* Bảo vệ tính toàn vẹn dữ liệu.
* Logic nội bộ (tính passed/failed) được giấu kín.

---

## 5. Protected attribute (`_variable`)

Python không enforced mức bảo vệ này. Đây chỉ là quy ước:

```python
class Person:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary   # Protected (chỉ nên dùng nội bộ)
```

---

## 6. Private method

```python
class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        return isinstance(num, (int, float))

    def add(self, num):
        if self.__validate(num):
            self.result += num
```

---

## 7. Name Mangling trong Python

Khi dùng `__variable`, Python đổi tên thành:

```
__age → _Person__age
```

→ Giúp tránh ghi đè vô tình khi kế thừa.
Không nhằm mục đích bảo mật tuyệt đối, chỉ để bảo vệ nội bộ.

---

## 8. Lợi ích của Encapsulation

1. Bảo vệ dữ liệu khỏi truy cập sai.
2. Kiểm soát quyền đọc/ghi dữ liệu.
3. Giấu chi tiết nội bộ.
4. Dễ bảo trì và mở rộng.
5. Dữ liệu được xác thực trước khi thay đổi.
6. Tăng tính nhất quán và toàn vẹn của hệ thống.

---

## 9. Câu hỏi phỏng vấn liên quan

1. Encapsulation là gì?

* **Khái niệm:**
  Kỹ thuật **ẩn dữ liệu bên trong class** và cung cấp **giao diện truy cập an toàn** (getter/setter hoặc method).
* **Mục đích:**

  * Bảo vệ dữ liệu khỏi thay đổi ngoài ý muốn.
  * Kiểm soát quyền truy cập và logic validate.
  * Giảm rủi ro lỗi khi code bên ngoài tương tác với class.

2. Private và protected trong Python khác gì Java/C++?

| Modifier  | Python                                                                | Java/C++                                                  |
| --------- | --------------------------------------------------------------------- | --------------------------------------------------------- |
| Protected | `_var` (convention) – vẫn truy cập được bên ngoài                     | `protected` – chỉ truy cập trong class và subclass        |
| Private   | `__var` (name-mangling) – khó truy cập từ bên ngoài nhưng vẫn có cách | `private` – hoàn toàn không truy cập được bên ngoài class |

**Lưu ý Python:**

* Không có cơ chế thật sự ngăn cấm; chỉ là **quy ước và name-mangling**.

3. Name-mangling hoạt động thế nào?

* Khi khai báo biến `__var` trong class, Python **tự động đổi tên thành `_ClassName__var`** để tránh xung đột tên subclass hoặc truy cập ngoài.
* Ví dụ:

```python
class A:
    def __init__(self):
        self.__x = 10

a = A()
print(a._A__x)  # 10
```

* Thực chất biến vẫn **truy cập được**, nhưng “khó vô tình dùng”.

4. Khi nào dùng getter/setter?

* Khi muốn **kiểm soát việc đọc/ghi dữ liệu** (validate input, tính toán giá trị, logging…).
* Khi muốn **ẩn attribute**, nhưng vẫn expose API an toàn cho người dùng class.
* Khi cần **tương thích với abstraction**, để thay đổi cài đặt bên trong mà không phá vỡ code bên ngoài.

```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, r):
        if r > 0:
            self.__radius = r
        else:
            raise ValueError("Radius must be positive")
```

5. Encapsulation liên quan gì với abstraction?

* **Encapsulation**: Ẩn **dữ liệu** (how stored/managed).
* **Abstraction**: Ẩn **chi tiết cài đặt/logic**, expose **giao diện** (what class làm).

**Tóm lại:**

* Encapsulation giúp abstraction hoạt động hiệu quả hơn:

  * Dữ liệu được bảo vệ,
  * Người dùng chỉ nhìn thấy interface mà không biết chi tiết bên trong.


```

