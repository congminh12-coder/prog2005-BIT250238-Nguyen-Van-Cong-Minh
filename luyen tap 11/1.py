def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and len(arr[j]) > len(key):
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key
strings = []
for i in range (5):
    strings.append(input(" 5 chuoi bat ky la :"))
insertion_sort(strings)
print(strings)
