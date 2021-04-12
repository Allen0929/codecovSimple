from __future__ import print_function
import sys

def fibonacci(n):
    if n <= 1: 
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
fibonacci(1)
fibonacci(11)

factorial(0)
factorial(1)

#def hello(what):
#    print('Hello, {}!'.format(what))


#def say_what():
#    return 'world'


#def main():
#    hello(say_what())
#   return 0


#if __name__ == '__main__':
#    sys.exit(main())

