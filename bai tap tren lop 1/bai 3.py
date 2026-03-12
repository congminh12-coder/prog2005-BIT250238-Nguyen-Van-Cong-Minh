n = int(input(" nhap so tu 1 den 9 :"))
if 1 <= n <= 9:
    print (" bang cuu chuong la :")
    for i in range (1,10):
        ket_qua = n*i
        print(ket_qua)
else:
    print(" loi ket qua ")