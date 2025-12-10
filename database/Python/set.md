# **Set — Ghi chú nhanh & Câu hỏi phỏng vấn**

## 1. **Khái niệm**

* `set` là **tập hợp không có thứ tự**, **không chứa phần tử trùng lặp**.
* Dựa trên **hash table**, thao tác tìm kiếm/thêm/xóa trung bình O(1).
* Dùng khi cần kiểm tra tồn tại nhanh hoặc loại bỏ trùng lặp.
* Sets được sử dụng để lưu trữ nhiều phần tử trong một biến duy nhất.
* Sets là một tập hợp không được sắp xếp, không thể thay đổi* và không được lập chỉ mục.

---

## 2. **Khởi tạo**

```python
# Sets được viết bằng dấu ngoặc nhọn.
thisset = {"apple", "banana", "cherry"}

# Sets cũng có thể được viết bằng cách sử dụng 2 dấu (())
thisset = set(("apple", "banana", "cherry"))

# Sets khổng thể Các mục thiết lập không được sắp xếp, không thể thay đổi và không cho phép giá trị trùng lặp.
thisset = {"apple", "banana", "cherry", True, 1, 2} # True và 1 được coi là cùng một giá trị trong một tập hợp và chỉ xuất hiện một lần

# tương tự với false và 0
# thisset = {"apple", "banana", "cherry", False, 0, 2}

```

---

## 3. **Các thao tác cơ bản**

### Truy cập phần tử trong set

```python
# Không thể truy cập các mục trong một tập hợp bằng cách tham chiếu đến key hoặc index.

# Nhưng có thể lặp qua các phần tử trong một tập hợp, ví dụ như sử dụng vòng lặp for:
for x in thisset:
  print(x)
```

### Kiểm tra giá trị có trong set hay không
```python
print("banana" not in thisset) # kiểm tra xem "banana" không có trong set ở đay trả về giá trị boolean False
```

### Thêm giá trị

```python
# Thêm phần tử vào set trong Python
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
# Kết quả
{'cherry', 'orange', 'banana', 'apple'}

# Thêm nhiều phần tử vào set bằng phương thức update()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
# Kết quả
{'cherry', 'apple', 'pineapple', 'mango', 'papaya', 'banana'}

# Update không nhất thiết phải là một set, nó có thể là bất kỳ iterable nào như list, tuple, v.v.
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
# Kết quả
{'cherry', 'kiwi', 'orange', 'apple', 'banana'}
```

### Xóa giá trị

```python
thisset = {"apple", "banana", "cherry"}

# Nếu phần tử để xóa không tồn tại sẽ báo lỗi
thisset.remove("kiwi")
# Kết quả
# thisset.remove("kiwi")
#     ~~~~~~~~~~~~~~^^^^^^^^
# KeyError: 'kiwi'

# Nếu phần tử để xóa không tồn tại sẽ không báo lỗi
thisset.discard("banana")
# Kết quả
{'apple', 'cherry'}

# Vẫn có thể dùng pop() để xóa phần tử ngẫu nhiên trong set
x = thisset.pop()
print(x)
print(thisset)
# Kết quả
apple
{'cherry'}

# Clear và del giống với các kiểu dữ liệu khác
# Xóa toàn bộ set
del thisset 
# Kết quả
Báo lỗi vì thisset không còn tồn tại nữa

# Xóa tất cả phần tử trong list nhưng vẫn giữ list tồn tại
thisset.clear() 
[]
```

### Gộp, giao, hiệu

```python
a = {1, 2, 3}
b = {3, 4, 5}

a | b      # union -> {1,2,3,4,5}
a & b      # intersection -> {3}
a - b      # difference -> {1,2}
a ^ b      # symmetric difference -> {1,2,4,5}
```

---

## 4. **Đặc điểm quan trọng**

* Phần tử trong set **phải hashable**, tức **immutable**:

  * Hợp lệ: int, float, str, tuple chứa kiểu hashable.
  * Không hợp lệ: list, dict, set.

```python
{ [1,2] }  # lỗi
{ (1,2) }  # OK
```

* Không đảm bảo thứ tự → không index.

---

## 5. **Use-case thực tế**

* Loại bỏ trùng lặp:

```python
unique = list(set(my_list))
```

* Kiểm tra tồn tại cực nhanh:

```python
if x in my_set:
    ...
```

* Tìm phần tử chung giữa 2 danh sách:

```python
common = set(list1) & set(list2)
```

---

## 6. **Điểm mạnh – điểm yếu**

