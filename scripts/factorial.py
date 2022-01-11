#!/usr/bin/python


##1. Calculate factorial using recursion.
##2. Call factorial function using thread. 


from threading import Thread

threadId = 1


def factorial(n):
   global threadId
   if n < 1:   # base case
       print("%s: %d" % ("Thread", threadId ))
       threadId += 1
       return 1
   else:
       returnNumber = n * factorial( n - 1 )  # recursive call
       print(str(n) + '! = ' + str(returnNumber))
       return returnNumber

Thread(factorial,(5, ))
Thread(factorial,(4, ))

c = input("Waiting for threads to return...\n")
