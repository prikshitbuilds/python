userage=24
day='Tuesday'

price = 12 if userage>=18 else 8

if day == 'Wednesday':
    price=price-2


print("Ticket price for you is $",price)