zbroj = 0
print("Unosi cijele brojeve (0 za kraj):")

for _ in iter(int,1):
    broj = int(input("Unesi broj: "))
    if broj == 0:
        break
    zbroj += broj

print(f"Zbroj unesenih brojeva je {zbroj}.")    