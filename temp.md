Dưới đây là **đáp án chuẩn, súc tích, rõ ràng**, đúng trọng tâm phỏng vấn về **Encapsulation trong Python**:

---

## **1. Encapsulation là gì?**

* **Khái niệm:**
  Kỹ thuật **ẩn dữ liệu bên trong class** và cung cấp **giao diện truy cập an toàn** (getter/setter hoặc method).
* **Mục đích:**

  * Bảo vệ dữ liệu khỏi thay đổi ngoài ý muốn.
  * Kiểm soát quyền truy cập và logic validate.
  * Giảm rủi ro lỗi khi code bên ngoài tương tác với class.

---

## **2. Private và Protected trong Python khác gì Java/C++?**

| Modifier  | Python                                                                | Java/C++                                                  |
| --------- | --------------------------------------------------------------------- | --------------------------------------------------------- |
| Protected | `_var` (convention) – vẫn truy cập được bên ngoài                     | `protected` – chỉ truy cập trong class và subclass        |
| Private   | `__var` (name-mangling) – khó truy cập từ bên ngoài nhưng vẫn có cách | `private` – hoàn toàn không truy cập được bên ngoài class |

**Lưu ý Python:**

* Không có cơ chế thật sự ngăn cấm; chỉ là **quy ước và name-mangling**.

---

## **3. Name-mangling hoạt động thế nào?**

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

---

## **4. Khi nào dùng getter/setter?**

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

---

## **5. Encapsulation liên quan gì với abstraction?**

* **Encapsulation**: Ẩn **dữ liệu** (how stored/managed).
* **Abstraction**: Ẩn **chi tiết cài đặt/logic**, expose **giao diện** (what class làm).

**Tóm lại:**

* Encapsulation giúp abstraction hoạt động hiệu quả hơn:

  * Dữ liệu được bảo vệ,
  * Người dùng chỉ nhìn thấy interface mà không biết chi tiết bên trong.

---

Nếu bạn muốn, mình có thể tạo **file `encapsulation.md`** tổng hợp tất cả ý trên, kèm ví dụ minh họa, theo đúng format bạn đang dùng để ôn tập.
