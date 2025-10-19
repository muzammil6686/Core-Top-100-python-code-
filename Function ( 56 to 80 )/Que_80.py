def zakat(*args):
    total_zakat = 0
    for amount in args:
        zakat_amount = amount * 0.025
        total_zakat += zakat_amount
        print(f"Zakat for {amount} is: {zakat_amount}")
    print(f"Total Zakat for all amounts is: {total_zakat}")
zakat(5000, 10000, 15000)
