'''

    Non-OOP

    Bank Account Simulation 5 - List of Account Dictionaries
        In this version, is created a list of accounts, where each account
        (each element of this list) is a dictionary that looks like this:

        {'name':<someName>, 'password':<somePassword>, 'balance':<someBalance>}

'''

accountsList = []


def newAccount(aName, aBalance, aPassword):
    global accountsList
    newAccountDict = {'name': aName, 'balance': aBalance,
                      'password': aPassword}
    accountsList.append(newAccountDict)


def show(accountNumber):
    global accountsList
    print('Account', accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print('       Name', thisAccountDict['name'])
    print('       Balance:', thisAccountDict['balance'])
    print('       Password:', thisAccountDict['password'])
    print()


def getBalance(accountNumber, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None
    return thisAccountDict['balance']


def deposit(accountNumber, amountToDeposit, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None

    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None

    thisAccountDict['balance'] = thisAccountDict['balance'] + amountToDeposit
    return thisAccountDict['balance']


def withdraw(accountNumber, amountToWithdraw, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None

    if password != thisAccountDict['password']:
        print('Incorrect password for this account')
        return None

    if amountToWithdraw > thisAccountDict['balance']:
        print('You cannot withdraw more than you have in your account')
        return None

    thisAccountDict['balance'] = thisAccountDict['balance'] - amountToWithdraw
    return thisAccountDict['balance']


# Create two sample accounts
print("Joe's account is account number:", len(accountsList))
newAccount("Joe", 100, 'soup')

print("Mary's account is account number:", len(accountsList))
newAccount("Mary", 12345, 'nuts')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()

    if action == 'b':
        print('Get Balance:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        userAccountNumber = input('Please enter the account number: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        newBalance = deposit(userAccountNumber, userDepositAmount,
                             userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

    elif action == 'n':
        print('New Account:')
        userName = input('What is your name? ')
        userStartingAmount = input('What is the amount of your\
                                    initial deposit? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What password would you like to use for this\
                             account? ')

        userAccountNumber = len(accountsList)
        newAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)

    elif action == 's':  # show all
        print('Show:')
        nAccounts = len(accountsList)
        for accountNumber in range(0, nAccounts):
            show(accountNumber)

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')

        newBalance = withdraw(userAccountNumber, userWithdrawAmount,
                              userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

print('Done')


'''

This cleans things up quite a bit, making the organization of the data
more logical. But each of the functions in the program must still have access
to the global list of accounts. As we'll see in the next section, granting
functions access to all account data raises potential security risks. Ideally,
each function should only be able to affect the data of a single account.

Common Problems with Procedural Implementation:
    The examples shown in this chapter share a common problem: all the data
    the functions operate on is stored in one or more global variables. For the
    following reasons, using lots of global data with procedural programming is
    bad coding practice:
        1.  Any function that uses and/or changes global data cannot easily be
            reused in a different program. A function that accesses global
            data is operating on data that lives at a different (higher) level
            than the code of the function itself. That function will need a
            global statement to access this data. You can't just take a
            function that relies on global data and reuse it in another
            program; it can only be reused in a program with similar global
            data.

        2.  Many procedural programs tend to have large collections of global
            variables. By definition, a global variable can be used or changed
            by any piece of code anywhere in the program. Assignments to global
            variables are often widely scattered throughout procedural
            programs, both in the main code and inside functions. Because
            variable values can change anywhere, it can be extremely difficult
            to debug and maintain programs written this way.

        3.  Functions written to use global data often have access to too much
            data. When a function uses a global list, dictionary, or any other
            global data structure, it has access to all the data in that data
            structure. However, typically the function should operate on only
            one piece (or just a small amount) of that data. Having the ability
            to read and modify any data in a large data structure can lead to
            errors, such as accidentally using or overwriting data that the
            function was not intended to touch.


'''
