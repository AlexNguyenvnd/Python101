#BÀI TẬP LỆNH ĐIỀU KIỆN CƠ BẢN

'''
Nhập ngày vào ngày, tháng. Hãy tính và 
in ra xem ngày nhập vào cách ngày đầu năm bao nhiêu ngày 
(giả sư năm đó không phải là năm nhuận)
'''

ngay = int(input("nhap ngay vao: "))
thang = int(input("nhap thang vào: "))

if (thang <= 8):
    sothang30ngay = (thang - 1)//2
    sothang31ngay = thang//2
else:
    sothang30ngay = thang//2 - 1
    sothang31ngay = (thang + 1)//2

so_ngay = ngay + sothang30ngay * 30 + sothang31ngay * 31

if thang > 2:
    so_ngay = so_ngay- 2

print(so_ngay)
