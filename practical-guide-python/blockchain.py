""" blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])
    print(transaction_amount)


def get_user_input():
    user_input =  float(input("Your transaction amount please: "))
    return user_input

tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain) """

""" name = "Fil"
age = 25

def print_data():
    print("My name is " + name + " and my age is " + str(age))
    
print_data()

name_input = input("Your name is: ")
age_input = int(input("Your age is: "))

def print_inputs():
    print("My name is " + name_input + " and my age is " + str(age_input))
    
print_inputs() """

""" import math

age = int(input("Enter your age, please: "))

def calculate_decades():
    return print("You lived " + str(math.floor(age/10)) + " decades.")

calculate_decades()
 """


""" ----------------------------------------------------------------------------------------- """

