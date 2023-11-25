#BÀI TẬP LỆNH ĐIỀU KIỆN CƠ BẢN
'''
Giải và biện luận phương trình ax + b = 0
'''

a = float(input("nhap he so  a: "))
b = float(input("nhap he so  b: "))

if (a == 0 and b == 0):
    print("phương trình vô số nghiệm.")
elif (a != 0):
    print("x = ", -b/a)
else:
    print("phương trình vô nghiêm.")

