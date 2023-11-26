#BÀI TẬP LỆNH ĐIỀU KIỆN CƠ BẢN

'''
Giải và biện luận phương trình ax^2 + bx + c = 0
'''


'''
- Nếu hệ số a chứa tham số, ta xét 2 trường hợp:

   - Trường hợp 1: a = 0, ta giải và biện luận ax + b = 0.

   - Trường hợp 2: a ≠ 0. Ta lập Δ = b2 - 4ac. Khi đó:

      + Nếu Δ > 0 thì phương trình có 2 nghiệm phân biệt 

      + Nếu Δ = 0 thì phương trình có 1 nghiệm (kép): x = -b/2a

      + Nếu Δ < 0 thì phương trình vô nghiệm.
'''

a = float(input("nhap he so  a: "))
b = float(input("nhap he so  b: "))
c = float(input("nhap he so  c: "))

print("phương trình bậc 2: " + str(a) + " x^2 " + str(b) + " x " + str(c) + " = 0")


if (a == 0):
    if (b == 0):
        if (c == 0):
            print("phuong trinh vo so nghiem")
        else:
            print("phuong trinh vo nghiem")
    else:
        print("phuong trinh có 1 nghiem = ", -c/b)
else:
    delta = b * 2 - 4 * a * c
    print("delta = ", delta)
    if (delta > 0):
        print("phuong trinh có 2 nghiem phan biet")
    elif (delta == 0):
        print("phuong trinh có 1 cặp nghiệm kép", -b/(2*a))
    else:
        print("phương trinh vô nghiệm")
        
        