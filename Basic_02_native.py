import web3.eth
from web3 import Web3

#connecting to a node
eth = 'INSERT YOUR API KEY'

w3 = Web3(Web3.HTTPProvider(eth))
print("This the status of your connection to the blockchain: " + str(w3.isConnected()))

# Getting the native balance of an ethereum account
balance = w3.eth.get_balance('0x9f4B4CeCa7aCE96834Bd2fcC961c772De7cb481a')
print("This is the balance of the account: " + str(balance))

# convert the balance to ether
print("This is the balance but it is in ether ----------------------------")
print(w3.fromWei(balance,'ether'))


# getting information about transactions
transaction = w3.eth.get_transaction("0xe468de392030d7cc9d5b32f7849e652dd334671dac236c16576a38a2d7d410da")
print("These are the transaction details")
print(transaction)

# Traversing the transaction --------------------------------------
print("These are the transaction details:--------------------------------- ")
for i,j in transaction.items():
    print(i,j)
# You can also go and get the specific key-value pair via mentioning the key




