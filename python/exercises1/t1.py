#تبدیل کند intبرنامه ای که فقط عدد زوج داخل لیست را بهب
a=["1","2","3","4","5","6","7","8"]
for idx in range(len(a)):
    if int(a[idx])%2==0:
        a[idx]=int(a[idx])
    else:
        a[idx]=str(a[idx])

print(a)
  

