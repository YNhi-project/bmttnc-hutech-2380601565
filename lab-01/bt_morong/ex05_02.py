import re

chuoi = input("Nhập chuỗi bất kỳ: ")

cac_so = re.findall(r'-?\d+', chuoi)

tong_duong = 0
tong_am = 0

for s in cac_so:
    so = int(s)
    if so > 0:
        tong_duong += so
    elif so < 0:
        tong_am += so

print("Giá trị dương:", tong_duong)
print("Giá trị âm:", tong_am)