#by Christian J. Rodriguez and Michelle Bou

# BANK ACCOUNT SIMULATOR
account_name = str( input( "Name for your account: " ) )
try:
    balance = float( input( "What is your starting balance?: $" ) )
except:
    print('FOR YOUR STARTING BALANCE, YOU MUST ENTER ONLY NUMBERS')
    balance = float( input( "What is your starting balance?: $" ) )
starting_balance = balance  # this varible is use to calculate the amount of deposits doned
run = True

options = """1. Deposit some funds
2. Withdraw some funds
3. View balance 
4. Create new account
5. Quit
"""
# LOGS OF VARIABLES # LAS VECES QUE OCURRE ESA FUNCIONALIDAD
log_reward = 0
log_penalty = 0
log_deposit = 0
log_withdrawn = 0
amount_of_deposits = 0
bonus_received = 0
penalty_received = 0
successful_withdrawn = 0
unsuccessful_withdrawn = 0

while run:      #MAIN LOOP
    print( f'\tACCOUNT NAME: {account_name}\n' )
    print( options )
    try:        #MANAGE ILEGAL INPUTS
        user_choice = int( input( "/>" ) )
    except:
        print('ENTER A INTEGRER NUMBER')
        print(options)
        user_choice = int( input( "/>" ) )

    if user_choice == 1:
        try:
            user_input = float( input( 'How much you want to deposit ?: $' ) )
        except:
            print('ENTER A NUMBER')
            user_input = float( input( 'How much you want to deposit ?: $' ) )
        if user_input > balance:        # Sum the balance and 2% reward
            balance += (user_input * 1.02)      # add the balance and the reward
            balance = round(balance, 2)
            bonus_received += (user_input * 1.02) - user_input
            bonus_received = round(bonus_received, 2)
            log_deposit += 1
            log_reward = +1
            amount_of_deposits += user_input
            print( f'Your new balance is ${balance}' )
        else:       #THE DEPOSIT IS LESS THAN THE CURRENT BALANCE
            balance += user_input
            log_deposit += 1
            amount_of_deposits += user_input
            print( f'Your new balance is ${balance}' )

    elif user_choice == 2:
        try:
            user_input = float( input( "How much you want to withdraw?: $" ) )
        except:
            print('ENTER A NUMBER')
            user_input = float( input( "How much you want to withdraw?: $" ) )

        if user_input > balance:  # conditional to charge a penalty fee
            balance -= 5
            penalty_received += 5
            unsuccessful_withdrawn += user_input
            log_penalty += 1
            print("you do not have the minimum balance to be able to withdraw the money")
            print( f'Your new balance is ${balance}' )
        else:       #IF THIS RUNS, IT MEANS YOU HAVE THE SUFFICIENT BALANCE
            balance -= user_input
            successful_withdrawn += user_input
            log_withdrawn += 1
            print( f'Your new balance is ${balance}' )

    elif user_choice == 3:      #PRINT THE CURRENT BALANCE
        print( f'\tYour current balance is: ${balance}' )
    elif user_choice == 4:      #RESET ALL VARIABLES AND CREATE NEW ACCOUNT
        print( 'ALERT YOU WILL CREATE A NEW ACCOUNT AND THE PREVIUS DATA WILL BE RESETED\n' )
        account_name = str( input( "Name for your account: " ) )
        try:
            balance = float( input( "What is your starting balance?: $" ) )
        except:
            print( 'FOR YOUR STARTING BALANCE, YOU MUST ENTER ONLY NUMBERS' )
            balance = float( input( "What is your starting balance?: $" ) )
        log_reward = 0
        log_penalty = 0
        log_deposit = 0
        log_withdrawn = 0
        amount_of_deposits = 0
        bonus_received = 0
        penalty_received = 0
        successful_withdrawn = 0
        unsuccessful_withdrawn = 0

    elif user_choice == 5:      #PRINT THE VALUES OF ALL VARIABLES
        print( '\tFINAL BALANCE' )
        print(f'Your final balance is: ${balance}')
        print( f'The total of times attempted to deposit: {log_deposit}' )
        print( f'The total amount of fund deposited: ${amount_of_deposits}' )
        print( f'The total of times a bonus was received: {log_reward}' )
        print( f'The total of bonus received: ${bonus_received}' )
        print( f'The total of times attempted to withdrawn funds successfully: {log_withdrawn}' )
        print( f'The total amount of funds successfully withdrawn: ${successful_withdrawn}' )
        print( f'The total of times attempted to withdrawn funds unsuccessfully: {log_penalty}')
        print( f'The total amount of funds unsuccessfully withdrawn:  ${unsuccessful_withdrawn}' )
        # print( f'penalty_received: {penalty_received}' )
        print( f'The total of times to receive penalties: {log_penalty}')
        print( f'The total amount of penalties received: ${penalty_received}')
        print( f'DONE' )
        run = False




