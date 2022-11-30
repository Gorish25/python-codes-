
def romanToInt(s):
    
    # dictionary of roman numerals
    roman_map={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    #length of given string
    n=len(s)

    #this variable will store the last element of the string
    num=roman_map[s[n-1]]

    # loop through for each character from right to left
    for i in range(n-2,-1,-1):
        # checks if the character at left is bigger or smaller than right position character
        if roman_map[s[i]]>= roman_map[s[i+1]]: 
            num+=roman_map[s[i]]
        else:
            num-=roman_map[s[i]]
    return num

number=input("Enter the number")
print(f'The number for {number} is {romanToInt(number)}')