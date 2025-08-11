grade=101

if grade>=101:
    print("Invalid grade")
    exit()

if 90<=grade<=100:
    print("grade A")
elif 80<=grade<=89:
    print("grade B")
elif 70<=grade<=79:
    print("grade C")
elif 60<=grade<=69:
    print("grade D")
else:
    print("grade F")