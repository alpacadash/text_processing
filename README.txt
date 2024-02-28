 Part A: Word Frequencies

Write a program that takes a file name as a command line argument, read this text file, tokenize it, count the tokens, and print out the token (word) frequencies. You can use the following methods as an example (you are not required to use these specific methods):

Method/Function: List<Token> tokenize(TextFilePath)
Write a method/function that reads in a text file and returns a list of the tokens in that file. For the purposes of this project, a token is a sequence of alphanumeric characters, independent of capitalization (so Apple, applE and aPPle are the same token "apple").
Method:        Map<Token,Count> computeWordFrequencies(List<Token>)
Write another method/function that counts the number of occurrences of each token in the token list.

Method:         void print(Frequencies<Token, Count>)
Finally, write a method that prints out the word frequency counts onto the screen. The print out should be ordered by decreasing frequency. (so, highest frequency words first). Resolve ties alphabetically and in ascending order.

Here is an example if input/output:

Input :

Here's a fun-fact! White tigers live mostly in "India".

Wild lions mostly live in "Africa".

Output:

in	2
live	2
mostly	2
a	1
africa	1
fact	1
fun	1
here	1
india	1
lions	1
s	1
tigers	1
white	1
wild	1
 

Each line of the output should use "[token]\t[frequency]" formatting where you need to replace [token] with the token name and [frequency] with the token frequency. For example, if you have two tokens: hello with frequency 1 and world with frequency 2, the output should be:

world\t2
hello\t1

Note that "\t" will be changed to a tab (couple of spaces) when printed on the console.

 

Part B: Intersection of two files

Write a program that takes two text files as command line arguments and outputs the number of tokens they have in common. Here is an example of input/output:

Input file 1:

We  reviewed the trip and credited the cancellation fee. The driver has been notified.

Input file 2:

If a trip is cancelled more than 5 times after the driver-partner has confirmed the request, a cancellation fee will apply.

Output:

6

You can reuse code you wrote for part A.
Common Tasks

For both part A and part B, please add a brief runtime complexity explanation for your code as a comment on top of each method or function (does it run in linear time relative to the size of the input? Polynomial time? Exponential time? ). This explanation and your code's actual conformance with this explanation will be the basis for evaluating the performance of your program.
You should get the file names from command line arguments. Do not hard code the input file names in your code or read them from system standard input (stdin). As the assignment will be graded using an automatic grader, not doing this will result in losing the whole credit for the assignment.
Exception handling is required for bad inputs. An example of bad input would be a character in a non-english language. Your code should be able to tokenize the whole input file even though there may be some bad inputs in it. You should be able to skip the bad input and continue with the rest. If your code throws an exception in the middle of tokenizing a TA's input test case, you will lose the whole credit for that test case.
Submitting Your Assignment

Your submission should be a single zip file containing two programs, one for part A, the other for part B. Something like this:

Assignment1.zip
------------ PartA.py
------------ PartB.py

Submit it to Canvas.

You can replace Assignment1 with whatever name you think is appropriate. You don't need to add your UCInetID or student number to the zip file name. Canvas will do that automatically when we are downloading your assignments. Do not zip the directory containing these two files! So the following examples are not a correct structure:

Assignment1.zip
------------ Assignment 1
------------------------ PartA.py
------------------------ PartB.py

Assignment1.zip
------------  PartA
------------------------ PartA.py
------------ PartB
------------------------ PartB.py