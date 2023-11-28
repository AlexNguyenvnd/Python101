#BÀI TẬP VÒNG LẶP FOR
'''
Nhập vào số nguyên dương a, in ra bảng cửu chương của a
'''

a = int(input("nhập số nguyên dương a: "))

for i in range(10):
    i += 1
    print(f"{a} x {i} =", (a*i))