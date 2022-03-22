# by Christian J. Rodriguez and Michelle Bou #BANK ACC SIMULATOR

# starting questions to open the acc
account_name = str( input( "Name for your account: " ) )
try:
    balance = float( input( "What is your starting balance?: $" ) )
except:  # if not int entered this will print and ask again
    print( 'FOR YOUR STARTING BALANCE, YOU MUST ENTER ONLY NUMBERS' )
    balance = float( input( "What is your starting balance?: $" ) )

starting_balance = balance  # used to calculate the amount of deposits done
run = True

options = """1. Deposit some funds
2. Withdraw some funds
3. View balance 
4. Create new account
5. Quit
"""
#  VARIABLES # LAS VECES QUE OCURRIO ESA FUNCIONALIDAD PARA PODER HACER COUNT
log_reward = 0
log_penalty = 0
log_deposit = 0
log_withdrawn = 0
amount_of_deposits = 0
bonus_received = 0
penalty_received = 0
successful_withdrawn = 0
unsuccessful_withdrawn = 0

while run:  # MAIN LOOP
    print( f'\tACCOUNT NAME: {account_name}\n' )
    print( "+++++++++++++++++++++++++++" )

    print( options )
    try:  # MANEJA ILEGAL INPUTS
        user_choice = int( input( ">>>> " ) )
    except:
        print( 'ENTER A INTEGRER NUMBER' )
        print( options )
        user_choice = int( input( ">>>>> " ) )

    if user_choice == 1:
        try:
            user_input = float( input( 'How much you want to deposit ?: $' ) )
        except:
            print( 'ENTER A NUMBER' )
            user_input = float( input( 'How much you want to deposit ?: $' ) )
        if user_input > balance:  # Suma the balance and 2% reward
            balance += (user_input * 1.02)  # add the new balance and the reward
            balance = round( balance, 2 )       #Esta linea causa problemas de roundoff luego de varias entradas
            bonus_received += (user_input * 1.02) - user_input
            bonus_received = round( bonus_received, 2 )     # en esta linea fue que ocurrio el error de aproximacion de redondeo del reward
            log_deposit += 1  # sum accumulator
            log_reward = +1
            amount_of_deposits += user_input
            print( f'Your new balance is ${balance}' )      #este print no debe estar ahí, es para la opción #3
        else:  # THE DEPOSIT IS LESS THAN THE CURRENT BALANCE AND PRINTS NEW BALANCE
            balance += user_input
            log_deposit += 1
            amount_of_deposits += user_input
            print( f'Your new balance is ${balance}' )

    elif user_choice == 2:  # WITHDRAL AND PENALTIES
        try:
            user_input = float( input( "How much you want to withdraw?: $" ) )
        except:
            print( 'ENTER A NUMBER' )
            user_input = float( input( "How much you want to withdraw?: $" ) )

        if user_input > balance:  # conditional to charge a penalty fee
            balance -= 5
            penalty_received += 5
            unsuccessful_withdrawn += user_input
            log_penalty += 1
            print( "WARNING!\nYou do not have the balance and you are unable to withdrawl" )
            print( f'Your new balance is ${balance}' )  #Se supone que no imprimas el balance para esta opción

        else:  # MEANS YOU HAVE THE SUFFICIENT BALANCE
            balance -= user_input
            successful_withdrawn += user_input
            log_withdrawn += 1
            print( f'Your new balance is ${balance}' )

    elif user_choice == 3:  # PRINT THE CURRENT BALANCE
        print( f'\tYour current balance is: ${balance}' )
    elif user_choice == 4:  # RESET ALL AND  CREATES NEW ACCOUNT
        print( 'ALERT YOU WILL CREATE A NEW ACCOUNT AND THE PREVIUS DATA WILL BE RESETED\n' )# ANTES DE RESETEAR LA CUENTA, IMPRIME LOS VALORES QUE, SE ESTABAN REGISTRANDO
        print( '-------------------------------' )

        account_name = str( input( "Name for your account: " ) )
        try:
            balance = float( input( "What is your starting balance?: $" ) )
        except:
            print( 'FOR YOUR STARTING BALANCE, YOU MUST ENTER ONLY NUMBERS' )
            balance = float( input( "What is your starting balance?: $" ) )

        # variables in 0 for the reset
        log_reward = 0
        log_penalty = 0
        log_deposit = 0
        log_withdrawn = 0
        amount_of_deposits = 0
        bonus_received = 0
        penalty_received = 0
        successful_withdrawn = 0
        unsuccessful_withdrawn = 0

    elif user_choice == 5:  # PRINT THE VALUES OF ALL VARIABLES AND CURRENT MENU
        print( '- - - - - - - - - - - - - - ' )
        print( '\tFINAL BALANCE' )
        print( f'Your final balance is: ${balance}' )
        print( f'The total of times attempted to deposit: {log_deposit}' )
        print( f'The total amount of fund deposited: ${amount_of_deposits}' )
        print( f'The total of times a bonus was received: {log_reward}' )
        print( f'The total of bonus received: ${bonus_received}' )
        print( f'The total of times attempted to withdrawn funds successfully: {log_withdrawn}' )
        print( f'The total amount of funds successfully withdrawn: ${successful_withdrawn}' )
        print( f'The total of times attempted to withdrawn funds unsuccessfully: {log_penalty}' )
        print( f'The total amount of funds unsuccessfully withdrawn:  ${unsuccessful_withdrawn}' )
        # print( f'penalty_received: {penalty_received}' )
        print( f'The total of times to receive penalties: {log_penalty}' )
        print( f'The total amount of penalties received: ${penalty_received}' )
        print( f'DONE' )

        print( "Thank you for using our services" )

        print( "Have a nice day!" )

        break  # if quit exits and the loop stops