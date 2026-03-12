typle = (1, 2 , 4 ,7 ,9)
sum = 0
for i in typle:
    sum += i
    max_index = tuple[0]
    min_index = tuple[0]
    if sum > max_index:
        max_index = i
    if sum < min_index:
        min_index = i
print ("tong la :", i)
print ("so lon nhat la :", max_index)
print ("so nho nhat la :", min_index)