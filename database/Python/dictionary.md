# **dictionary.md**

## 1. Tóm tắt khái niệm (Definition)

`dict` trong Python là cấu trúc dữ liệu ánh xạ **key → value**, cho phép truy xuất nhanh theo key.
Key phải **hashable** (immutable). Value có thể là bất kỳ kiểu dữ liệu nào.

---

## 2. Mục đích & khi nào dùng (Use Cases)

* Lưu trữ dữ liệu dạng cặp key–value.
* Xây dựng bảng tra cứu nhanh (lookup table).
* Lưu cấu hình, tham số model, metadata.
* Dùng trong JSON, API, data pipelines.
* Lưu các statistics trong training ML.

---

## 3. Cách hoạt động bên trong (Internal Logic)

* Dictionary dùng **hash table**.
* Key được hash thành số → ánh xạ đến bucket → chứa value.
* Tìm kiếm, thêm, xóa thường O(1).
* Khi đầy, bảng sẽ rehash (tăng kích thước).

Key hợp lệ:

* String
* Number
* Tuple immutable
* Không dùng list hoặc dict làm key.

---

## 4. Cấu trúc / Cú pháp (Syntax / Structure)

Tạo dict:

```python
d = {"a": 1, "b": 2}
```

Thêm phần tử:

```python
d["c"] = 3
```

Truy cập:

```python
value = d.get("a", default_value)
```

Duyệt:

```python
for key, value in d.items():
    ...
```

Xóa:

```python
del d["a"]
```

---

## 5. Ví dụ code (Code Examples)

# Ví dụ cơ bản
```python
student = {
    "name": "Huy",
    "age": 22,
    "skills": ["Python", "Machine Learning"],
}

print(student["name"])
print(student.get("gpa", 4.0))

for k, v in student.items():
    print(k, ":", v)
```

```
Huy
4.0
name : Huy
age : 22
skills : ['Python', 'Machine Learning']
```
# không cho duplicate key, key trùng sẽ bị ghi đè với giá trị khai báo phia sau nó hoặc giá trị mới

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}

