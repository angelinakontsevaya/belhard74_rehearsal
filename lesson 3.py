#task1
a=1
b=2
c=("Hello")
d=("Angelina!")
print (a,b,c,d, sep= "-" )

#task2
numbers = (10,12,97)
average = (sum(numbers)/ len(numbers))
print(average)
text = f"{(average):.2f}"
print (text)
#или округление
a = 39.67
b = round (a, 2)
print (b)

#task3
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
text = "Hello {} {}".format(name,age,city)
print(text)
