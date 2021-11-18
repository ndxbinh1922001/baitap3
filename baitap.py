import random
import string


def bai1():
    print("De bai: Cho nguoi dung nhap vao hai so nguyen va tra ve tich cua chung. Neu ket qua lon hon 1000 thi tra ve tong cua chung.")
    while(True):
        mystr = input("Nhap vao 2 so nguyen (cach nhau 1 khoang trang):")
        mylist = mystr.split(' ')
        if (len(mylist) == 2):
            break
        print("Du lieu khong phu hop.Vui long nhap lai!")
    if((int(mylist[0])*int(mylist[1])) > 1000):
        print("Ket qua:", int(mylist[0])+int(mylist[1]))
    else:
        print("Ket qua:", int(mylist[0])*int(mylist[1]))


def bai2():
    print("De bai: Cho nguoi dung nhap vao so nguyen duong n. Su dung ham range() de sinh ra day so 0 ≤ x < n , thuc hien tinh tong day tren va xuat ket qua ra man hinh.")
    n = int(input("Nhap so phan tu cua day: "))
    sum = 0
    for i in range(0, n):
        a = int(input("Nhap phan tu thu {} :".format(i+1)))
        sum += a
    print("Ket qua: ", sum)


def bai3():
    print("De bai: Cho phep nguoi dung nhap chuoi ky tu tu ban phim. Hien thi nhung ky tu o vi tri chan ra man hinh (theo thu tu trong chuoi).")
    a = input("Nhap vao chuoi ki tu: ")
    vitri = 0
    result = ""
    for i in a:
        if (vitri % 2 == 0):
            result += i
        vitri += 1
    print("Ket qua:", result)


def bai4():
    print("De bai: Cho phep nguoi dung nhap chuoi ky tu tu ban phim va so nguyen n Hien thi ra man hinh n ky tu cuoi cung trong chuoi tren")
    a = input("Nhap vao chuoi ky tu: ")
    n = int(input("Nhap vao so nguyen n: "))
    if (int(n) >= int(len(a))):
        print("Ket qua:", a)
    elif (n <= 0):
        print("n khong phu hop")
    else:
        print("Ket qua:", a[len(a)-n:])


def bai5():
    print("De bai: Cho danh sach cac so nguyen duoc nhap tu ban phim Tra ve True neu so dau tien va so cuoi cung cua danh sach giong nhau Nguoc lai tra ve False")
    a = input("Nhap danh sach cac so nguyen (cach nhau 1 khoang trang) :")
    l = a.split(' ')
    if (int(l[0]) == int(l[-1])):
        print("Ket qua: True")
    else:
        print("Ket qua : False")


def bai6():
    print("De bai: Cho phep nguoi dung nhap vao so nguyen duong n Thuc hien sinh ra n so nguyen ngau nhien va in ra man hinh nhung so nguyen to trong day so vua sinh ra theo thu tu tang dan")
    n = int(input("Nhap vao so nguyen duong: "))
    a = []
    for i in range(0, n):
        a.append(random.randint(0, 1000))
    a.sort()
    print("Ket qua: ", end="")
    for i in range(0, n):
        print(a[i], end=" ")
    print('\n', end='')


def bai7():
    print("De bai: Cho mot chuoi bat ky nhap tu ban phim dao nguoc chuoi tren va xuat ra man hinh Voi cac ky tu in thuong chuyen thanh in hoa; va nguoc lai chuyen cac ky tu in hoa sang in thuong")
    a = input("Nhap chuoi ky tu tu ban phim: ")
    new_str = ""
    for i in range(len(a)):
        if a[i].isupper():
            new_str += a[i].lower()
        elif a[i].islower():
            new_str += a[i].upper()
        else:
            new_str += a[i]
    print("Ket qua:", new_str[::-1])


def bai8():
    print("De bai:8 Cho 1 list gom n so nguyen duoc sinh ngau nhien n nhap tu ban phim hay ghi cac phan tu cua list nay ra file “f txt” sao cho\n- Moi phan tu nam rieng le tren 1 dong\n- Dong duoi se thut lui vao trong so voi dong tren 1 dau cach")
    n = int(input("Nhap so nguyen duong: "))
    file = open("f.txt", "w")
    for i in range(n):
        a = random.randint(0, 1000)
        file.write(" "*i + str(a) + "\n")
    file.close()
    print("Ket qua: Da ghi vao file f.txt")


def bai9():
    print("De bai: Hay doc file “f txt” trong bai tren va xuat ra man hinh bieu thuc phep tinh cong va tong cua chung cua cac so co trong file")
    with open("f.txt", "r") as file:
        lines = file.readlines()
    sum = 0
    for line in lines:
        sum += int(line.strip())
    print("Ket qua:", sum)


