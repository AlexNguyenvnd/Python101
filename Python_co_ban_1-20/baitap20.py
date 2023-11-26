#BÀI TẬP LỆNH ĐIỀU KIỆN CƠ BẢN

'''
Nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày
'''
# tháng có 31 ngày: 1 3 5 7 8 10 12
# tháng có 30 ngày: 4 6 9 11
# tháng có 28, 29 ngày: 2
# năm nhuận là năm chia hết cho 4 nhưng ko chia hết cho 100  
# hoặc chia hết cho 400 cũng là năm nhuân

thang = int(input("Nhập tháng bạn cần tra số ngày trong tháng: "))
nam = int(input("Nhập năm bạn cần tra số ngày trong tháng: "))

if (thang == 1 or thang == 3 or thang == 5 or thang == 7 
    or thang == 8 or thang == 10 or thang == 12):
    print(f"tháng {thang} này có 31 ngày.")
elif (thang == 4 or thang == 6 or thang == 9 or thang == 11):
    print(f"tháng {thang} này có 30 ngày.")
else:
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print(f"tháng {thang} này có 29 ngày.")
    else:
        print(f"tháng {thang} này có 28 ngày.")