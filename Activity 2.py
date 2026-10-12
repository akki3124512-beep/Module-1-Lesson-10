upper = int(input("Enter your upper range: "))
lower = int(input("Enter your lower range: "))
print("The prime number in your range is:")
for n in range(lower, upper + 1):
  if n > 1:
    for i in range(2, n):
      if (n % i) == 0:
        break
    else:
      print(n)