#BÀI TẬP VÒNG LẶP FOR
'''
Nhập vào số nguyên dương a, 
kiểm tra xem a có phải là số nguyên tố hay không
'''

a = int(input("nhập số nguyên dương a: "))
s = 0
if a>0:
    for i in range(1,a+1):
        if a % i == 0:
            s += 1
    if s > 2:
        print("a không phải số nguyên tố")
    else:
        print("a là số nguyên tố")
else:
    print("a không phải là số nguyên tố")