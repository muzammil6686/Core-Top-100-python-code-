def pages():
    list = []
    for i in range(7):
        pages = int(input("Enter number of pages in book"))
        list.append(pages)
        page = sum(list)
    print("Total number of pages in book:", page)

pages()