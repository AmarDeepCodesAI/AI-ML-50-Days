# List
# A Python List is an ordered, mutable collection that can 
# store multiple items of different data types. 
# Lists are created using square brackets [].
students = ["Amar", "Rahul", 5, 5.2, True]

print("List->",students)  # Output: ['Amar', 'Rahul', 5, 5.2, True]


# Ordered
# Mutable (can change values)
# Allows duplicates
# Can store different data types
# Uses square brackets []


# Tupple

# A Tuple is an ordered, immutable collection in 
# Python that can store multiple values. Tuples are created using parentheses () 
# and are generally used when data should not be modified after creation.

teacher = ("40","amar", 5, 5.5, False,5,"amar")

print("Tuple->",teacher)  # Output: ('40', 'amar', 5, 5.5, False, 5, 'amar')

# Ordered
# Faster than List
# Allows Duplicates
# Cannot Change Values (Immutable)
# Cannot Add/Remove Items

# String
# A String is a sequence of characters enclosed in single quotes (' '),
# double quotes (" "), or triple quotes (''' ''' or """ """).
# Strings are immutable, meaning they cannot be changed after they are created.
greeting = "Hello, World!"

print("String->",greeting)  # Output: Hello, World!


#Set
# A Set is an unordered collection of unique items in Python.
# Sets are created using curly braces {} or the set() constructor.
# Set Does Not Support Indexing means it give error
# when we try to access element by index
# e.g. fruits[0] will give error because set does not support indexing.
fruits = {"apple", "banana", "orange", "apple"}
print("Set->",fruits)  # Output: {'banana', 'orange', 'apple'}

# Dictionary
# A Dictionary is an unordered collection of key-value pairs in Python.
# Dictionaries are created using curly braces {} with key-value pairs separated by colons (:).
# Each key must be unique, but values can be duplicated.
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "name": "Bob",  # Duplicate key, will overwrite previous value
    "name":"Amar Deep"
}
print("Dictionary->",person)  # Output: {'name': 'Bob', 'age': 30, 'city': 'New York'}

print("Keys->",person["name"])  # Output: dict_keys(['name', 'age', 'city'])