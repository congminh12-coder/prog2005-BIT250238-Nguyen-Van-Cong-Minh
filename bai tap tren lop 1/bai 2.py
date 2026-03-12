
import math
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
luy_thua = a ** b
can_bac_2_a = math.sqrt(a) \
    if a >= 0 \
    else "Không thể tính căn bậc 2 của số âm"
if b != 0:
        chia_nguyen = a // b
        chia_du = a % b
else:chia_nguyen = chia_du = "Không thể chia cho 0"
lam_tron_a = round(a, 2)
print(f"1. Lũy thừa :",luy_thua)
print(f"2. Căn bậc hai của a: ", can_bac_2_a)
print(f"3. Chia lấy phần nguyên : ", chia_nguyen)
print(f"4. Chia lấy phần dư :" , chia_du)
print(f"5. Làm tròn số a (đến 2 chữ số):", lam_tron_a)