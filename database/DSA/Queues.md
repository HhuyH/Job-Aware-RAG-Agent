---
title: "Queue"
description: "Tổng quan về Queue."
tags: ["DSA", "Queue"]
---

# Queue trong Python

## 1. Khái niệm

Queue (hàng đợi) là cấu trúc dữ liệu tuyến tính tuân theo nguyên tắc **FIFO – First In, First Out**. Phần tử vào trước sẽ được lấy ra trước.

Ứng dụng: hệ thống in ấn, xử lý request, BFS trong đồ thị, task scheduling…

---

## 2. Các thao tác chính

* **Enqueue**: thêm phần tử vào cuối queue.
* **Dequeue**: lấy và xoá phần tử đầu queue.
* **Peek**: xem phần tử đầu mà không xoá.
* **isEmpty**: kiểm tra queue rỗng.
* **Size**: đếm số lượng phần tử.

---

## 3. Queue bằng Python List

### Code

```python\queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

# Peek
frontElement = queue[0]
print("Peek: ", frontElement)

# Dequeue
poppedElement = queue.pop(0)
print("Dequeue: ", poppedElement)

print("Queue after Dequeue: ", queue)

# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))
```

### Output

```
Queue:  ['A', 'B', 'C']
Peek:  A
Dequeue:  A
Queue after Dequeue:  ['B', 'C']
isEmpty:  False
Size:  2
```

---

## 4. Queue bằng Class (List implementation)

### Code

```python
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

myQueue = Queue()
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", myQueue.queue)
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", myQueue.queue)
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())
```

### Output

```
Queue:  ['A', 'B', 'C']
Peek:  A
Dequeue:  A
Queue after Dequeue:  ['B', 'C']
isEmpty:  False
Size:  2
```

---

## 5. Queue bằng Linked List

### Code

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()

myQueue = Queue()
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", end="")
myQueue.printQueue()
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", end="")
myQueue.printQueue()
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())
```

### Output

```
Queue: A -> B -> C -> 
Peek:  A
Dequeue:  A
Queue after Dequeue: B -> C -> 
isEmpty:  False
Size:  2
```

---

## 6. Ưu – Nhược điểm Linked List Queue

### Ưu điểm

* Kích thước động, không bị giới hạn như mảng.
* Không cần dịch chuyển phần tử khi dequeue.

### Nhược điểm

* Tốn thêm bộ nhớ cho con trỏ.
* Mã dài, phức tạp hơn list.

---

## Kết luận

Queue là cấu trúc dữ liệu nền tảng, đơn giản nhưng cực kỳ quan trọng, đặc biệ
