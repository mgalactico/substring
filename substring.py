# Prints longest substring in which letters appear in alphabetical order
s = 'azcbobobegghakl'
n = len(s)
i = 1
currentString = ''
largestString = s[i - 1] # initializes string to first char in string
currentLetter = ''
nextLetter = ''

# Loop over length of s
while i < n:

    currentLetter = s[i - 1]
    nextLetter = s[i]

    # Loop to build substring
    while nextLetter >= currentLetter:
        if len(currentString) == 0: # Begin of currentString
            currentString = currentLetter + nextLetter
        elif len(currentString) != 0: # Grow currentString
            currentString = currentString + nextLetter

        if (i + 1) < n: # counter is only increased if within boundaries of s's length
            i += 1
            currentLetter = s[i - 1]
            nextLetter = s[i]
        else:
            break

    # Compares two strings and replaces one with other
    if len(currentString) > len(largestString):
        largestString = currentString

    # resets current string and increases counter to move to next character
    currentString = ''
    i += 1

# print largest string
print('Longest substring in alphabetical order is:', largestString)
