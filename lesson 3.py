#task1
a=1
b=2
c=("Hello")
d=("Angelina!")
print (a,b,c,d, sep= "-" )


#task2
numbers = (10,12,97)
average = (sum(numbers)/len(numbers))
print (f"{(average):.2f}")
#или округление
print (round(average),2)


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


#task4
numbers1 =(9,10,1)
count = numbers1.count("if numbers1 > 0, or = 0")
count2 = numbers1.count("if numbers1 < 0")
print ("the count of numbers1: ",count)
print ("the count of numbers1:",count2)

