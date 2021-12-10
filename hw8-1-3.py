# MEE 12/09/21

def sorting(my_string):
    my_lst = list(my_string)
    sorted_lst = my_lst.copy()
    sorted_lst.sort()

    if sorted_lst == my_lst:
        print("This list isnt sorted.")
    else:
        print("This list isnt sorted.")


sorting("abcd")
sorting("zyx")
sorting("efg")