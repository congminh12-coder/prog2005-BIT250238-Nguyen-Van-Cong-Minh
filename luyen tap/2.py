n = 4
print(" Hình 1")
for i in range(n):
    print("* " * n)

print("\n Hình 2")
for i in range(1, n + 1):
    print("* " * i)

print("\n Hình 3")
for i in range(n, 0, -1):
    print("* " * i)

print("\n Hình 4")
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

print("\n Hình 5")
for i in range(n):
    for j in range(i + 1):
        # j == 0 là cạnh đứng, i == n-1 là cạnh đáy, i == j là cạnh huyền
        if j == 0 or i == n - 1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\n Hình 6")
for i in range(n):
    for j in range(n - i):
        if i == 0 or j == 0 or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print(" Hình 7")
for i in range(n):
    for j in range(n):
        if j == n - 1 or i == n - 1 or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\n Hình 8")
for i in range(n):
    print(" " * (n - i - 1), end="")
    print("* " * (i + 1))
    print()

print("\n Hình 9")
for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(i + 1):
        if j == 0 or j == i or i == n - 1:
            print("*", end=" ")
        else:
            print("  ", end="")
    print()

print("\n  Hình 10")
for i in range(n):
    print(" " * i, end="")
    for j in range(n - i):
        if i == 0 or j == 0 or j == n - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()