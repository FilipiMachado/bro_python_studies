""" blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


tx_amount = float(input("Your transaction amount please: "))
add_value(tx_amount)

tx_amount = float(input("Your transaction amount please: "))
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = float(input("Your transaction amount please: "))
add_value(tx_amount, get_last_blockchain_value())

print(blockchain) """

my_value = input("Your value here: ")
print(my_value)








""" def sum(a, b):
    return a + b

print(sum(5, 15)) """


""" def calculate(number):
    print(25 + number)

calculate(5) """
