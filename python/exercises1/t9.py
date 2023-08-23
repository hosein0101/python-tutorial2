#برنامه ای بنویسید که همه ی صفر های موجود در لیست زیر را به انتهای لیست منتقل کند
my_list = ["0", "7", "0", "6", "8"]
for i in range(len(my_list)):
    if my_list[i]=="0":
        my_list.remove("0")
        my_list.append("0")

print(my_list)



    
