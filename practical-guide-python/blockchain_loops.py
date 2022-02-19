# Initializing our (empty) blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    user_input = float(input('Your transaction amount please: '))
    return user_input

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block:')
        print(block)

# Get the first transaction input and add the value to the blockchain
tx_amount = get_transaction_value()
add_value(tx_amount)

# Get the second transaction input and add the value to the blockchain


# Get the third transaction input and add the value to the blockchain


# Output the blockchain list to the console

while True:
    print("Choose a option")
    print("1: Add a transaction")
    print("2: Output the blockchain")
    print("q: Quit")
    user_choice = get_user_choice()
    
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        print("Quitted!")
    else:
        print("Input is invalid, pick a correct value!")
    

print("Done!")


