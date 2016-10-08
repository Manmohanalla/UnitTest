import argparse

val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def main(input):
    string = input
    string = string.upper()
    total = 0
    while string:
        if len(string) == 1 or val[string[0]] >= val[string[1]]:
            total += val[string[0]]
            string = string[1:]
            print 'total: %s' %total,'string: %s' %string
        else:
            total += val[string[1]] - val[string[0]]
            string = string[2:]
            print 'total: %s' %total,'string: %s' %string
    print total

main('ixxx')

