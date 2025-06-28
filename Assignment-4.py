# Assignment 4 : Hands on Python Data Structures

# Task 1

fruits = ['apple', 'pear', 'blueberry', 'pineapple', 'watermelon']
print("Original list: ", end="")
print(fruits)

fruits.append('mango')
print("After adding a fruit: ", end="")
print(fruits)

fruits.remove('apple')
print("After removing a fruit: ", end = "")
print(fruits)

print("Reversed list: ", end="")
print(fruits[::-1])

# Task 2

info = {"name":"Claire", "age": 23, "city": "Austin"}
info["favorite color"] = "blue"
info["city"] = "New York"

print("Keys:", end="")
for key in info.keys():
    print(key, end=" ")

print()

print("Values: ", end="")
for value in info.values():
    print(value, end=" ")

print()


# Task 3
favs = ('Lion King', 'Love Again', 'A Little Life')
print("Length of tuple: ", len(favs))
