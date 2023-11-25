'''
Nhập vào số nguyên a, kiểm tra xem a có phải là số chính phương hay không, 
nếu có thì in ra True, ngược lại in ra False
'''

a = int(input("nhap so nguyen a: "))

#Số chính phương là số bằng bình phương đúng của một số nguyên
#kiểm tra căn bâc hai số a là số nguyên
b = a**0.5
print(round(b) == b)