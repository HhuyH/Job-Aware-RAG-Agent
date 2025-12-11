Dưới đây là **đáp án chuẩn, súc tích, rõ ràng** về **Inheritance trong Python**, đúng trọng tâm phỏng vấn:

---

## **1. Kế thừa là gì?**

* **Khái niệm:**
  Cơ chế cho phép **lớp con (child class) kế thừa thuộc tính và phương thức** của lớp cha (parent class).
* **Mục đích:**

  * **Tái sử dụng code**, tránh lặp lại.
  * **Mở rộng chức năng** mà không sửa code lớp gốc.
  * Hỗ trợ **polymorphism** và **abstraction**.

---

## **2. Sự khác nhau giữa `super()` và gọi trực tiếp `Parent.__init__()`**

| Điểm khác         | `super()`                                       | `Parent.__init__()`                    |
| ----------------- | ----------------------------------------------- | -------------------------------------- |
| Cách hoạt động    | Tìm **MRO** → gọi hàm tiếp theo trong hierarchy | Gọi trực tiếp **class cụ thể**         |
| Hỗ trợ đa kế thừa | ✔️ – tôn trọng MRO, tránh gọi trùng             | ❌ – bỏ qua MRO, dễ gọi trùng nhiều lần |
| Linh hoạt         | ✔️ – thay đổi parent class không ảnh hưởng      | ❌ – hard-code tên parent class         |

**Ví dụ:**

```python
class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        super().__init__()  # đúng chuẩn MRO
        print("B init")
```

---

## **3. Khi nào nên dùng kế thừa, khi nào không?**

* **Dùng khi:**

  * Lớp con là **một dạng của lớp cha** (“is-a” relationship).
  * Cần **tái sử dụng code** và mở rộng logic.
  * Muốn **ghi đè phương thức** (override) hoặc thêm behavior.

* **Không nên dùng khi:**

  * Không có quan hệ “is-a” → dùng **composition** tốt hơn.
  * Khi kế thừa chỉ để **tái sử dụng vài method**, dễ làm class trở nên rối và phụ thuộc mạnh.

---

## **4. Đa kế thừa trong Python hoạt động thế nào? (MRO – Method Resolution Order)**

* Python hỗ trợ **đa kế thừa**: một lớp có thể kế thừa nhiều lớp cha.

* Khi gọi method, Python dùng **MRO** để xác định thứ tự tìm method:

  1. Lớp con
  2. Lớp cha theo thứ tự khai báo
  3. Các lớp cha tiếp theo trong hierarchy
  4. `object` class (tối ưu nhất)

* Dùng `ClassName.mro()` hoặc `help(ClassName)` để xem thứ tự.

**Ví dụ:**

```python
class A:
    def hello(self): print("A")

class B(A):
    def hello(self): print("B")

class C(A):
    def hello(self): print("C")

class D(B, C):
    pass

d = D()
d.hello()  # B được gọi theo MRO: D → B → C → A → object
print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

* **Lưu ý:** MRO giúp tránh **diamond problem** (trùng lặp gọi method).

---

Nếu bạn muốn, mình có thể tạo **file `inheritance.md`** tổng hợp tất cả kiến thức, kèm ví dụ minh họa trực quan, đúng format bạn đang dùng để ôn tập phỏng vấn.
