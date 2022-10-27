'''

    Non-OOP

    Bank Account Simulation 1 - Single Account Without Functions
        Note that these program is not production-ready; invalid user entries
        or misuse will lead to errors. The intent is to have you focus on how
        the code interacts with the data associated with one or more bank
        accounts.
        To start, consider what operations a client would want to do with a
        bank account and what data would be needed to represent an account.

    A list of operations a person would want to do with a bank account would
    include:
        - Create (an account)
        - Deposit
        - Withdraw
        - Check balance

    Next, here is a minimal list of the data we would need to represent a
    bank account:
        - Customer name
        - Password
        - Balance


'''

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()

    if action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter the password: ')
        if userPassword != accountPassword:
            print('Incorrect password')
        else:
            print('Your balance is:', accountBalance)

    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        if userDepositAmount < 0:
            print('You cannot deposit a negative amount!')
        elif userPassword != accountPassword:
            print('Incorrect password')
        else:  # OK
            accountBalance = accountBalance + userDepositAmount
            print('Your new balance is:', accountBalance)

    elif action == 's':  # show
        print('Show:')
        print(' Name', accountName)
        print(' Balance:', accountBalance)
        print(' Password:', accountPassword)
        print()

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')

        if userWithdrawAmount < 0:
            print('You cannot withdraw a negative amount')
        elif userPassword != accountPassword:
            print('Incorrect password for this account')
        elif userWithdrawAmount > accountBalance:
            print('You cannot withdraw more than you have in your account')
        else:  # OK
            accountBalance = accountBalance - userWithdrawAmount
            print('Your new balance is:', accountBalance)

'''

All the actions are at the main level; there are no functions in the code.
The program works fine, but it may seem a little long. A typical approach
to make longer programs clearer is to move related code into functions and
make calls to those functions.

'''
