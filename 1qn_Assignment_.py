# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.



# sample input: 10

# sample output: 35


def fun():
    num = int(input("Enter any number:"))
    add_25 = lambda a : a + 25 
    print(add_25(num))
fun()

