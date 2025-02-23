def invest(amount, rate, years):
    annual = 0
    for i in range (1, years+1):
        annual = amount * (rate)
        amount += annual
        print("year", i, ":", f"{amount:.2f}")

principal = int(input("Enter the principal amount: "))
rate = float(input("Enter the annual rate: "))
years = int(input("Enter the years: "))
invest(principal, rate, years)