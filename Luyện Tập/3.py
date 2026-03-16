n = input('Nhap ten: ')
n = n.strip()

a = n.split()

b = []
for i in a:
    b.append(i.capitalize())

c = " ".join(b)
print('Ten chuan: ', c)