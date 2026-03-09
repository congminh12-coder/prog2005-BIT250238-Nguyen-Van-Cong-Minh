import math
def la_so_nguyen_to(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
print(" Các số lẻ từ 17 đến 111 : ")
so_le = [i for i in range(17, 112) if i % 2 != 0]
print(so_le)

print("\n Các số nguyên tố từ 17 đến 111 :")
so_nguyen_to = [i for i in range(17, 112) if la_so_nguyen_to(i)]
print(so_nguyen_to)