print(thisdict)
```

```
{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
```

# cũng có thể dùng dict() để tạo dictionary
```python
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
```

```
{'name': 'John', 'age': 36, 'country': 'Norway'}
```

# truy cập phần tử trong dictionary bằng key
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"] # hoặc dùng .get() ví dụ x = thisdict.get("model")
print(x)
```

```
Mustang
```

# lấy độ dài của dictionary
```python
print(len(thisdict))
```

# lấy tất cả key trong dictionary
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()
print(x)
```

```
dict_keys(['brand', 'model', 'year'])
```

# lấy tất cả giá trị trong dictionary thay vì lấy key
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
print(x) 
```

```
dict_values(['Ford', 'Mustang', 1964])
```

# lấy cả key và values
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# lấy tất cả cặp key:value trong dictionary
x = car.items()
print(x)
```

```
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
```

# thêm một key mới vào dictionary và xem sự thay đổi của keys
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
print(x) # Trước thay đổi

car["color"] = "white" # hoặc sử dụng car.update({"color": "white"})
print(x) # Sâu thay đổi
```

```
dict_keys(['brand', 'model', 'year'])
dict_keys(['brand', 'model', 'year', 'color'])
```

# Update giá trị
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
print(x) # Trước thay đổi

car["year"] = 2020 # Hoặc sử dụng car.update({"year": 2020})
print(x) # Sâu thay đổi
```

```
dict_values(['Ford', 'Mustang', 1964])
dict_values(['Ford', 'Mustang', 2020])
```

# Xóa phần tử
```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# xóa key:value bằng hàm pop()
car.pop("model") # Hoặc del car["model"]
```

```
{'brand': 'Ford', 'year': 1964}
```

# xóa phần tử cuối cùng được thêm vào dictionary bằng hàm popitem()
```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()
```

```
{'brand': 'Ford', 'model': 'Mustang'}
```

# xóa toàn bộ dictionary bằng từ khóa del
```python
del car 
print(car)
```
```
In ra sẽ báo lỗi vì car đã bị xóa
```

# xóa tất cả phần tử trong dictionary nhưng vẫn giữ dictionary tồn tại bằng hàm clear()
```python
car.clear()
print(car)
```

```
{}
```

# Lập qua từng phần tử trong dictionary
```python
import sys
sys.stdout.reconfigure(encoding='utf-8')

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print("Lập qua từng key trong dictionary:")
# lập qua từng key trong dictionary bằng vòng for và in ra key đó
for x in thisdict: # hoặc dùng .key() ví dụ for x in thisdict.keys():
  print(x)

print("\nLập qua từng value trong dictionary:")
# lập qua từng value trong dictionary bằng vòng for và in ra value đó
for x in thisdict: # hoặc dùng .values() ví dụ for x in thisdict.values():
  print(thisdict[x])

print("\nLập qua từng cặp key:value trong dictionary:")
# lập qua từng cặp key:value trong dictionary bằng vòng for và in ra cả key và value
for x, y in thisdict.items():
  print(x, y)
```

```
Lập qua từng key trong dictionary:
brand
model
year

Lập qua từng value trong dictionary:
Ford
Mustang
1964

Lập qua từng cặp key:value trong dictionary:
brand Ford
model Mustang
year 1964
```

# Copy dictionary
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy() # hoặc mydict = dict(thisdict)
print(mydict)
```

# dictionary lòng
```python
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
```

# Hoặc tạo 3 dictionary riêng rồi lồng chúng vào một dictionary cha
```python
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
```

# cách láy giá trị trong dictionary lồng nhau
```python
print(myfamily["child2"]["name"])
```

```
Tobias
```

# loop qua dictionary lồng nhau
```python
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
```

```
child1
name: Emil
year: 2004
child2
name: Tobias
year: 2007
child3
name: Linus
year: 2011
```

---

## 6. Lỗi thường gặp (Common Pitfalls)

* Truy cập key không tồn tại → lỗi `KeyError`.
  → dùng `get()` để an toàn.
* Dùng list/dict làm key → lỗi vì không hashable.
* Hiểu lầm rằng dict có thứ tự cũ. (Từ Python 3.7+: dict **giữ thứ tự** insertion.)
* Quên copy sâu → thay đổi nested dict ngoài ý muốn.

---

## 7. So sánh với khái niệm liên quan (Comparison)

| Cấu trúc      | Đặc điểm                          | Khi dùng            |
| ------------- | --------------------------------- | ------------------- |
| `dict`        | key → value, O(1) lookup          | Tra cứu nhanh       |
| `list`        | index → value                     | Dữ liệu theo thứ tự |
| `set`         | giống dict nhưng chỉ key          | Kiểm tra tồn tại    |
| `defaultdict` | dict có default value             | Tránh KeyError      |
| `OrderedDict` | dict có order rõ ràng (trước 3.7) | Kiểm soát order     |

---

## 8. Ứng dụng trong thực tế (Practical Insights)

* Lưu hyperparameters cho model training.
* Đóng gói kết quả eval: accuracy, loss, runtime.
* Quản lý config trong ML pipeline.
* Xây từ điển ánh xạ label → index.
* Làm cache để tăng tốc inference.

---

## 9. Câu hỏi phỏng vấn (Interview Questions)

1. Cơ chế hash table trong dict hoạt động như thế nào?
dict trong Python dùng hash table:

`dict` trong Python dùng **hash table**:
Quy trình:
- Gọi `hash(key)` → ra **giá trị hash**
- Chuyển hash thành **index** trong mảng bằng phép modulo
- Nếu **collision** → xử lý bằng **open addressing + probing**
Python không dùng chain list, mà dùng **probing (linear/quadratic style)**.

**Câu chốt phỏng vấn:**
> Python dict dùng hash table với open addressing, không dùng linked list chaining.

2. Tại sao key phải hashable?

Vì:
* `dict` cần `hash(key)` để xác định vị trí lưu.
* Hash phải **ổn định** trong suốt vòng đời object.

Hashable = object:

* Có `__hash__()`
* Immutable

Ví dụ:
✅ `int`, `str`, `tuple`
❌ `list`, `dict`, `set`

3. Sự khác nhau giữa `dict.get()` và truy cập bằng `[]`?

| `dict[key]`                    | `dict.get(key)`                   |
| ------------------------------ | --------------------------------- |
| Raise `KeyError`               | Trả về `None` (hoặc default)      |
| Dùng khi chắc chắn key tồn tại | Dùng khi **có thể không tồn tại** |

Ví dụ:

```python
d = {"a":1}

d["b"]      # -> KeyError
d.get("b")  # -> None
```

4. Tại sao lookup trong dict là O(1)?
Vì:

* Truy cập trực tiếp qua **hash → index**
* Không phải duyệt tuần tự như list

Thực tế là:
**Average case: O(1)**
**Worst case: O(n)** (rất hiếm, khi collision nhiều hoặc bị attack)

5. Khi nào dict bị rehash?

`dict` rehash (resize + reallocate) khi:
* Load factor vượt ngưỡng (table gần đầy)
* Thường khi ~**2/3 capacity bị sử dụng**

Lúc này:
* Cấp phát mảng mới
* Tính lại index cho toàn bộ key


6. Dict có giữ thứ tự không? (Python 3.7+)
✅ Từ **Python 3.7+**, dict **giữ thứ tự insertion order**.

Quan trọng:
* Đây là **guaranteed behavior**, không phải “side effect”
* Trước 3.7: không đảm bảo

## Câu trả lời mẫu ngắn - đúng chất phỏng vấn:
> Python dict được cài đặt bằng hash table với open addressing. Key phải hashable vì cần hash value ổn định để xác định vị trí lưu. Lookup trung bình là O(1). Dict resize khi vượt load factor. Từ Python 3.7+, dict đảm bảo giữ thứ tự insert.

---

## 10. TL;DR (Short Summary)

* Dict là bảng ánh xạ key–value dùng hash table.
* Lookup cực nhanh (O(1)).
* Key phải immutable + hashable.
* Dùng `get()` để tránh lỗi KeyError.
* Quan trọng cho config, cache, JSON, ML pipelines.

