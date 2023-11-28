#BÀI TẬP VÒNG LẶP FOR
'''
Nhập vào số nguyên dương a và b, 
in toàn bộ ước chung của a và b
'''

a = int(input("nhập số nguyên dương a: "))
b = int(input("nhập số nguyên dương b: "))

for i in range(1,a+1):
    if i > b:
        break
    if a % i == 0 and b % i == 0:
        print(i)

