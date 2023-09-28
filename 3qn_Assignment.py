# Write a Python program to square the elements of a list using map() function.

# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# # [16, 25, 4, 81]

def square_lst():
    lst = [4,5,2,9]
    square_lst = list(map(lambda lst : lst **2 ,lst))
    print(square_lst)

square_lst()