dic = {'minh':'25IT','lam':'25IT','quoc':'25IT','nhung':'25MK'}
a = input('Nhap key: ')
if a not in dic:
    print('Key nay khong ton tai trong dictionary')
else:
    print(dic[a])