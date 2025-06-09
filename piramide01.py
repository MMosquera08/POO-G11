print("Pirámide.")
z = 5
x = 1
print("0" * z + "0" * x + "0" * z)
while z > 0:
    print("0" * z + "1" * x + "0" * z)
    x += 2
    z -= 1
print("0" * z + "0" * x + "0" * z)