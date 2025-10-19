def average_pani():
    list_of_pani = []
    for i in range(7):
        water = float(input(f"Enter pani consumed on day {i+1} in liters: "))
    list_of_pani.append(water)
    average = sum(list_of_pani) / len(list_of_pani)
    print(f"The average pani consumed in a week is {average} liters.")
average_pani()