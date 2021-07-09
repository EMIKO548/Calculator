'''
File Name: Emikookoturo_CodingPractices_Practical_Answers.py
Author:    Emiko Okoturo
Date Created: 9 July 2021
Date Last modified: 9 July 2021
Version: 0.0.1
Copyright: c Emiko Okoturo.
Purpose of Calculator: To implement arithnetical operations.'''



import math
import time

# Define and add integers to substitute into the variables

def add(x,y):
  return x + y

def subtract(x,y):
  return x - y

def divide(x,y):
  return x / y

def multiply(x,y):
  return x * y

def sqrt(x):
  if math.sqrt(x) * math.sqrt(x):
     return False
  else:
     return math.sqrt(x)


def power(x,y):
  return math.pow(x,y)

# decisions to select options in the calculating program

def repeat():
  print('Would you like to perform another calculation? y/n')
  rep = input('')
  if rep.lower() == 'y':
     time.sleep(0.5)
     main()
  elif rep.lower() == 'n':
     print('Goodbye!')
     time.sleep(1)
     exit()
  else:
     print('Please enter y/n.')
     time.sleep(1)
     repeat()


# checking and capturing errors in the calculating program 

def numCheck(x):
  try:
     int(x)
  except ValueError:
     print("Please enter a valid number.")
     print('')
     time.sleep(1)
     main()


def choiceCheck(y, z):
   for x in y:
       if x == z:
           return True
           break
       else:
           pass


# Defining choices and selecting printing calculating options 

def main():
  choices = ['1', '2', '3', '4']
  print('Choose your operation: ')
  print('1. Add')
  print('2. Subtract')
  print('3. Divide')
  print('4. Multiply')
  print('5. Square Root')
  print('6. Exponent')
  print('1/2/3/4/5/6')
  choice = input('')
  if choice == '5':
     print('Please choose the number you would like to square root.')
     rt = input('')
     numCheck(rt)
     rt = int(rt)
     rts = sqrt(rt)
     if rts == False:
        print('%d is an irrational number.' % (rt))
     else:
        print('The square root of %d is %d' % (rt, rts))
        repeat() 
  elif choice == '6':       
     print('Choose the number you would like to raise to a power: ')
     base = input('')
     numCheck(base)
     base = int(base)
     print('')
     print('Now please choose the indice: ')
     ind = input('')
     numCheck(ind)
     ind = int(ind)
     time.sleep(1)
     print('%d to the power of %d is %d' % (base, ind, power(base,ind)))
     repeat()
  elif choiceCheck(choices, choice) != True: 
     print('Please choose a valid number.')
     print('')
     time.sleep(1)
     main()
  a = input('Please choose your first number: ')
  numCheck(a)
  a = int(a)
  print('')
  b = input('Please choose your second number: ')
  numCheck(b)
  b = int(b)
  if choice == '1':
     print('%d + %d = %d' % (a, b, add(a,b)))
  elif choice == '2':
     print('%d - %d = %d' % (a, b, subtract(a,b)))
  elif choice == '3':
     print('%r / %r = %r' % (a, b, divide(a,b)))
  elif choice == '4':
     print('%d * %d = %d' % (a, b, multiply(a,b)))
  else:
     print('Please choose a valid number')
     print('')
     time.sleep(1)
     main()
  repeat()


main()