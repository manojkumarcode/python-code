for num in range(0,10):
    if num == 5:
        print(f"Breaking the look at Number{num}")
        break
    else: 
        print(f"Number is {num}")

for num in range(1, 6):
    if num == 3:
        continue
    print(num)

print("range(-5,5)")

for num in range(-5,6):
    print(num)

print(" ['A', 'B', 'C']")
for x in ['A', 'B', 'C']:
    print(x + 'A')