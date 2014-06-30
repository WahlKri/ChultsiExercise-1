"""Chapters 15-17"""

"READING FILES"

"*** Extra files that comes with the project: exampleText.txt ***"

"""Reading files with Python is actually really easy. First we need to introduce yet a new function : open()

   For this exercise there is a .txt-file named 'exampleText.txt'. Open it in pyCharm and try to use open()-
   function to print its content. 
   
   1. Make a new variable.
   2. Assing the function open(filename) to that variable.
   3. Now write yourVariable and a dot. See what different functions you can use for opened file.
   4. Find at least how to see if a opened file is writable/readable, how to get the name of the file and
      the most important function read(). 
   5. Use those functions to print out the following:
   
    Name of the file: exampleText.txt
    Writable: False
    Readable: True
    
    Contents: 
    This is stuff I typed into a file.
    It is really cool stuff.
    Lots and lots of fun to have in here.
      
   6. Now do the same exercise, but use input from the user.
      Note: The files in this project works with just by name because
      Their root is project/ so they actually are /exampleText.txt.
      You still can open a file using the complete path for example:
      var = open("C:\\Users\\Ville\\Desktop\\InfoForLinux.txt")
      The output should be something like this:
   
    Give filename: exampleText.txt (user input)
    
    Name of the file: exampleText.txt
    Writable: False
    Readable: True
    
    Contents: 
    This is stuff I typed into a file.
    It is really cool stuff.
    Lots and lots of fun to have in here.
      
   7. Find out answer for these next questions: 
  
      * Does txt = open(filename) return the contents of the file?
      * What does from sys import argv mean?
      * Why is there no error when we open the file twice?
      * Should I close the file using .close() command when I'm done with the file?


"""

"READING AND WRITING FILES"

"""

Here are some useful commands to use when working with files:

close -- Closes the file. Like File->Save.. in your editor.
read -- Reads the contents of the file. You can assign the result to a variable.
readline -- Reads just one line of a text file.
truncate -- Empties the file. Watch out if you care about the file.
write(stuff) -- Writes stuff to the file.


    1. Open the file using open(filename, 'w'). Remember to save it into variable!
    2. Try to figure out what 'w' does. Hint use .writable and .readable
    3. How about 'r'?
    4. Now the file is opened in write-mode. First you need to initialize it (empty it from the data). Do that.
    5. Ask from user three different lines.
    6. Write those three different files to exampleText.txt just by using one write()-function and formats.
    7. You can assume that everything we write here. We write to a exampleText.txt -file.
    8. REMEMBER TO CLOSE THE FILE AFTER USING!
    9. Finally print out the contents of that file.



    Question & thinkables:

    Is the .truncate() necessary with the 'w' parameter?
    What are the modifiers to the file modes we can use?
    Does just doing open(filename) open it in 'r' (read) mode?


"""

"MORE FILES"

"""
    Now we are going to do some file processing/copying.


    1. Import exists from os.path. With exists() you can check if a file really exists.
        The functions exists() return True or False (those are called boolean values)
    2. Ask a file from the user and check if that file exists (print it out)
    3. Open that file in read-mode and save that data to a variable. Note you can combine
        functions together. For example:

    nameOfTheFile = open("exampleText.txt").name

    4. As you can see, you can have a variable of any kind of data. Use that knowledge to use the .read()
        inside open(). So you can store all the data from the opened file to a variable. It is really good
        practise to know what kind of/type of information different functions return. We learn more about returning
        later when we deal with functions :)
    5. If that felt too hard to understand you can still use the style we have learned to open files and fetch the data:

      openedFileToReadMode = open(filename)
      dataOfTheFile = openedFileToReadMode.read()

    6. Check if the copyToHere.txt exists. That will be the file where we store the contents from the exampleText.txt
        It is really really important to check that files exists
        when we learn if-statements. It prevents the program from crashing. Or can you read a book
        that you don't have ;)

    7. Print the contents of that variable that holds the value of read() from exampleText.txt
    8. Open the copyToHere.txt to write mode. If you misspell and run the program it will create a new file.
        Don't create any extra files. That's how writing works here :P
    9. Use write()-function and write the contents of exampleText.txt TO (!!) copyToHere.txt
    10. You should now have two different whiles which both have the same contents. You can open those files
        In PyCharm to check that out (just by clicking the name).
    11. THAT IS CALLED COPYING WOO ^^
    12. oh. REMEMBER TO CLOSE THOSE FILES AFTER USING!!! >:(

    Extra & Questions:

    See how short you can make the script. The most shortest is one line (Without printing).
    What does the len() function do?
    Is it normal to feel like this exercise was really hard?
    Next lessons are going to be about functions and how to combine functions and files. YEEHAAW. Excited?


"""





