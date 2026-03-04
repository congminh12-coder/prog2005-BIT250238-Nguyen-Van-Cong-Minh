#bai 3
mau_sac = ["red", "blue", "green", "purple", "white"]
print(mau_sac)
try:
    mau_sac.remove("green")
    print(mau_sac)
except ValueError:
    print(mau_sac)