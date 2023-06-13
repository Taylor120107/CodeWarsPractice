def find_short(s):
    words = s.split() #split into string
    shortest_length = float('inf')
    
    for word in words:
        word_length = len(word)
        if word_length < shortest_length:
            shortest_length = word_length
    return shortest_length

#Split the string into individual words using a space as the delimiter.
# Initialize a variable shortest_length with a value of positive infinity.
# Iterate over each word in the split string.
# For each word, compare its length to the current value of shortest_length.
# If the length of the word is smaller than shortest_length, update the value of shortest_length to the length of that word.
# After iterating over all the words, the value of shortest_length will represent the length of the shortest word(s).
def find_short(s):
    return min(len(x) for x in s.split())