blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])

add_value(2.5)
add_value(8, get_last_blockchain_value())
add_value(3.6, get_last_blockchain_value())

print(blockchain)








""" def sum(a, b):
    return a + b

print(sum(5, 15)) """


""" def calculate(number):
    print(25 + number)

calculate(5) """
