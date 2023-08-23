asgharfruit =["orange", "banana", "apricot", "cucumber", "watermelon", "orange"]
# شمارش تعداد "orange"
asgharfruit.count("orange")

#ترتیب سمت چپ 
listl=(asgharfruit[:5:2])

#ترتیب سمت راست
listr=(asgharfruit[1::2])

#اضافه کردن یک میوه 
asgharfruit.insert(2,"peach")

#حذف کردن یکی از میوه ها
asgharfruit.remove("watermelon")

#اضافه کردن سبد محصول به انتهای  لبست
asgharfruit.append("cherry")

#جایگزین کردن 
asgharfruit[4]=("pineapple")

#حذف کردن یک میوه به دلیل گرانی
asgharfruit.remove("banana")



print(asgharfruit)



