# This is the function definition
def is_anagram(s1, s2):
    print('Call the function is_anagram')

s1 = 'silent'
s2 = 'listen'
# This is the function call, notice that s1 and s2 are variables that are pointing to a value
# Here we call the function
is_anagram(s1, s2)

# Which is different than
is_anagram  # this does not do anything since it is not called (what do we need to *call* or *execute* a function?)

# can you tell the difference between is_anagram(s1, s2) and is_anagram?
# is_anagram is just the *name* of the function
# We print it:
print("We print the name of the function", is_anagram)

# the bracket *()* are used to execute/call something (for exemple here the function).
# In which other context would you need brackets to execute something?
# When we create a class template, for example *class Rectangle: pass*, we need to execute the contructor *Rectangle* to create an object from it
# For example:
class Rectangle:
    pass

r1 = Rectangle()  # we use the bracket to call the constructor of the class, to construct/instantiate/create an object/instance
# notice the difference between *class* and *object*
print("We print the representation of the class", Rectangle)
print("We print the representation of the object/instance",Rectangle())


# I can attach attribute to the object:
r1.some_attribute = "my object attribute"

# I can also attach an attribute to the Class:
Rectangle.some_class_attribute = "my class attribute"

# In python, everything is object, notice that I can also attach an attribute to a function:
is_anagram.som_function_attribute = "my function attribute"

# I access my attributes of each object, the rectangle object, the class object, the function object
print("my object attribute is ", r1.some_attribute)
print("my class attribute is ", Rectangle.some_class_attribute)
print("my function attribute is ", is_anagram.som_function_attribute)