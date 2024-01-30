#task3
# Пользователь вводит Имя, Возраст,Город, сформировать приветственное сообщение путем форматирования 3-мя способами
#1st
name = "Margo"
age = 28
city = "Minsk"
text = "Hello %s %s %s" % (name, age, city)
print(text)
#2nd
text = "Hello %(first_name)s %(user_age)s %(user_city)s" % {"first_name":name,"user_age":age,"user_city":city}
print(text)
#3d
text = "Hello {} {} {}".format(name,age,city)
print(text)
