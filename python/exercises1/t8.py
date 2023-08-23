#لیستی از نمرات به شما داده شده است
#اگر همه ی نمرات بالای ۱۰ بودند در خروجی عبارت pass و در غیر این صورت عبارت fail رو چاپ کنید
my_list= [20,18,12,15,20]
for score in my_list:
    if score < 10 :
     print("fail")
else:
  print("pass")
   
print("pass"if all(score>10 for score in my_list ) else "fail" )

   
        
        
      
