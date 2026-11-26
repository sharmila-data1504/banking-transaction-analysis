user_details={'yaazhu':['yaazhu@123',1000,1234],'sharmi':['sharmi@234',500,5678]}
print('\t\t\t\t WELCOME TO NPS BANK')
print('*'*100)
print("\t1.login\n\t2.Signup\n\t")
type=input('choose what you need to do:')
if type == '1':
    while True:
        user_name = input('Username:')
        pwd = input('Password: ')
        if user_name in user_details and user_details[user_name][0] == pwd:
           print('Login Successful')
           break 
    while True:
        print("\t1.Deposit\n\t2.Withdraw\n\t3.Balance Check\n\t4.Exit")
        option_type=int(input('Choose The Option:'))
        if option_type == 1:
            pin = int(input('enter the pin: ')) 
            if user_details[user_name][2] == pin:
                print('Correct PIN')
                amount=int(input('Enter the amount:'))
                if amount > 0:
                    user_details[user_name][1]=user_details[user_name][1]+amount
                    print('Deposit done successfully')
                else:
                    print('Deposit is not done successfully')
            else: 
                print('Incorrect PIN')
        elif option_type == 2:
            pin = int(input('enter the pin: '))
            if user_details[user_name][2] == pin:
                print('Correct PIN')
                amount=int(input('Enter the amount:'))
                if amount > 0 and amount < user_details[user_name][1]:
                   user_details[user_name][1]=user_details[user_name][1]-amount
                   print('Withdraw done successfully')
                else:
                   print('Withdraw is not done successfully')
            else:
                print('Incorrect PIN')
        elif option_type == 3:
            pin = int(input('Enter the pin: '))
            if user_details[user_name][2] == pin:
                print('Correct PIN')
                bank_balance=user_details[user_name][1]
                print(f'Your bank balance:{bank_balance}')
            else:
                print('Incorrect pin')
        elif option_type == 4:
            print('Thank You For Using NPS Bank')
            break
        else:
            print('Invalid option')
    else:
        print('Invalid username or password')              
elif type == '2':
     while True:
       user_name = input('username: ')
       if user_name in user_details:
        print('User name already exists')
       else:
           break
     while True:
            pwd = input('password: ')
            upper = 0
            lower = 0
            number = 0
            special = 0
            for i in pwd:
                if i.isupper():
                    upper = upper + 1
                elif i.islower():
                    lower = lower + 1
                elif i.isdigit():
                    number = number + 1
                else:
                    special = special + 1
            if len(pwd) >= 8 and upper >= 1 and lower >= 1 and number >= 1 and special >= 1:
                break
            print('Password should contain 8 characters, uppercase, lowercase, number and special character')
     while True:
            confirm_password = input('confirm password: ')
            if pwd == confirm_password:
                break
            print('Confirm password does not match with the password')
     while True:
            pin = input('Enter the pin: ')
            if len(pin) == 4 and pin.isdigit():
                break
            print('Pin should be 4 digits')
     while True:
            confirm_pin = input('Confirm pin: ')
            if pin == confirm_pin:
                break
            print('Confirm pin does not match with the pin')
     while True:       
            amount = int(input('Enter the amount: '))
            if amount >= 500:
               user_details[user_name] = [pwd, amount, pin]
               print(user_details)
               print('signup successfully!!!!!!!!!!')
               break
            else:
               print('minimum amount should be 500')

            
            
        
    
    
             

    


