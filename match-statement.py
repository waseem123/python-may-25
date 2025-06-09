print("1. Idli - INR. 40")
print("2. Biryani - INR. 140")
print("3. Dosa - INR. 70")
print("4. Kebab - INR. 130")
print("5. Lollipop - INR. 120")
choice = int(input("ENTER YOUR CHOICE - "))

match choice:
    case 1:
        quantity = int(input("ENTER QUANTITY OF IDLI - "))
        bill = quantity * 40
        print(f'YOUR BILL FOR {quantity} IDLI(s) IS INR.{bill}')
    case 2:
        quantity = int(input("ENTER QUANTITY OF BIRYANI - "))
        bill = quantity * 140
        print(f'YOUR BILL FOR {quantity} BIRYANI(s) IS INR.{bill}')
    case 3:
        quantity = int(input("ENTER QUANTITY OF DOSA - "))
        bill = quantity * 70
        print(f'YOUR BILL FOR {quantity} DOSA(s) IS INR.{bill}')
    case 4:
        quantity = int(input("ENTER QUANTITY OF KEBAB - "))
        bill = quantity * 130
        print(f'YOUR BILL FOR {quantity} KEBAB(s) IS INR.{bill}')
    case 5:
        quantity = int(input("ENTER QUANTITY OF LOLLIPOP - "))
        bill = quantity * 120
        print(f'YOUR BILL FOR {quantity} LOLLIPOP(s) IS INR.{bill}')
    case _:
        print("WRONG INPUT! PLEASE SELECT THE OPTION BETWEEN 1 TO 5")