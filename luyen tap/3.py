n = 4
print("\n Hình 1:")
for i in range(n):
    for j in range(n):
        print(1, end=" ")
    print()

print("\n Hình 2:")
for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()

print("\n Hình 3:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n Hình 4:")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n Hình 5:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print(j, end=" ")
        else:
            print("  ", end="")
    print()

print("\n Hình 6:")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print(j, end=" ")
        else:
            print("  ", end="")
    print()

print("\n Hình 7:")
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print(i, end="   ")
        else:
            print("    ", end="")
    print()

print("\n Hình 8:")
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()

n = 4
print("\n Hình 9")

for i in range(1, n + 1):
    print("  " * (n - i), end="")
    if i == 1:
        print(1)
    elif i == n:
        for j in range(1, n + 1):
            print(j, end=" ")
        for j in range(n - 1, 0, -1):
            print(j, end=" ")
        print()
    else:
        print(1, end="")
        print("  " * (2 * i - 3), end=" ")
        print(1)