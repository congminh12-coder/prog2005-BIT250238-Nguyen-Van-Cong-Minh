import math
try :
    n = int(input(" so ngau nhien "))
    if n < 0 :
        print(" so loi ")
    else :
        ket_qua = math.sqrt(n)
        print(" can bac hai cua n la : ",ket_qua)
except :
    print(" loi " )


