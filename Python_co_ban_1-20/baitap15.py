#BÀI TẬP LỆNH ĐIỀU KIỆN CƠ BẢN
'''Nhập vào 3 số thực dương a, b, c. Kiểm tra 
xem a, b, c có cấu thành độ dài của 1 tam giác được không?
'''

#điều kiện cấu thành 1 tam giác là: tổng 2 canh > canh con lai
canha = float(input("nhap do dai canh a: "))
canhb = float(input("nhap do dai canh b: "))
canhc = float(input("nhap do dai canh c: "))

if ( (canha + canhb) > canhc 
    and (canha + canhc) > canhb 
    and (canhb + canhc) > canha):
    print("Đây là 1 hình tam giác.")
else:
    print("ko phải là hình tam giác.")