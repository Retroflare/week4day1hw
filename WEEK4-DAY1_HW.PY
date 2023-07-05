# write this code: The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

# Input
# Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

# Output
# Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

# Example
# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

def categorize_members(members):
    result = []
    for member in members: #O(n)
        age, handicap = member[0], member[1]
        if age >= 55 and handicap > 7:  #O(1) 
            result.append("Senior")
        else:
            result.append("Open") #O(1) 
    return result



# Example usage:
input_data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = categorize_members(input_data)
print(output)


# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).


def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False #O(1)

    if a + b > c and a + c > b and b + c > a:
        return True  #O(1)

    return False  



# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# Note: The function accepts an integer and returns an integer.

def square_digits(num): #O(d)
    result = ""
    for digit in str(num):
        square = int(digit) ** 2
        result += str(square)
    return int(result)




# fire works


import random

def create_show(fireworks, show_time):
     fireworks.sort()  # O(n log n),
    show = []

    remaining_time = show_time


    while remaining_time > 0 and fireworks:

           # Select a random firework

           firework = random.choice(fireworks) #O(1)


           if firework <= remaining_time:

               # Add the firework to the show

               show.append(firework) #O(n)

               remaining_time -= firework

          else:

              # This firework is too long, remove it from consideration

              fireworks.remove(firework) #O(n)

  return show
