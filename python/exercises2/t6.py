string = input("Enter a string: ")

seen = set()
for char in string:
  if char in seen:
    print("NO")
    break
  else:
    seen.add(char)
else:
  print("YES")

