'''
Nhập vào nguyên a và b, 
nếu 1 trong 2 số a và b chia hết cho 2 
thì in ra True, ngược lại in ra False
'''

a = int(input("nhap so nguyen a: "))
b = int(input("nhap so nguyen b: "))

print(a % 2 == 0 or b % 2 == 0)