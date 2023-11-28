#BÀI TẬP VÒNG LẶP FOR
'''
Nhập vào số nguyên dương a, 
đếm số ước của a
'''

a = int(input("nhập số nguyên dương a: "))
s = 0

for i in range(1,a+1):
    if a % i ==0:
        s += 1
print(s)