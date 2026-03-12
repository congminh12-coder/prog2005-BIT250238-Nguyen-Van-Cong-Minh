sinh_vien = {" long": 9.5 , "minh" : 8.5 , " toàn" : 7.0 }
tong = 0
dem = 0
for i in sinh_vien:
    tong += sinh_vien[i]
    dem += 1
print (f"diem trung binh cua cac sinh vien la : ",tong/dem )
