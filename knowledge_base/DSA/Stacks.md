---
title: "Stacks"
description: "Tổng quan về Stacks."
tags: ["DSA", "Stacks"]
---

# Stack (LIFO)

## 1. Khái niệm

Stack là cấu trúc dữ liệu tuân theo nguyên tắc **LIFO – Last In, First Out**: phần tử vào sau sẽ ra trước.

## 2. Các thao tác chính

* **push(x)**: Thêm phần tử vào đỉnh stack.
* **pop()**: Lấy và xóa phần tử trên cùng.
* **peek()**: Xem phần tử trên cùng.
* **isEmpty()**: Kiểm tra rỗng.
* **size()**: Trả về số lượng phần tử.

## 3. Ứng dụng

* Undo/Redo
* Backtracking
* DFS
* Kiểm tra dấu ngoặc
* Call stack khi thực thi hàm

---

## 4. Triển khai Stack bằng List

```python
stack = []
stack.append("A")  # push
stack.append("B")
stack.append("C")

stack[-1]           # peek
stack.pop()         # pop
len(stack)          # size
not stack           # isEmpty
```

### Class Stack (List)

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        return "Stack is empty" if self.isEmpty() else self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
```

### Ưu điểm / Nhược điểm

**Ưu điểm**

* Đơn giản, nhanh.
* Tối ưu bộ nhớ hơn linked list.

**Nhược điểm**

* Resize tốn chi phí.
* Không hoàn toàn động như linked list.

---

## 5. Triển khai Stack bằng Linked List

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        val = self.head.value
        self.head = self.head.next
        self.size -= 1
        return val

    def peek(self):
        return "Stack is empty" if self.isEmpty() else self.head.value

    def isEmpty(self):
        return self.size == 0
```

### Ưu điểm / Nhược điểm

**Ưu điểm**

* Kích thước động thực sự.
* push/pop luôn O(1).

**Nhược điểm**

* Tốn bộ nhớ cho con trỏ `next`.
* Code dài và phức tạp hơn.
