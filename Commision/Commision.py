#this program calculates sales commissions and sums the total of all sales commissions the user has entered

print("Welcom to the program sales commission loop")

keep_going='y'

total=0
while keep_going=='y':

    #get a salespersons sales and commission rate
    sales=float(input('Enter the amount of sales: '))
    comm_rate=float(input('Enter commission rate: '))

    #calculate the commission
    commission=sales*comm_rate

    print("commission is",commission)

    keep_going=input('Enter y for yes: ')

    total=total+commission
    print("Total is",total)

print("You have exited the program. Thet total is",total)