---
title: "Args And Kwargs"
description: "Tổng quan về Args And Kwargs."
tags: ["Python", "Args And Kwargs"]
---

# **args_kwargs.md**

## 1. Tóm tắt khái niệm (Definition)

`*args` và `**kwargs` là cơ chế nhận **số lượng tham số linh hoạt** trong Python.

* `*args` nhận các tham số **không có tên** → dạng tuple.
* `**kwargs` nhận các tham số **có tên** → dạng dict.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Viết hàm có số lượng đầu vào không cố định.
* Tạo API/hàm linh hoạt trong thư viện.
* Khi viết decorator cần “ôm” cả positional + keyword args.
* Khi xây wrapper cho model, training loop, logging.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* Dấu `*` trước biến → Python **unpack positional arguments** vào tuple.
* Dấu `**` trước biến → Python **unpack keyword arguments** vào dictionary.
* Khi gọi hàm, Python gom toàn bộ cách truyền tham số vào hai biến đó nếu hàm có khai báo.

Thứ tự bắt buộc trong định nghĩa hàm:

```
def func(positional, *args, keyword_only, **kwargs):
```

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

```
def function_name(*args, **kwargs):
    ...
```

Gọi hàm:

```
function_name(1, 2, 3, a=10, b=20)
```

---

## 5. Ví dụ code (Code Examples)

```python
def demo(*args, **kwargs):
    print("args:", args)      # dạng tuple
    print("kwargs:", kwargs)  # dạng dict

demo(10, 20, "hello", name="Huy", x=1, y=2)
```

Kết quả:

```
args: (10, 20, 'hello')
kwargs: {'name': Huy, 'x': 1, 'y': 2}
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* **Đặt `*args` sau `**kwargs`** → sai cú pháp.
* Nhầm rằng `args` là list (thực ra là tuple).
* Không biết rằng khi unpack list/dict → phải dùng `*` hoặc `**`.
* Ghi sai thứ tự tham số trong hàm (positional → args → keyword-only → kwargs).

---

## 7. So sánh với khái niệm liên quan (Comparison)

| Khái niệm          | Kiểu dữ liệu     | Khi nào dùng                       |
| ------------------ | ---------------- | ---------------------------------- |
| `*args`            | tuple            | Nhiều positional args              |
| `**kwargs`         | dict             | Nhiều keyword args                 |
| unpacking `*list`  | list → elements  | Khi truyền list thành từng tham số |
| unpacking `**dict` | dict → key=value | Khi truyền dict thành keyword args |

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Viết decorator cho logging hoặc timing trong ML pipeline.
* Xây dựng trainer model có thể nhận nhiều tham số tùy ý.
* Dùng trong API wrappers, để không cần liệt kê toàn bộ tham số.
* Dùng trong class để override hàm nhưng vẫn giữ khả năng linh hoạt.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

* Sự khác nhau giữa `*args` và `**kwargs`?
* Tại sao decorator gần như luôn dùng `*args` và `**kwargs`?
* Khi nào nên dùng `*args` thay vì list?
* Trình bày thứ tự tham số hợp lệ trong hàm Python.
* Giải thích cơ chế unpacking với ví dụ.

---

## 10. TL;DR (Short Summary)

* `*args` → gom positional args vào tuple.
* `**kwargs` → gom keyword args vào dict.
* Rất quan trọng trong decorator, wrapper, API.
* Thứ tự tham số phải đúng.
* Dễ kết hợp với unpacking khi truyền đối số.

---

## Một số ví dụ khác
# Hàm dùng *args để tính tổng của mọi tham số.
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))

```
10
```

# Dùng **kwargs để in từng cặp key: value.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

```
name: Huy
age: 21
city: 
```