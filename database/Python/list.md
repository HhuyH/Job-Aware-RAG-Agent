# **List**

## 1. **Khái niệm**

* `list` là cấu trúc dữ liệu **thay đổi được (mutable)**.
* Duy trì **thứ tự**.
* Có thể chứa nhiều kiểu dữ liệu khác nhau.

Ví dụ:

```python
nums = [1, 2, 3]
mixed = [1, "a", True, 3.14]
```

---

## 2. **Các thao tác cơ bản**

### Tạo list

```python
a = []
b = list()
c = [x for x in range(5)]
```

### Truy cập phần tử

```python
fruitbasket = ["apple","banana","orange","grape","mango", "kiwi", "pineapple"]

# Truy cập phần tử thứ 2 trong list (chỉ số bắt đầu từ 0)
print(fruitbasket[1]) 
# Kết quả
banana

# In toàn bộ list
print(fruitbasket)
# Kết quả
['apple', 'banana', 'orange', 'grape', 'mango', 'kiwi', 'pineapple']

# Lấy phần tử cuối trong list
print("Lấy phần tử cuối cùng trong list: ", fruitbasket[-1])  # truy cập phần tử cuối cùng trong list bằng chỉ số âm
# Kết quả
Lấy phần tử cuối cùng trong list:  pineapple

# Lấy phần từ kế cuối trong list
print("Lấy phần từ kế cuối trong list: ", fruitbasket[-2]) # truy cập phần tử kế cuối trong list bằng chỉ số âm
# Kết quả
Lấy phần từ kế cuối trong list:  kiwi
```

### Cắt (slicing)

```python
fruitbasket = ["apple","banana","orange","grape","mango", "kiwi", "pineapple"]

# Lấy 1 cụm phần từ từ index 1 - 3
print("Lấy 1 cụm phần từ từ index 1 - 3: ", fruitbasket[1:4])  # truy cập phần tử từ chỉ số 1 đến chỉ số 3 (không bao gồm chỉ số 4)
# Kết quả
Lấy 1 cụm phần từ từ index 1 - 3:  ['banana', 'orange', 'grape']

# Lấy 1 cụm phần từ từ index đầu - 3
print("Lấy 1 cụm phần từ từ index đầu - 3: ", fruitbasket[:4]) # truy cập phần tử từ đầu đến chỉ số 3 (không bao gồm chỉ số 4)
# Kết quả
Lấy 1 cụm phần từ từ index đầu - 3:  ['apple', 'banana', 'orange', 'grape']

# Lấy 1 cụm phần từ từ index 2 - cuối
print("Lấy 1 cụm phần từ từ index 2 - cuối: ", fruitbasket[2:]) # truy cập phần tử từ chỉ số 2 đến cuối list
# Kết quả
Lấy 1 cụm phần từ từ index 2 - cuối:  ['orange', 'grape', 'mango', 'kiwi', 'pineapple']

# 1 cụm phần từ từ index -4 - -1
print("Lấy 1 cụm phần từ từ index -4 - -1: ", fruitbasket[-4:-1]) # truy cập phần tử từ chỉ số -4 đến chỉ số -1 (không bao gồm chỉ số -1)
# Kết quả
Lấy 1 cụm phần từ từ index -4 - -1:  ['grape', 'mango', 'kiwi']

# Lấy toàn bộ phần từ trong list
print("Lấy toàn bộ phần từ trong list: ", fruitbasket[:]) # truy cập toàn bộ phần tử trong list
# Kết quả
Lấy toàn bộ phần từ trong list:  ['apple', 'banana', 'orange', 'grape', 'mango', 'kiwi', 'pineapple']

# Đỏa toàn bộ list
print("Đảo toàn bộ list: ", fruitbasket[::-1]) # đảo list
# Kết quả
Đảo toàn bộ list:  ['pineapple', 'kiwi', 'mango', 'grape', 'orange', 'banana', 'apple']
```

---

## 3. **Các method quan trọng**

### Thay đổi giá trị phần tử trong list

```python
fruitbasket = ["apple","banana","orange","grape","mango"]

# Thay đổi giá trị phần tử thứ 2 trong list
fruitbasket[1] = "blackcurrant" 
# Kết quả
['apple', 'blackcurrant', 'orange', 'grape', 'mango']

# Thay đổi giá trị một cụm phần tử trong list
fruitbasket[1:3] = ["blackcurrant", "watermelon"]
# Kết quả
['apple', 'blackcurrant', 'watermelon', 'grape', 'mango']

# Thay đổi 1 giá trị phần tử trong mảng bằng 2 giá trị mới (giống như là chèn thêm phần tử)
fruitbasket[1:2] = ["blackcurrant", "watermelon"]
# Kết quả
['apple', 'blackcurrant', 'watermelon', 'orange', 'grape', 'mango']

# Thay đổi một cụm phần tử trong list bằng 1 giá trị mới (tức 2 hay là 3 giá trị cũng chuyển thành giá trị mới thêm vào)
fruitbasket[1:4] = ["blackcurrant"]
# Kết quả
['apple', 'blackcurrant', 'mango']

```