def bai10():
    print("De bai: Hay chen them dong chu “Lap trinh ung dung WEB” viet Tieng Viet co dau  vao cuoi file “f txt” ma khong lam mat noi dung truoc do cua file f khi mo file f len phai doc duoc Tieng Viet co dau")
    s = "Lập trình ứng dụng WEB\n"
    with open("f.txt", "ab") as file:
        file.write(string.capwords(s).encode("utf-8"))
    with open("f.txt", "rb") as file:
        lines = file.readlines()
    for line in lines:
        print(line.decode("utf-8"), end='')
    print("\nKet qua: Da ghi file va doc file")


def bai11():
    print("De bai: Cho danh sach list gom 10 so nguyen duoc nhap tu ban phim co the trung nhau Hay tao mot danh sach y lay cac phan tu tu x khong trung nhau Ghi them y vao file f txt sao cho khong lam mat noi dung truoc do cua file f txt")
    while (True):
        a = input("Nhap 10 so nguyen (cach nhau 1 khoang trang) :")
        b = a.split(' ')
        if (int(len(b)) == 10):
            break
        else:
            print("Du lieu khong phu hop")
    b = list(map(int, b))
    c = set(b)
    b = list(c)
    b = list(map(str, b))
    d = ' '.join(b)
    with open("f.txt", "a") as file:
        file.write('\n'+str(d))
    print("Ket qua: Da them list vao file f.txt")


def read_number(n):
    mau = ["khong ", "mot ", "hai ", "ba ", "bon ",
           "nam ", "sau ", "bay ", "tam ", "chin "]


def them(vitri):
    if vitri == 2:
        return "mươi"
    elif vitri == 3:
        return "trăm"
    elif vitri == 4:
        return "nghìn"
    elif vitri == 5:
        return "mươi"
    elif vitri == 6:
        return "trăm"
    elif vitri == 7:
        return "triệu"
    else:
        return ""


def so2chu(n, a=False):
    if (n == 0):
        return "không"
    elif (n == 1):
        if a == False:
            return "một"
        else:
            return "mốt"
    elif (n == 2):
        return "hai"
    elif (n == 3):
        return "ba"
    elif (n == 4):
        return "bốn"
    elif (n == 5):
        if (a == False):
            return "năm"
        else:
            return "lăm"
    elif (n == 6):
        return "sáu"
    elif (n == 7):
        return "bảy"
    elif (n == 8):
        return "tám"
    elif (n == 9):
        return "chín"
    else:
        return ""


def bai12():
    print("De bai: Cho file input txt moi dong la cac so nguyen tu 0 den 10 000 000 Thuc hien doc nhung so nay va ghi ket qua vao file output txt\nVi du:\n125000 \t\tmot tram hai muoi lam nghin\n1100075\t\tmot trieu mot tram nghin khong tram bay muoi lam")
    with open("input.txt", "r") as file:
        lines = file.readlines()
    #val = "1100075"
    for line in lines:
        line = line.replace('\n', '')
        val = str(line)
        vitri = len(val)
        i = 0
        result = ""
        if int(val) == 0:
            print("Không")
        else:
            while(vitri > 0 and i < len(val)):
                if (int(val[i]) != 0 or vitri == 6 or vitri == 3):
                    result = str(result) + " " + \
                        so2chu(int(val[i]), i == len(val)-4 or i ==
                               len(val)-1)
                if (int(val[i]) != 0 or vitri == 6 or vitri == 3 or vitri == 4):
                    result = result + " " + them(vitri)
                vitri -= 1
                i += 1
        with open("output.txt", "ab") as file:
            file.write(string.capwords(result).encode(
                "utf-8")+"\n".encode("utf-8"))
    print("Ket qua: Da chuyen so sang chu va ghi vao file output.txt")


def main():
    while (True):
        a = -1
        while(True):
            a = int(input("Hay chon bai tap (1-12).Nhap 0 de thoat chuong trinh :"))

            if (a == 0):
                return 0
            if (a >= 1 and a <= 12):
                break
            print("Lua chon khong phu hop. Vui long chon lai (0-12)!")
        if (a == 1):
            bai1()
        elif (a == 2):
            bai2()
        elif (a == 3):
            bai3()
        elif (a == 4):
            bai4()
        elif (a == 5):
            bai5()
        elif (a == 6):
            bai6()
        elif (a == 7):
            bai7()
        elif (a == 8):
            bai8()
        elif (a == 9):
            bai9()
        elif (a == 10):
            bai10()
        elif (a == 11):
            bai11()
        elif (a == 12):
            bai12()
        else:
            print("Du lieu khong ton tai")


if __name__ == "__main__":
    main()
