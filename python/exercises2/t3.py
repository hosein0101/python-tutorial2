string=input("Enter the string :")
count={}
for char in string:
    if char not in count:
     count[char]=1
    else:  
      count[char]+=1
for char,count in count.items():
    print(f"{char}:{count}")