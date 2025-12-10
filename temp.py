# ------- frozenset là phiên bản bất biến của một tập hợp.-------

# Giống như sets, frozenset chứa các phần tử duy nhất, không có thứ tự và không thể thay đổi.
# Không giống như sets, các phần tử không thể được thêm hoặc bớt khỏi frozenset.

# dùng frozenset() để tạo frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x) # Kết quả: frozenset({'cherry', 'banana', 'apple'})
print(type(x)) # Kết quả: <class 'frozenset'>