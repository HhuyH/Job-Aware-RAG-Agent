---
title: "Linked Lists"
description: "Tổng quan về Linked Lists."
tags: ["DSA", "Linked Lists"]
---
# Linked Lists

## 1. Khái niệm cơ bản

Danh sách liên kết (Linked List) là cấu trúc dữ liệu tuyến tính gồm các **nút (Node)**. Mỗi nút chứa:

* **data** – giá trị
* **next** – con trỏ đến nút tiếp theo

Khác với mảng (array):

* Các phần tử **không cần nằm liền kề nhau trong bộ nhớ**.
* Kích thước **linh hoạt**, có thể tăng/giảm tùy ý.
* Thao tác thêm/xóa **không cần dịch chuyển các phần tử khác**.

Các thao tác thường gặp:

* Traversal (duyệt)
* Insert
* Remove
* Sort

---

## 2. Traversal — Duyệt danh sách liên kết

Duyệt từ `head` → đi theo `.next` đến khi gặp `None`.

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)
```

---

## 3. Tìm giá trị nhỏ nhất trong Linked List

Giống tìm min trong array nhưng phải đi theo các `.next`.

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def findLowestValue(head):
  minValue = head.data
  currentNode = head.next
  while currentNode:
    if currentNode.data < minValue:
      minValue = currentNode.data
    currentNode = currentNode.next
  return minValue

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("The lowest value in the linked list is:", findLowestValue(node1))
```

---

## 4. Xóa một nút trong Linked List

Cần cập nhật con trỏ `.next` của nút đứng trước.

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def deleteSpecificNode(head, nodeToDelete):
  if head == nodeToDelete:
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:
    currentNode = currentNode.next

  if currentNode.next is None:
    return head

  currentNode.next = currentNode.next.next
  return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseAndPrint(node1)

node1 = deleteSpecificNode(node1, node4)

print("\nAfter deletion:")
traverseAndPrint(node1)
```

---

## 5. Ghi chú quan trọng

### Ưu điểm:

* Kích thước động
* Không cần dịch chuyển khi thêm/xóa
* Phù hợp cho queue/stack cỡ lớn hoặc thao tác chèn nhiều

### Nhược điểm:

* Truy cập phần tử theo index **O(n)**
* Tốn thêm bộ nhớ cho con trỏ `next`
* Khó debug và kém trực quan hơn array

Nếu muốn thêm: **Doubly Linked List, Circular Linked List, insertion, sorting**, tôi có thể mở rộng ngay.
