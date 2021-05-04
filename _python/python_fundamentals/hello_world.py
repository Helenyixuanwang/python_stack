#1. TASK: print "Hello World"
print("Hello Wolrd")

#2. print"Hello {{your name}}!" with the name in a variable

#using a comma in the pirnt function
name = "Michael Jordan"
print("His name is ", name)

#using a + in the print function
lname= "Grace Liu"
print("Her name is "+ lname)

#3. store your favorite number in a variable, and then use it to print the string"Hello {{num}}!" using a comma in the print function(#3a)

number = 7
print("Hello", number)

#usiing a + in the print function
print("Hello " + str(number))

#4. store 2 of your favorite foods in variables, and the use them to print the string "I love to eat {{food_one}} and {{food_two}}." with the format method.

fave_food1="noodle"
fave_food2="salad"
print("I love to eat {} and {}.".format(fave_food1, fave_food2))

#using f-strings
print(f"I love to eat {fave_food1} and {fave_food2}.")

#bonus
#string.upper()
name= "brian liu"
print("His name is ", name.upper())

name="GIGI"
print("I am "+name.lower())

str1="She sells seashells at a seashore"
print("There are "+ str(str1.count("se"))+" se  in this string")

str2="There are three black horses over there"
print(str2.find("horse"))

str3="Percy Buttons is 40 years old"
str4="PercyButtonsis40yearsold"
print(str3.isalnum())
print(str4.isalnum())

str5="This is a painting of sunset"
print(str5.endswith("set"))
