import time
print("PLEASE INSERT YOUR CARD")
time.sleep(3)
password = 2005
pin = int(input("ENTER YOUR ATM PIN "))
balance = 78000
if pin == password:
    while True:
        print("""      
                        1 == balance
			2 == withdraw balance
			3 == deposit balance
			4 == exit
			""")
        try:    
            option = int(input("PLEASE ENTER YOUR CHOICE "))
        except:
            print("PLASE ENTER VALID OPTION")
        if option == 1:
            print(f"YOUR CURRENT BALANCE IS {balance}")                                    
        if option == 2:
            withdraw_amount = int(input("PLASE ENTER YOUR WITHDRAW AMOUNT "))   
            balance = balance - withdraw_amount
            print(f"{withdraw_amount} IS DEBITED FROM YOUR ACCOUNT")    
            print(f"YOUR UPDATED AMOUNT IS {balance}")        
        if option == 3:
            deposit_amount = int(input("PLEASE ENTER YOUR DEPOSIT AMOUNT"))
            balance = balance + deposit_amount          
            print(f"{deposit_amount} IS CREDITED FROM YOUR ACCOUNT")
            print(f"YOUR UPDATED BALANCE IS {balance}")
        if option == 4:
            break
else:
    print("WRONG PIN TRY AGAIN")
