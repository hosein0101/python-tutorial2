#لیست به شما داده شده است
#لیست دوم را از لیست اول تفریق کنید

a =[2,4,6,8,10]
b =[1,3,6,4,8]
c=[]
for i in range(len(a)):
  if a[i]not in b:
    c.append(a[i])
print(c)