### Điểm mạnh

* Tốc độ tìm kiếm / membership O(1).
* Loại bỏ trùng lặp tự nhiên.
* Thao tác tập hợp mạnh mẽ.

### Điểm yếu

* Không giữ thứ tự.
* Chỉ lưu được phần tử hashable.
* Không dùng để truy cập theo index.

---

## 7. **Lỗi phổ biến**

### Dùng `{}` để tạo set rỗng

```python
s = {}       # → dict
```

### Thêm phần tử không hashable

```python
s.add([1,2]) # lỗi
```

### Mong đợi thứ tự ổn định

```python
list(set([3,1,2]))  # thứ tự không đảm bảo
```

---

## 8. **Câu hỏi phỏng vấn thường gặp**

1. Vì sao set không giữ thứ tự?

Set được cài đặt bằng **hash table**. Hash table tổ chức phần tử theo **hash value**, không theo vị trí tuyến tính.
Python chỉ cần đảm bảo **không trùng lặp**, **tra cứu nhanh**, nên việc giữ thứ tự không phải mục tiêu thiết kế ban đầu.
*(Lưu ý: từ Python 3.7+, dict giữ thứ tự, nhưng set thì không. Đây là hai cấu trúc khác nhau.)*

2. Vì sao phần tử của set phải là hashable?

Vì set dùng hash table để:

* kiểm tra trùng lặp
* tra cứu xem phần tử có tồn tại hay không

Mỗi phần tử phải có:

* **hash value cố định** (immutable)
* **hàm `__hash__()`** và **`__eq__()`** hoạt động ổn định

Nếu phần tử thay đổi giá trị sau khi thêm vào, hash table sẽ hỏng.

3. Sự khác nhau giữa `remove()` và `discard()`?

| Hàm          | Nếu phần tử không tồn tại | Nếu tồn tại |
| ------------ | ------------------------- | ----------- |
| `remove(x)`  | **Raise KeyError**        | Xóa phần tử |
| `discard(x)` | **Không lỗi**, làm gì cả  | Xóa phần tử |

Khi không chắc phần tử có tồn tại, dùng `discard()` an toàn hơn.

4. Vì sao `set` có complexity trung bình O(1)?

Do hash table:

* Hash phần tử → lấy index trong bucket → truy cập trực tiếp
* Không phải duyệt tuần tự như list

Trung bình O(1), nhưng **worst-case** có thể O(n) nếu hash collisions nặng.

5. Khi nào dùng set thay vì list?

Dùng set khi ưu tiên:

* **Loại bỏ trùng lặp**
* **Tra cứu có/không có** nhanh (membership test)
* **So sánh tập hợp** (intersection, union, difference)

Không dùng set khi:

* Cần giữ **thứ tự**
* Cần **phần tử trùng lặp**
* Cần **indexing**

6. Sự khác nhau giữa `set` và `frozenset`?

| Thuộc tính        | `set`                 | `frozenset`                                     |
| ----------------- | --------------------- | ----------------------------------------------- |
| Mutable           | ✔️                    | ❌                                             |
| Hashable          | ❌                    | ✔️ (dùng làm key của dict hoặc phần tử của set)|
| Thao tác thay đổi | add/remove            | Không thể thay đổi                              |
| Dùng khi          | cần tập hợp linh hoạt | cần tập hợp bất biến, an toàn, hashable         |

7. Tại sao `{}` không tạo ra set rỗng?

Vì Python giữ lại cú pháp `{}` để tạo **dict rỗng** — dạng literal cơ bản của dictionary.
Muốn tạo set rỗng phải dùng:

```python
set()
```

Lý do: dict được dùng phổ biến hơn set, nên cú pháp `{}` ưu tiên cho dict để tránh mô hồ và giữ tính nhất quán.

---

## 9. **Code minh họa**

```python
# Lọc qua list
# Chỉ có thể loop qua set bằng vòng for và không làm gì khác được
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Lọc trùng trong list
def unique_items(items):
    return list(set(items))

# Tìm phần tử xuất hiện ở cả hai danh sách
def overlap(a, b):
    return set(a) & set(b)

# Dùng set để tối ưu tìm kiếm
seen = set()
for value in data:
    if value in seen:
        print("duplicate:", value)
    seen.add(value)
```

