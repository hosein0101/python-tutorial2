#برنامه ای بنویسید که دومین عضو کوچک لیست زیر را نمایش دهد
a = ["2", "5", "1",  "3", "4"]
smallest = a[0]
second_smallest = a[0]

for i in range(len(a)):
   if a[i]<=smallest:
       smallest=a[i]
   elif a[i]<=second_smallest:
       second_smallest=a[i]

print(second_smallest)
