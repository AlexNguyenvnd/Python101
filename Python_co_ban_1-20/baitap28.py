#BÀI TẬP VÒNG LẶP FOR
'''
Nhập vào n
Tính S = 1 + 2 + 3 + 4 + … + n
'''

n = int(input("nhập vào n "))
s = 0
for i in range(n):
    i += 1
    s = s + i
    

print("tổng s là: ", s)

