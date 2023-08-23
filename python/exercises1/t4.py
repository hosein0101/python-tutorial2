#برنامه ای بنویسید که مجموع اعداد لیست زیر و میانگین  را نمایش دهد
a = [1,2,3,4,5]
sum=0
for i in range(len(a)):
    sum+=a[i]
m=sum/len(a)
print(sum)
print(m)



