#BÀI TẬP LỆNH ĐIỀU KIỆN CƠ BẢN
'''Nhập vào số nguyên dương a, nếu a là số chẵn 
thì in ra đây là số chẵn, 
ngược lại in ra đây là số lẻ
'''

a = int(input("nhap so nguyen duong a: "))

if (a % 2 == 0):
    print("day la so chan.")
else:
    print("day la so le.")