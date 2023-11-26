#BÀI TẬP LỆNH ĐIỀU KIỆN CƠ BẢN

'''
Nhập điểm toán, văn, anh.
Nếu điểm đúng quy tắc (trong khoảng từ 0 - 10), 
-> ta tính điểm trung bình rồi tiến hành xét:

Nếu điểm trung bình >= 8, toán hoặc văn >= 8 và không có điểm nào dưới 6.5 
    thì in ra “Học sinh giỏi”

Nếu không đủ điều kiện học sinh giỏi ta xét nếu điểm trung bình >= 6.5, 
    toán hoặc văn >= 6.5 và không có điểm nào dưới 5 thì in ra “Học sinh khá”


Nếu không đủ điều kiện học sinh yếu ta in ra “Học sinh kém”
'''

a = float(input("điểm môn toán: "))
b = float(input("điểm môn văn: "))
c = float(input("điểm môn anh: "))

if (0<= a <=10 and 0<= b <=10 and 0<= c <=10):
    dtb = (a + b + c) / 3
    if (dtb >= 8) and (a >= 8 or b >= 8) and (a > 6.5 and b > 6.5 and c > 6.5):
        print("Học sinh giỏi.")
    elif (dtb >= 6.5) and (a >= 6.5 or b >= 6.5) and (a > 5 and b > 5 and c > 5):
        print("Học sinh khá.")
    else:
        print("Học sinh kém.")

else:
    print("Nhập điểm không hợp lệ.")

