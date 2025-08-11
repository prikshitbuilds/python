password= input("Enter Password")

pass_len = len(password)

if pass_len <6:
    print('Weak Pass')
elif 6<=pass_len<10:
    print('Medium Strength')
else:
    print('Strong password')