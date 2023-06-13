def greet(name,owner):
    if name == owner:
        return "Hello Boss"
    else:
        return "Hello Guest"

name="Daniel"
owner="Daniel"

greeting=greet(name,owner)
print (greeting) 

