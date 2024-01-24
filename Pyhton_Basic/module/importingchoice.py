import sys

bal = 2

if len(sys.argv) < 2:
    sys.exit('too few argument')


for arg in sys.argv[1:-1]:
    print('hello my name is ' , arg)

