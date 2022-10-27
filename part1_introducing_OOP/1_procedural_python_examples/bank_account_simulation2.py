'''

    Non-OOP

    Bank Account Simulation 2 - Single Account with Functions
        In the version of the program in Listing 1-3, the code is broken up
        into separate functions, one for each action. Again, this simulation
        is for a single account.

'''

accountName = ''
accountBalance = 0
accountPassword = ''


def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password


def show():
    global accountName, accountBalance, accountPassword
    print(' Name', accountName)
    print(' Balance:', accountBalance)
    print(' Password:', accountPassword)
    print()


def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Incorrect password')
        return None
    return accountBalance


def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None
    if password != accountPassword:
        print('Incorrect password')
        return None

    accountBalance = accountBalance + amountToDeposit
    return accountBalance


def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None

    if password != accountPassword:
        print('Incorrect password for this account')
        return None

    if amountToWithdraw > accountBalance:
        print('You cannot withdraw more than you have in your account')
        return None

    accountBalance = accountBalance - amountToWithdraw
    return accountBalance


newAccount("Joe", 100, 'soup')  # create an account

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
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

    elif action == 'w':
        print('Withdraw:')
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')

        withdraw(userWithdrawAmount, userPassword)

    elif action == 's':
        show()

    elif action == 'q':
        break


# Snip calls to appropriate functions
print('Done')


'''

As a general programming tenet, functions should never modify global
variables. A function should only use data that is passed into it, make
calculations based on that data, and potentially return a result or results.
The withdraw() function in this program does work, but it violates this rule by
modifying the value of the global variable accountBalance (in addition to
accessing the value of the global variable accountPassword).

'''
