# GIỚI THIỆU VỀ PYTHON

## Câu a:

### int

Int, hoặc integer, là một số nguyên, dương hoặc âm, không có số thập phân, có độ dài không giới hạn.
<br>
Ví du:
<br>
x = 1
<br>
y = 35656222554887711
<br>
z = -3255522

### float

Float, hoặc "số dấu phẩy động" là một số, dương hoặc âm, chứa một hoặc nhiều số thập phân.Float cũng có thể là các số khoa học với chữ "e" để biểu thị lũy thừa của 10.
<br>
Ví dụ
<br>
x = 1.10
<br>
y = 1.0
<br>
z = -35.59

### str

Các ký tự chuỗi trong python được bao quanh bởi dấu ngoặc kép đơn hoặc dấu ngoặc kép.
<br>
Ví dụ:
<br>
'hello' cũng giống như "hello".
<br>
Bạn cũng có thể gán một chuỗi nhiều dòng cho một biến bằng cách sử dụng ba dấu ngoặc kép:
<br>
Ví dụ:
<br>
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
<br>
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

### list

List là một tập hợp được sắp xếp và có thể thay đổi. Trong Python, list được viết bằng dấu ngoặc vuông.Bạn truy cập các mục trong list bằng cách tham chiếu đến số chỉ mục.Ngoài ra, cũng có thể sử dụng hàm tạo list() để tạo một danh sách mới.<br>
Ví dụ:<br>
thislist = ["apple", "banana", "cherry"]<br>
print(thislist[1])<br>
thislist = list(("apple", "banana", "cherry"))<br>

### tuple

tuple là một tập hợp được sắp xếp theo thứ tự và không thể thay đổi. Trong Python, tuple được viết bằng dấu ngoặc tròn.Bạn có thể truy cập phần tử của tuple bằng cách tham chiếu đến số chỉ mục, bên trong dấu ngoặc vuông.Cũng có thể sử dụng hàm tạo tuple() để tạo một bộ tuple.<br>
Ví dụ:<br>
thistuple = ("apple", "banana", "cherry")<br>
print(thistuple[1])<pr>
thistuple = tuple(("apple", "banana", "cherry"))<br>
Khi một tuple được tạo, bạn không thể thay đổi các giá trị của nó. Tuples là không thể thay đổi, hoặc cũng được gọi bất biến.Nhưng có một cách giải quyết. Bạn có thể chuyển đổi tuple thành một list, thay đổi list và chuyển đổi lại list thành tuple.<br>

### set

set là một tập hợp không có thứ tự và không được lập chỉ mục. Trong Python, set được viết bằng dấu ngoặc nhọn.Bạn không thể truy cập các mục trong một set bằng cách tham chiếu đến chỉ mục hoặc khóa.Nhưng bạn có thể lặp qua các phần tử trong set bằng vòng lặp for hoặc kiểm tra xem giá trị được chỉ định có trong set hay không bằng cách sử dụng từ khóa in.<br>
Ví dụ:<br>
thisset = {"apple", "banana", "cherry"}<br>
for x in thisset:<br>
####code####<br>
Sau khi set được tạo, bạn không thể thay đổi các mục của nó, nhưng bạn có thể thêm các mục mới.Có thể sử dụng hàm tạo set() để tạo một set.<br>

### dict

dictionary là một tập hợp không có thứ tự, có thể thay đổi và được lập chỉ mục. Trong Python dictionary được viết bằng dấu ngoặc nhọn và chúng có các khóa và giá trị.dictionary cũng có thể chứa nhiều dictionary, đây được gọi là nested dictionaries.Cũng có thể sử dụng hàm tạo dict() để tạo dictionary mới.<br>
Ví dụ:<br>
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}<br>
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
}<br>
thisdict = dict(brand="Ford", model="Mustang", year=1964)<br>

### bool

Boolean đại diện cho một trong hai giá trị: True hoặc False.<br>
Ví dụ:<br>
a=True<br>
a=10>9 #True<br>
a=9>10 #False<br>

### bytes

Kiểu dữ liệu byte có thể được tạo ở hai dạng: dùng hàm byte() hoặc sử dụng tiền tố “b”.<br>
Ví dụ:<br>
print(byte("hello","utf-8")) #b'hello'<br>
print(type(byte("hello","utf-8"))) #<class 'bytes'><br>