### Thêm phân tử mới

```python
fruitbasket = ["apple","banana","orange","grape","mango"]

# thêm phần tử vào cuối list bằng hàm append(value)
fruitbasket.append("kiwi")
# Kết quả
['apple', 'banana', 'orange', 'grape', 'mango', 'kiwi']

# chèn thêm phần tử vào list bằng hàm insert(index, value)
fruitbasket.insert(2, "watermelon")
# Kết quả
['apple', 'banana', 'watermelon', 'orange', 'grape', 'mango']

# thêm nhiều phần tử từ 1 list khác vào cuối list bằng hàm extend(iterable)
tropical = ["mango", "pineapple", "papaya"]
fruitbasket.extend(tropical)
# Kết quả
['apple', 'banana', 'orange', 'grape', 'mango', 'mango', 'pineapple', 'papaya']

# thêm nhiều phần tử từ 1 tuple vào cuối list bằng hàm extend(iterable)
thistuple = ("kiwi", "orange")
fruitbasket.extend(thistuple)
# Kết quả
['apple', 'banana', 'orange', 'grape', 'mango', 'kiwi', 'orange']

```

### Xoá

```python
fruitbasket = ["apple","banana","orange","grape","mango"]

# Xóa phần tử "banana" khỏi list
fruitbasket.remove("banana") 
# Kết quả
['apple', 'orange', 'grape', 'mango']

# Xóa phần tử ở vị trí index 2 khỏi list
fruitbasket.pop(2) 
# Kết quả
['apple', 'banana', 'grape', 'mango']

# Xóa phần tử cuối cùng khỏi list
fruitbasket.pop() 
# Kết quả
['apple', 'banana', 'orange', 'grape']

# Xóa phần tử ở vị trí index 0 khỏi list
del fruitbasket[0]
# Kết quả
['banana', 'orange', 'grape', 'mango']

# Xóa toàn bộ list
del fruitbasket 
# Kết quả
Báo lỗi vì fruitbasket không còn tồn tại nữa

# Xóa tất cả phần tử trong list nhưng vẫn giữ list tồn tại
fruitbasket.clear() 
[]
```

### Sắp xếp

```python
sort()
sorted(a)
```

### Liên kết list

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# Tạo 1 list mới bằng cách nối 2 list với nhau
list3 = list1 + list2

# Thêm các phần tử từ list2 vào cuối list1 bằng hàm extend()
list1.extend(list2)

# Thêm các phần tử từ list2 vào cuối list1 bằng vòng for
for x in list2:
  list1.append(x)

# Kết quả
['a', 'b', 'c', 1, 2, 3]
```

### Khác

```python
index(x)
count(x)
```

# Loop quá các phần tử

```python
fruitbasket = ["apple","banana","orange","grape","mango"]

# loop qua từng phần tử trong list bằng vòng for
for fruit in fruitbasket:
    print(fruit)

# loop qua từng phần tử trong list bằng chỉ số index
for i in range(len(fruitbasket)):
    print(fruitbasket[i])

# loop qua từng phần tử trong list bằng vòng while
i = 0
while i < len(fruitbasket):
  print(fruitbasket[i])
  i = i + 1

# loop qua từng phần tử trong list bằng list comprehension
[print(x) for x in fruitbasket]
```

# Một số kỹ thuật tạo list

```python
fruitbasket = ["apple","banana","orange","grape","mango", "kiwi"]

# Dùng for loop để tạo list mới chứa các phần tử có chữ "a"
newlist = []
for fruit in fruitbasket:
    if "a" in fruit:
        newlist.append(fruit)

# Cách viết gọn hơn với list comprehension
# newlist = [x for x in fruitbasket if "a" in x] # Cú pháp list comprehension | newlist = [expression for item in iterable if condition == True]
# Kết quả
['apple', 'banana', 'orange', 'grape', 'mango']

# Tạo list mới chứa các phần tử từ fruitbasket mà không phải có "apple"
newlist = [x for x in fruitbasket if x != "apple"]
# Kết quả
['banana', 'orange', 'grape', 'mango', 'kiwi']