# Nối set
```python
# Có một số cách để nối hai hoặc nhiều tập hợp trong Python.
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
# Kết quả: {1, 2, 3, 4, 5}

# Phương thức union() và update() nối tất cả các phần tử từ cả hai tập hợp.
a = {1, 2, 3}
b = {3, 4, 5}

a.update(b)
print(a)
# Kết quả: {1, 2, 3, 4, 5}

# Phương thức intersection() CHỈ giữ lại các phần tử trùng lặp.
a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a.intersection(b))
# Kết quả: {3, 4}

# Phương thức difference() giữ lại các phần tử từ tập hợp đầu tiên không có trong set(s) tập hợp khác.
a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a.difference(b))
# Kết quả: {1, 2}

# Phương thức symmetric_difference() giữ lại tất cả các phần tử NGOẠI TRỪ các phần tử trùng lặp.
a = {1, 2, 3}
b = {3, 4, 5}

print(a.symmetric_difference(b))
# Kết quả: {1, 2, 4, 5}

```

# Union set
```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) # cũng có thể dùng | để nối 2 set với nhau để có kết quả tương tự như union(): set3 = set1 | set2

print(set3)
# Kết quả: {'a', 'b', 'c', 1, 2, 3}

# cũng có thể join nhiều set với nhau

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4) # hoặc myset = set1 | set2 | set3 |set4
print(myset)
# Kết quả: {'a', 'b', 'c', 1, 2, 3, 'John', 'Elena', 'apple', 'bananas', 'cherry'}

# cũng có thể join set với list hoặc tuple bằng union() hoặc |
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z) #kết quả trả về vẫn là một set
# Kết quả: {'a', 'b', 'c', 1, 2, 3}

```
# Update set
```python
# Phương thức update() chèn tất cả các phần tử từ một tập hợp vào một tập hợp khác.
# Phương thức update() thay đổi tập hợp ban đầu và không trả về một tập hợp mới.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) # Kết quả: {1, 'a', 2, 3, 'c', 'b'}

```

# Intersection set
```python
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# Phương thức intersection() sẽ trả về một tập hợp mới, chỉ chứa các mục có trong cả hai tập hợp.

set3 = set1.intersection(set2) # cũng có thể dùng & để lấy giao của 2 set sẽ có kết quả tương tự
print(set3) # Kết quả: {'apple'}

# tuy nhiên "&" chỉ có thể cho bạn join 2 sets có cũng loại data types không như khi bạn dùng intersection()

#Phương thức intersection_update() cũng CHỈ giữ lại các phần tử trùng lặp, nhưng nó sẽ thay đổi tập hợp gốc thay vì trả về một tập hợp mới.

set1.intersection_update(set2)
print(set1) # Kết quả: {'apple'}

```

# Difference Set
```python
#Phương thức difference() sẽ trả về một tập hợp mới chỉ chứa các mục từ tập hợp đầu tiên không có trong tập hợp kia.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2) # cũng có thể dùng "-" để lấy hiệu của 2 set sẽ có kết quả tương tự
print(set3) # Kết quả: {'banana', 'cherry'}

# Phương thức difference_update() cũng sẽ giữ lại các mục từ tập đầu tiên không có trong tập khác, nhưng nó sẽ thay đổi tập ban đầu thay vì trả về một tập mới.
set1.difference_update(set2)
print(set1) # Kết quả: {'cherry', 'banana'}

# Phương thức symmetric_difference() sẽ chỉ giữ lại những phần tử KHÔNG có trong cả hai tập hợp.
set3 = set1.symmetric_difference(set2) # cũng có thể dùng "^" để lấy hiệu đối xứng của 2 set sẽ có kết quả tương tự
print(set3) # Kết quả: {'microsoft', 'cherry', 'banana', 'google'}

# Phương thức symmetric_difference_update() cũng sẽ giữ lại tất cả các phần tử trừ phần tử trùng lặp, nhưng nó sẽ thay đổi tập hợp gốc thay vì trả về một tập hợp mới.
set1.symmetric_difference_update(set2)
print(set1) # Kết quả: {'cherry', 'microsoft', 'banana', 'google'}
```
# Frozenset Set
```python
# Giống như sets, frozenset chứa các phần tử duy nhất, không có thứ tự và không thể thay đổi.
# Không giống như sets, các phần tử không thể được thêm hoặc bớt khỏi frozenset.

# dùng frozenset() để tạo frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x) # Kết quả: frozenset({'cherry', 'banana', 'apple'})
print(type(x)) # Kết quả: <class 'frozenset'>
```

---

## 10. **Ghi chú thêm**

* `frozenset` là phiên bản immutable của set → dùng làm key trong dict.
* Set không hỗ trợ indexing, slicing, hay sort trực tiếp.
