# "Return the number(count) of vowels in the given string.

# We will consider a, e, i, o, and u as vowels(but not y).

# The input string will only consist of lowercase letters and / or spaces.

# ex:
# solution('hello_world') = > 3"

def solution(a_string):
    # write your code here
    vowels = set('aeiou')
    vowel_count = 0
    
    for char in a_string:
        if char.lower() in vowels:
            vowel_count +=1
    return vowel_count

print(solution('hello_world'))
        
# print(solution('hello_world')
