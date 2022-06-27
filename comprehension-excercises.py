#Problem 1

#This is a classic problem given in technical interviews. First solve the problem WITHOUT using list comprehension.
#"Write a program that prints the numbers from 1 to 100. For multiples of three print "Fizz" instead of the number. For Multiples of five print "Buzz". Finally, for numbers which are multiples of both three and five print "FizzBuzz".
#Include comments for each step of your script explaining the Pseudo code/what each line is doing.
lst=[('Fizz' if item % 3 ==0 )for item in range(1,101)]

#After you have solved it, write a second version of your script using list comprehension.
lst1=[]
for num in range(1,101):
    if num % 3 ==0:
        lst1.append('Fizz')
    else:
        lst1.append(num)