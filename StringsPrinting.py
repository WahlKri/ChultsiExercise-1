"Chapters 4-9"


"Do the calculation of two different decimals. The output should be 0.425"


#"Copy next variables and fill them with your personal information. After that use %-operator to print strings" +
"like so:  print("#My name is -the operator- (your_variable)"). Hint: there are two different %-operators for strings"+
"%s and %d figure out what they do and use the correct one."

my_name = 'Julia Poutanen'
my_age = 21
my_height = 158 # centimeters
my_weight = 53 # kilograms
my_eyes = 'green'
my_teeth = 'what'
my_hair = 'dark'



"What is %s used for?"
#for strings
"What is %d used for?"
#for variables
"Use % for every variable and print them out somehow (you can use any sentence you like)"
print my_name
print "Let's talk about %s." % my_name

print "She's %d centimeters tall." % my_height

##"Calculate the sum of your weight, height and age using %-operator for strings. "+
"For example 'My age is 10, my height is 160 and my weight is 50" 
"Sum of those is 220"

print "My age is %d, my height is %d and my weight is %d." % (my_age, my_height, my_weight)
print "Sum of those is %d." % (my_age + my_height + my_weight)

#"Make a variable called 'truth' and set it to 42. Next make a variable called truth_sentence and use %-operator " +
#"to construct following sentence using the 'truth'-variable: 'the meaning of life is 42'" +
#"Next make a new variable called whole_sentence. The command print(whole_sentence) should produce " +
"I heard that the meaning of life is 42"

truth = 42
truth_sentence = "the meaning of life is %d" %truth
whole_sentence = "I heard that %s" % truth_sentence
print whole_sentence

#end1 = "C"
#end2 = "h"
#end3 = "e"
#end4 = "e"
#end5 = "s"
#end6 = "e"
#end7 = "B"
#end8 = "u"
#end9 = "r"
#end10 = "g"
#end11 = "e"
#end12 = "r"

#"Copy those variables and construct a sentence using '+' and print(). Then print it 100 times " +
#"so that every word is separated by a line (Hint: print("a\n"*10), prints 'a' ten times to different rows)" +
#"\n means newline"

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

lause = end1 + end2 + end3 + end4 + end5 + end6 + end7 + end8 + end9 + end10 + end11 + end12
print lause
print lause * 100
print ((lause + "\n") * 10)

#"Make a variable 'formatter = %r %r %r %r' (%r means raw data and works as %-operator)." +
#"Now use it to display numbers like this: '1 2 3 4'"

formatter = "%r, %r, %r, %r."
print formatter % (1, 2, 3, 4)


"Make a variable that when called print(variable) prints out the next without '#':"

#Feb
#Mar
#Apr
#May
#Jun
#Jul
#Aug"

month = "%s\n%s\n%s\n%s\n%s\n%s\n%s\n"
print month % ("Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug")

"Make a multiline comment using '\"""', then use that to print: \""""

#There's something going on here.
#With the three double-quotes.
#We'll be able to type as much as we like.
#Even 4 lines if we want, or 5, or 6.

"""
ksfj
dkövlsd
"""







