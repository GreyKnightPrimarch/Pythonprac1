# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
Hello = "Hello"
print(Hello,name)	# with a comma
print(Hello+name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print(Hello,name)	# with a comma
# print(Hello+name)# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables

fave_food1 = "sushi"
fave_food2 = "pizza"
eats = f'I love to eat {f"{fave_food1}"} and {f"{fave_food2}"}.'
print(eats)
pi = 3.14151829573
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
string = f'{"%.4f"%pi:<10}'+"end"
print(txt1) # with .format()
print(string) # with an f string

