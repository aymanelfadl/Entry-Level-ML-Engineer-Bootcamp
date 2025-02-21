import sys

def whois():
    argvLen = len(sys.argv)
    if argvLen == 2:
        try:
            if int(sys.argv[1]) % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except ValueError as e:
            print("AssertionError:" + str(e))
    elif argvLen > 2:
        print("AssertionError: more than one argument is provided")


whois()
