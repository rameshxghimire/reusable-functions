""" 
This function takes a number as an argument and generates a febonacci 
sequence of numbers upto that number as a list. For example if you pass 100 as 
the argument, it will generate a list called flist as [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
"""


def febo_list_gen(num):
    flist = []          # Assigning an empty list for flist variable.
    num = int(num)      # Converting the number into whole numbers/ integera.
    x, y = 0, 1
    while x < num:
        x, y = y, y + x
        if x < num:
            flist.append(x)
    print(flist)
