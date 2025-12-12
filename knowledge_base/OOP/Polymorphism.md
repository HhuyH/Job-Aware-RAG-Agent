---
title: "Polymorphism"
description: "Tổng quan về Polymorphism. Code mẫu ví dụ chức năng"
tags: ["OOP", "Polymorphism"]
---

# Polymorphism trong Python

## Khái niệm
Polymorphism (đa hình) là khả năng các đối tượng thuộc những lớp khác nhau có thể phản hồi cùng một lời gọi phương thức bằng các hành vi khác nhau. Điều này giúp mã linh hoạt, mở rộng dễ dàng và giảm sự phụ thuộc vào kiểu đối tượng.

## Mục tiêu
- Cùng tên phương thức → nhiều hành vi khác nhau.
- Hỗ trợ lập trình theo giao diện/hợp đồng hành vi.
- Giảm trùng lặp, tăng tính mở rộng.

---

## Ví dụ không sử dụng đa hình
Trong trường hợp này, các lớp độc lập và đều có phương thức `move()`, nhưng không có chung kế thừa, khiến việc duyệt qua các đối tượng thiếu cấu trúc.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")
```

### Kết quả chạy:
```python
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()
```
**Output:**
```
Drive!
Sail!
Fly!
```

---

## Ví dụ sử dụng đa hình qua kế thừa
Tạo lớp cha `Vehicle` và để các lớp con override phương thức `move()`.

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")
```

### Kết quả chạy:
```python
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
```

**Output:**
```
Ford
Mustang
Move!
Ibiza
Touring 20
Sail!
Boeing
747
Fly!
```
---

## Ghi chú quan trọng
- Python hỗ trợ **duck typing**, nên đa hình không nhất thiết phải dựa trên kế thừa.
- Bất kỳ đối tượng nào có cùng tên phương thức cũng có thể được xử lý giống nhau.

Ví dụ:
```python
def start(obj):
    obj.move()
```
Miễn là đối tượng có `move()`, hàm sẽ hoạt động.

---

## **⚠️ Phân loại đa hình trong Python**

Trong lý thuyết OOP có hai dạng đa hình:

1. **Compile-time polymorphism (Method Overloading)**

   * Python **không hỗ trợ thật sự** vì hàm định nghĩa sau sẽ *ghi đè hoàn toàn* hàm trước.
   * Vì vậy Python giải quyết bằng **default parameters**, `*args`, `**kwargs` thay cho overloading.

2. **Runtime polymorphism (Method Overriding)**

   * Python **có hỗ trợ** thông qua kế thừa.
   * Lớp con định nghĩa lại (override) phương thức của lớp cha → hành vi khác nhau tại runtime.

---

## **⚠️ Ví dụ ngắn nhất về Method Overriding**

```python
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

for a in (Dog(), Cat()):
    print(a.sound())   # Bark, Meow
```

---

## Kết luận
Polymorphism giúp code rõ ràng, mở rộng dễ dàng và hạn chế phụ thuộc vào kiểu của đối tượng. Đây là nền tảng quan trọng trong OOP và trong thiết kế hệ thống linh hoạt.