# Tạo list mới chứa tất cả phần tử từ fruitbasket mà ko có dieu kiện lọc
newlist = [x for x in fruitbasket]
# Kết quả
['apple', 'banana', 'orange', 'grape', 'mango', 'kiwi']

# Tạo list mới chứa các số từ 0 đến 9
newlist = [x for x in range(10)]
# Kết quả
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Tạo list mới chứa các số từ 0 đến 9 mà nhỏ hơn 5
newlist = [x for x in range(10) if x < 5]
# Kết quả
[0, 1, 2, 3, 4]

# Chuyển tất cả phần tử trong fruitbasket thành chữ in hoa vào list mới
newlist = [x.upper() for x in fruitbasket]
# Kết quả
['APPLE', 'BANANA', 'ORANGE', 'GRAPE', 'MANGO', 'KIWI']

# Tạo list mới chứa toàn chữ 'hello', số phần tử bằng với fruitbasket
newlist = ['hello' for x in fruitbasket]
# Kết quả
['hello', 'hello', 'hello', 'hello', 'hello', 'hello']

# Tạo list mới, nếu phần tử là "banana" thì thay bằng "orange", còn lại giữ nguyên
newlist = [x if x != "banana" else "orange" for x in fruitbasket]
# Kết quả
['apple', 'orange', 'orange', 'grape', 'mango', 'kiwi']
```

# Xấp sếp phần tử trong list

```python
import sys
sys.stdout.reconfigure(encoding='utf-8')

fruitbasket = ["apple","Banana","orange","Grape","mango", "Kiwi"]

# Sắp xếp phần tử trong list theo thứ tự tăng dần (A-Z)
fruitbasket.sort()
# Kết quả
['Banana', 'Grape', 'Kiwi', 'apple', 'mango', 'orange']

# Sắp xếp phần tử trong list theo thứ tự giảm dần (Z-A)
fruitbasket.sort(reverse=True)
# Kết quả
['orange', 'mango', 'apple', 'Kiwi', 'Grape', 'Banana']

# Đảo ngược thứ tự phần tử hiện tại trong list
fruitbasket.reverse()
# Kết quả
['Kiwi', 'mango', 'Grape', 'orange', 'Banana', 'apple']

# Sắp xếp phần tử trong list không phân biệt chữ hoa chữ thường
fruitbasket.sort(key = str.lower)
# Kết quả
['apple', 'Banana', 'Grape', 'Kiwi', 'mango', 'orange']


list2 = [100, 50, 65, 82, 23]

# Sắp xếp phần tử trong list theo thứ tự tăng dần (nhỏ đến lớn)
list2.sort()
# Kết quả
[23, 50, 65, 82, 100]

# Sắp xếp phần tử trong list theo thứ tự giảm dần (lớn đến nhỏ)
list2.sort(reverse=True) 
# Kết quả
[100, 82, 65, 50, 23]

# Sắp xếp phần tử trong list theo thứ tự dựa trên hàm myfunc
def myfunc(n):
  return abs(n - 50)

list2.sort(key=myfunc) 
# Kết quả
[50, 65, 23, 82, 100]
```
---

## 4. **Shallow copy vs Deep copy**

Shallow copy là gì?
Shallow copy là sao chép lớp ngoài cùng của object.
- Object mới được tạo ra
- Nhưng object con bên trong vẫn dùng chung reference

### Shallow copy

```python
fruitbasket = ["apple","banana","orange","grape","mango"]

# Copy list bằng hàm copy()
newbasket = fruitbasket.copy()

# Copy list bằng cách sử dụng hàm list()
newbasket = list(fruitbasket)

# Sao chép list bằng cách sử dụng slicing
newbasket = fruitbasket[:]
```


### Deep copy

Deep copy là gì?
Deep copy là sao chép toàn bộ object, bao gồm cả object lồng bên trong.
Tạo bản sao độc lập hoàn toàn
Không dùng chung reference

```python
import copy

fruitbasket = ["apple", "banana", ["orange", "grape"], "mango"]

newbasket = copy.deepcopy(fruitbasket)
```

### Khi nào dùng cái nào?

Dùng shallow copy khi:
- Data chỉ có 1 tầng đơn giản
- Không có list/dict/object lồng bên trong
- Muốn tiết kiệm memory và tăng tốc

Dùng deep copy khi:
- Data có nested structure (list trong list, dict trong dict…)
- Cần đảm bảo thay đổi và không ảnh hưởng bản gốc

```python
a = [1, 2, [3, 4]]

# Shallow copy
b = a.copy()

# Deep copy
c = copy.deepcopy(a)

# Thay đổi list con trong list gốc
a[2].append(5)

