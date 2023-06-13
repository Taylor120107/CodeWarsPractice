def disemvowel(string_):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    return ''.join(char for char in string_ if char not in vowels)

input_string = "Hello, World!"
result = disemvowel(input_string)
print(result)

# In this function, we define a string vowels that contains all the vowels in both lowercase and uppercase. We then use a list comprehension and the join method to iterate over each character in the input string. 
# If the character is not found in the vowels string, it is included in the final result.