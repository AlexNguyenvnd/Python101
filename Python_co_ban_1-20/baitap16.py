#BÀI TẬP LỆNH ĐIỀU KIỆN CƠ BẢN
'''
Từ bài số 15, nếu a, b, c cấu tạo thành được một tam giác, 
kiểm tra xem đó là tam giác gì (tam giác đều, tam giác vuông cân, 
tam giác vuông, tam giác cân hay tam giác thường)
'''

#điều kiện cấu thành 1 tam giác là: tổng 2 canh > canh con lai
canha = float(input("nhap do dai canh a: "))
canhb = float(input("nhap do dai canh b: "))
canhc = float(input("nhap do dai canh c: "))

if ( (canha + canhb) > canhc 
    and (canha + canhc) > canhb 
    and (canhb + canhc) > canha):
    if (canha == canhb == canhc):
        print("Đây là 1 hình tam giác đều.")
    elif (canha == canhb or canhb == canhc or canha == canhc):
        if (canha**2 == canhb**2 + canhc**2 or canhb**2 == canha**2 + canhc**2 or canhc**2 == canha**2 + canhb**2):
            print("đây là tam giác vuông cân")
        else:
            print("Đây là 1 hình tam giác cân.")
    elif (canha**2 == canhb**2 + canhc**2 or canhb**2 == canha**2 + canhc**2 or canhc**2 == canha**2 + canhb**2):
        print("Đây à 1 hình tam giác vuông.")
    else:
        print("Đây là 1 hình tam giác thường.")

else:
    print("Đây ko phải là hình tam giác.")
