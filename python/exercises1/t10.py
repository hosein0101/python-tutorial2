#برنامه ای بنویسید که یک عدد به عنوان تعداد دانش آموزان دریافت کند
#سپس برای هر دانش آموز نام و  نمره های ریاضی و علوم و هنر دانش آموز را دریافت کنید
#حالا از کاربر دوباره نام یک دانش آموز را دریافت کنید و میانگین آن دانش اموز را در خروجی نمایش دهید

number_student=int(input("number_student:"))
students=[]
for i in range((number_student)):
      name=input("name student :")
      math=int(input("Enter the math numbeer:"))
      science=int(input("Enter the science number:"))
      art=int(input("Enter the art number:"))
      savarge= (math+science+art) / 3
      students.append([name,savarge])
student_name=input("Enter student wnana see the savarge: 2")
for item in students:
      if item[0]==student_name:
            print(item[1])
            break
      else:
            print("student not exests")

            