# Kết quả
a: [1, 2, [3, 4, 5]]
b (shallow): [1, 2, [3, 4, 5]]
c (deep): [1, 2, [3, 4]]
```

---

## 5. **List comprehension**

### Mẫu thường dùng

```python
# Nhân đôi từng phần tử
a = [1, 2, 3, 4]
result = [x * 2 for x in a]

# Kết quả
[2, 4, 6, 8]

# Lọc số chẵn
a = [1, 2, 3, 4, 5, 6]
result = [x for x in a if x % 2 == 0]

# Kết quả
[2, 4, 6]

```

### Lồng nhau

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flat = [x for row in matrix for x in row]

# Kết quả
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 6. **Các lỗi phổ biến**

* Gán list → dẫn đến shared reference:

```python
a = [1,2,3]
b = a
b.append(4)   # a cũng thay đổi
```

* Dùng `list * n` với list con:

```python
a = [[0] * 3] * 3  # tất cả hàng trỏ cùng một list
```

---

## 7. **Câu hỏi phỏng vấn thường gặp**

1. Sự khác nhau giữa `list` và `tuple`?

| Tiêu chí                | `list`   | `tuple`                      |
| ----------------------- | -------- | -----------------------------|
| Mutable (thay đổi được) | ✅ Có     | ❌ Không                   |
| Cú pháp                 | `[ ]`    | `( )`                        | 
| Performance             | Chậm hơn | Nhanh hơn                    |
| Dùng làm key dict       | ❌ Không  | ✅ Có (nếu chứa immutable) |

**Chốt phỏng vấn:**
> List mutable, tuple immutable nên tuple an toàn hơn và tối ưu hơn trong nhiều trường hợp.

2. Tại sao `list` là mutable và tuple là immutable?
Vì **thiết kế nội tại**:

* `list` cho phép thay đổi phần tử → phải quản lý bộ nhớ linh hoạt
* `tuple` được thiết kế **read-only**, không cho phép thay đổi để:

  * An toàn dữ liệu
  * Dùng làm key của dict
  * Hash được

3. `list.sort()` khác gì `sorted()`?

| `list.sort()`     | `sorted()`            |
| ----------------- | --------------------- |
| In-place          | Tạo list mới          |
| Trả về `None`     | Trả về list mới       |
| Chỉ dùng cho list | Dùng cho mọi iterable |

Ví dụ:

```python
a = [3,1,2]
a.sort()       # a bị thay đổi
b = sorted(a)  # a không đổi
```

4. Khi nào shallow copy gây bug?
Khi **object nested** (list trong list / dict trong dict).

Ví dụ bug case:

```python
a = [[1,2],[3,4]]
b = a.copy()
b[0].append(99) 
# => a cũng bị thay đổi
```

5. Tại sao `[[0]*3]*3` lại sai? Cách sửa?
Vì nó **copy cùng 1 reference** 3 lần.

Ví dụ lỗi:

```python
a = [[0]*3]*3
a[0][0] = 1
print(a)
```

Kết quả sai:

```
[[1,0,0], [1,0,0], [1,0,0]]
```

### Cách sửa đúng:

```python
a = [[0]*3 for _ in range(3)]
```

6. Big-O của:s
   * `append`
   * `insert`
   * `pop`
   * `in` (membership test)

(giữ ở mức **Python interview chuẩn**)

| Operation      | Big-O                |
| -------------- | -------------------- |
| `append()`     | **O(1)** amortized   |
| `insert(i, x)` | **O(n)**             |
| `pop()`        | **O(1)** (cuối list) |
| `pop(i)`       | **O(n)**             |
| `x in list`    | **O(n)**             |

7. Giải thích cách hoạt động của list comprehension.

Nó là **cú pháp rút gọn của for-loop**:

```python
[x*2 for x in a]
```

tương đương:

```python
for x in a:
    result.append(x*2)
```

**Điểm quan trọng để nói khi phỏng vấn:**

* Performance tốt hơn loop thường
* Code ngắn gọn, dễ đọc hơn (nếu không quá phức tạp)

8. List có dùng mảng động (dynamic array) hay linked list? Tại sao?

✅ **Dynamic array**

Python list được cài bằng **mảng động**, không phải linked list.

### Tại sao không dùng linked list?

* Linked list không hỗ trợ random access nhanh
* List cần:

  * `O(1)` access theo index
  * Cache-friendly (liền nhau trong memory)

---

## 8. **Ghi chú thêm**

* List trong Python dùng **dynamic array**.
* Tối ưu cho truy cập theo chỉ số, không tối ưu cho insert/delete giữa list.

---
