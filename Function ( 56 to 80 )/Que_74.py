def even_checker():
    list_of_number = [45, 22, 11, 3, 6, 19, 28, 37, 40, 49]
    for i in list_of_number:
        if i % 2 == 0:
            print(f"{i} is even number")
        else:
            print(f"{i} is odd number") 


even_checker()