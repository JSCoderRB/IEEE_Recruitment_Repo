# Code 1 of task 1 - prints a pattern of stars in the specified manner

patternLength = 6 # Value of maximum number of stars in the last line

for n in range(patternLength) :           # n counts the line number
    for x in range(patternLength-(n+1)) : # x counts the spaces
        print(' ', end = '')
    for y in range(n+1) :                 # y counts the stars
        print('*', end='')
    print('')                             # For going to a new line