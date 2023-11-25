'''
Nhập vào số nguyên a, nếu a là số chia hết cho 3 
Nằm trong khoảng từ 50 - 100 thì in ra True, ngược lại in ra False
'''
a = int(input("nhap so nguyen a: "))
print( a % 3 == 0 & 50 <= a <= 100)
