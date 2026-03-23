danh_sach =[]
for i in range(6):
    chuoi = str(input(" chuoi "))
    danh_sach.append(chuoi)
danh_sach_so = []
for chu in danh_sach:
    so = int(chu)
    if so % 2 == 0:
       danh_sach_so.append(so)
danh_sach_chan = []
tong_chan = 0
for n in danh_sach_so:
    if n % 2 == 0:
        print ("so chan la : ",n)
        tong_chan = tong_chan + n
print(tong_chan)



