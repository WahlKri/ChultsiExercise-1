"Chapters 10 - 14"
"""
"What does \t do?"
#tabulate
jultsi = "I'm split\non a line." \

print jultsi
"""

#pultsi = "\tI'm tabbed in one line."
#print(pultsi)

#"How about \n ?"
#a new line
#"Try to print out next sentence: 'OMG I just made a backslash \'"

#sentence = "OMG I just made a backslash \\ "

#print sentence


"Print a bulleted-list like so dismiss the comments #"

#   We need from the store:
#     * Teetua
#     * Leipua
#     * Karkkia
#     * Lisaa teetua


#kauppalista = """
#We need from the store:
#\t*Teetua
#\t*Leipua
#\t*Karkkia
#\t*Lisaa teetua
#"""


#print kauppalista
#"""

#"Try out the next code"

#"""
#while True:
  #  for i in ["/","-","|","\\","|"]:
   #     print "%s\r" % i,
#"""


"What happened and why?"

#crashed down :(((((

"To get input use the following function: 'input()', you can test it out by writing print(input())"
"You can also do name = input(). Test it out and write what it does"

#print(input())

#age = input()

#print age

"Next make a program that asks name, age and birthplace from the user. Save inputs to variables and print them out"
"""
print "What is your name?"
name = raw_input()
print "How old are you?"
age = input()
print("Where were you born?")
birthplace = raw_input()

print name, age, birthplace
"""
"Make a calculator which asks for a two integers and pluses them together. For example "
#Give number a: 
#Give number b: 
#The sum of a and b is result
"""
a = input()
b = input()
sum = (a+b)

print "Lukujen summa on %d" % sum
"""
"Did you encounter any problems? Remember that raw_input() produces raw data format/string. You must somehow turn that "
"into integer. For example '(float) variable = 5', turns 5 into decimal 5.0. That is called casting"

"What happens if you try input(5). Why this happens?"
"""
input(5)
"""
"Difference between %s and %r?"
# %s for display, %r for raw debugging

"""
age = raw_input("How old are you? ")
print age
"""

"What happens when you write input(), PyCharm gives more info about the function and it should say print(prompt),"
"What do you think prompt means and how it could be used? Hint: input(\"Give a number\")"

#print(input("Give a number"))

"Use this new way of writing a program that asks for a name, age and birthplace. It should also print the results out"
"""
name = raw_input("What's your name?")
age = raw_input("How old are you?")
birthplace = raw_input("Where were you born?")

print name
print age
print birthplace
"""
"Read chapter 14 and answer to these questions."
"What does import do? How about from?"

# en jaksa kirjottaa


"Try to import 'getsizeof' from sys and use it"
"""
from sys import getsizeof
var = getsizeof(100)
print var
"""
"import argv from sys. And make a variable called 'path' and set its value to argv[0]. Then print the variable 'path'"
"What happened?"

from sys import argv
path = argv[0]
print path

"Make a program that works the following way. You can use any structure you want, but the main idea is to ask the user"
"a couple of questions and print them out"

"""
I'd like to ask you a few questions.
What is your name?
> Kalle (user input)
Do you like me Kalle?
>  Yes (user input)
Where do you live Kalle?
>  San Francisco (user input)
What kind of computer do you have?
>  Tandy 1000 (user input)

Alright, so you said 'Yes' about liking me.
You live in 'San Francisco'.  Not sure where that is.
And you have a 'Tandy 1000' computer.  Nice.


"""
print "I'd like to ask you a few questions."
print "What's your name?"
name = raw_input()
print "Do you like me %s?" % name
likes = raw_input()
print "Where do you live %s?" % name
living = raw_input()
print("What kind of a computer do you have?")
computer = raw_input()

print """
Your name is %s.
You answered \'%s\' about liking me.
You are living in %s.
Your computer is %s.
""" %(name, likes, living, computer)



