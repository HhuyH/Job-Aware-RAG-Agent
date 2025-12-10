---
title: "Abstraction"
description: "Tổng quan về Abstraction. Code mẫu ví dụ chức năng"
tags: ["OOP", "Abstraction"]
---

## abstraction.md

````md
# Abstraction trong Python OOP

## 1. Khái niệm
- Abstraction là **che giấu sự phức tạp**, chỉ giữ lại **những gì cần thiết**.
- Một abstract class mô tả **khái niệm chung**, nhưng **không chứa logic cụ thể**.
- Các lớp con buộc phải tự implement những hành vi đó.

Python hỗ trợ abstraction qua module `abc`:
```python
from abc import ABC, abstractmethod
````

---

## 2. Ví dụ chuẩn về Abstraction

```python
from abc import ABC, abstractmethod

# Abstract class
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

Ý nghĩa:

* `PaymentMethod` mô tả: “Mọi phương thức thanh toán đều phải có `pay()`”.
* Không định nghĩa cách thanh toán → đó là abstraction.

---

## 3. Class con: Credit Card

```python
class CreditCardPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Trừ {amount} bằng Credit Card...")
        print(">>> Gửi request đến ngân hàng")
        print(">>> Ngân hàng xác nhận giao dịch")
        print(">>> Thanh toán thành công!")
```

---

## 4. Class con: E-Wallet

```python
class EWalletPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Thanh toán {amount} bằng E-Wallet...")
        print(">>> Kiểm tra số dư ví")
        print(">>> Trừ tiền trong ví")
        print(">>> Giao dịch hoàn tất!")
```

---

## 5. Dùng abstraction trong thực tế

```python
def checkout(payment_method: PaymentMethod, amount):
    payment_method.pay(amount)

checkout(CreditCardPayment(), 500_000)
print("-----------------------------")
checkout(EWalletPayment(), 200_000)
```

`checkout()` **không cần biết**:

* thanh toán bằng ví hay thẻ,
* gọi API nào,
* kiểm tra số dư hay liên hệ ngân hàng.

Nó chỉ biết gọi `pay()` → đúng tinh thần abstraction.

---

## 6. Câu hỏi phỏng vấn liên quan

1. Abstraction khác Encapsulation thế nào?

| Khía cạnh      | Abstraction                                                             | Encapsulation                                                      |
| -------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Mục tiêu       | Ẩn chi tiết **cách thức hoạt động**, chỉ hiện **giao diện (interface)** | Ẩn **dữ liệu bên trong** và cung cấp **getter/setter** để truy cập |
| Cách thực hiện | Abstract class, Interface, Method abstract                              | Private/protected attributes, property, setter/getter              |
| Tập trung      | **HÀNH VI**                                                             | **DỮ LIỆU**                                                        |

2. Tại sao dùng abstract class khi có thể dùng interface?

* Abstract class có thể **chứa cả method đã triển khai lẫn abstract method**, interface chỉ định nghĩa method chưa triển khai.
* Abstract class **có constructor, biến trạng thái, logic chung** → giảm lặp code.
* Khi cần **chung tính năng + enforce contract**, abstract class linh hoạt hơn interface.

3. Khi nào nên dùng abstraction?

* Khi muốn **ẩn chi tiết cài đặt**, chỉ expose **giao diện** cho người dùng/hàm khác.
* Khi muốn **bắt buộc lớp con phải triển khai** những method nhất định.
* Khi muốn **tái sử dụng code** nhưng vẫn giữ **hợp đồng bắt buộc**.

4. Abstract class có chứa constructor không? (Có)

**Có.**

* Lớp abstract vẫn có thể khai báo `__init__()` để **khởi tạo thuộc tính chung** cho các lớp con.
* Lớp con gọi `super().__init__()` để dùng logic khởi tạo này.

5. Class con không override `@abstractmethod` thì chuyện gì xảy ra? (Không thể khởi tạo instance)

* **Không thể khởi tạo instance** của lớp con.
* Python sẽ raise **TypeError** nếu cố gắng tạo object từ class chưa triển khai tất cả abstract method.

---

## 7. Tóm tắt

* Abstract class mô tả “cái khái niệm chung”.
* Class con tự hiện thực logic.
* Phương thức abstract bắt buộc phải override.
* Giúp giấu phức tạp, giảm phụ thuộc, tăng khả năng mở rộng.

```

