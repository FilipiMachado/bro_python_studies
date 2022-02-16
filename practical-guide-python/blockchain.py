blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


tx_amount = int(input("Your transaction amount please: "))
add_value(tx_amount)
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=8)
add_value(3.60, get_last_blockchain_value())

print(blockchain)








""" def sum(a, b):
    return a + b

print(sum(5, 15)) """


""" def calculate(number):
    print(25 + number)

calculate(5) """
