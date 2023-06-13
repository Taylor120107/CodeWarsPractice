def order_food(lst):
    options_count = {}
    for dev in lst:
        meal = dev['meal']
        if meal in options_count:
            options_count[meal] += 1
        else:
            options_count[meal] = 1
    return options_count

#the above function creates an empty dictionary to store the count each food option from array 
#You are able to iterate over each object within dev and lst array.
#You can extract the meal option using dev['meal'] and check whether it already exists as a key in the options_count dictionary
# if it does the ciunt increments by 1 if not its added as a new key with an initial count as 1
#then finally the options_coun t is returned to the dictionary
# list1 = [
#     { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian' },
#     { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard' },
#     { 'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan' },
#     { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian' },
# ]
