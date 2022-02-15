#                       Bank Account Simulator
#	BANK ACCOUNT SIMULATOR

account_name = str( input( "Name for your account: " ) )
balance = float( input( "What is your starting balance?: $" ) )
starting_balance = balance  # this varible is use to calculate the amount of deposits doned
run = True
options = """1. Deposit some funds
2. Withdraw some funds
3. View balance 
4. Create new account
5. Quit
"""
# LOGS OF VARIABLES # LAS VECES QUE OCURRIO ESA FUNCIONALIDAD
log_reward = 0
log_penalty = 0
log_deposit = 0
log_withdrawn = 0

amount_of_deposits = 0

bonus_received = 0
penalty_received = 0
successful_withdrawn = 0
unsuccessful_withdrawn = 0

while run:
    print( f'\tACCOUNT NAME: {account_name}\n' )
    print( options )
    user_choice = int( input( "/>" ) )
    if user_choice == 1:
        user_input = float( input( 'How much you want to deposit ?: $' ) )
        if user_input > balance:  # Sum the balance and 2% reward
            balance += (user_input * 1.02)  # add the balance and the reward
            bonus_received += (user_input * 1.02) - user_input
            log_deposit += 1
            log_reward = +1
            amount_of_deposits += user_input
            print( f'Your new balance is ${balance}' )
        else:
            balance += user_input
            log_deposit += 1
            amount_of_deposits += user_input
            print( f'Your new balance is ${balance}' )

    elif user_choice == 2:
        user_input = float( input( "How much you want to withdraw?: $" ) )
        if user_input > balance:  # conditional to charge a penalty fee
            balance -= 5
            penalty_received += 5
            unsuccessful_withdrawn += user_input
            log_penalty += 1
            print( f'Your new balance is ${balance}' )
        else:
            balance -= user_input
            successful_withdrawn += user_input
            log_withdrawn += 1
            print( f'Your new balance is ${balance}' )
    elif user_choice == 3:
        print( f'Your current balance is: ${balance}' )
    elif user_choice == 4:
        print( 'Create a new account!' )
    elif user_choice == 5:
        print( 'STATUS OF ALL VARIABLES' )
        print( f'log_reward {log_reward}' )
        print( f'log_penalty {log_penalty}' )
        print( f'log_deposit {log_deposit}' )
        print( f'log_withdrawn {log_withdrawn}' )
        print( f'amount_of_deposits {amount_of_deposits}' )
        print( f'log_reward {log_reward}' )
        print( f'bonus_received {bonus_received}' )
        print( f'penalty_received {penalty_received}' )
        print( f'successful_withdrawn {successful_withdrawn}' )
        print( f'unsuccessful_withdrawn {unsuccessful_withdrawn}' )
        print( f'DONE' )
        run = False




