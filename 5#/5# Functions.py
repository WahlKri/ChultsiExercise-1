"""
 Chapters 18-21
"""

"Names, Variables, Code, Functions"

"""
    First of all now you maybe notice this new file structure and from this point on we are going to use
     following:
        Directory number# (directory) will tell you what task are you working on. 'Source_Material'-folder
        will have everything you need to complete exercises. REMEMBER TO CHECK THAT YOU ARE WORKING WITH
        RIGHT EXERCISE! :) There are always .py-files which are usually the main files to be worked with (unless
        told otherwise).
        Those are usually called something like 'number# andTheSubject'. For example today we have this kind of
        structure:

        5#--------------------------------|
            Source_Material---------------|
                            lorem_ipsum.txt
            5# Functions.py

     So, lets start!

     1. What is a function?
     2. What can they do?
     3. Study this basic structure of a non returnable function: (!)

        def nameOfYourFunction(arguments):
            whatToDoWithIt

     4. That was called pseudo-code, it means a code which was just made for explaining something.
     5. To def a function, use the name of your very own function like this (note the indentation):

        def helloworld():
            print ("Hello world")

    6. To call it use the name

        helloworld()

    7. What is the difference between def and calling the function?
    8. Feel free to test above function by copy-pasting.
    9. helloworld()-function was called as non-parametric function. Next we are going to make A PARAMETRIC FUNCTION
        for example print() function is a parametric function. Parametric functions need to be supplied with data:

        // creating it for later use

        def shownumber(number):
            number = number +1
            print(number)

        // and to call it we just write for example

        shownumber(5)

    10. What happened and why?
    11. Ok now you are next. Make a function that takes two arguments (synonym for parameter) name and age.
        The function prints out greeting "Hi 'name', nice to meet you. Oh, you also were born in 1992!"
        Your function should work with call 'greeting("Kristian",21). Hint: you can calculate estimated year
        by 2014 - age.
    12. Top tips when writing functions:

        Did you start your function definition with def?
        Does your function name have only characters and _ (underscore) characters?
        Did you put an open parenthesis ( right after the function name?
        Did you put your arguments after the parenthesis ( separated by commas?
        Did you make each argument unique (meaning no duplicated names)?
        Did you put a close parenthesis and a colon ): after the arguments?
        Did you indent all lines of code you want in the function four spaces? No more, no less.
        Did you "end" your function by going back to writing with no indent (dedenting we call it)?

        Did you call/use/run this function by typing its name?
        Did you put the ( character after the name to run it?
        Did you put the values you want into the parenthesis separated by commas?
        Did you end the function call with a ) character?


"""

"Functions and Variables"

"""

    Functions are really flexible. You can perform different calculations with the arguments. For example
    we can create variables and use them as function arguments, or just input the arguments directly, or combine
    both! As you can see function arguments actually works like normal variables. Let's start with the first.

    Our function:

      def add_together(first,second):
        print (first+second)

    Variable way:

        a = 10
        b = 20

        add_together(a,b)

    Direct way #1:

        add_together(int(input("a: ")),int(input("b: ")))

    Direct way #2:

         add_together(5,10)


    Math way #1:

        add_together(5+2,10*2)

    Combined way:

        a = 3
        b = 2

        add_together(a*2,b*b)



    1. Make a function called repeater that takes two arguments: 'word' and 'n'. It multiplies (*) words to n and prints
        out the word n-times. For example call 'repeater("Jultsi",5)' should print:

        'JultsiJultsiJultsiJultsiJultsi '

    2. Make two variables first_name and last_name. Then make a function called shout which should take two arguments:
        firstname and lastname. The function should capitalize both of those words and print them. For example

        shout("Kristian","Wahlroos") should print: 'HI KRISTIAN WAHLROOS!'

        Hint: Cast first the variable to string (str). Then use the method str(your_variable).upper() to make the whole
        word capitalized. Find out also what other methods str. keeps inside.

    3. Do the 2. task again but now with user input.
        - Prompt and save results to variables
        - call the function shout with those variables.
        - ????
        - enjoy your new function! ^^

    4. Answer:

        Is there a way to analyze what this function is doing so I can understand it better?
        What if I want to ask the user for the numbers?
        Is it bad to have global variables with the same name as function variables? Why?
        Is there a limit to the number of arguments a function can have?
        Can you call a function within a function?



"""

"Functions and Files"

"""


"""