import web3.eth
from web3 import Web3

#connecting to a node
eth = 'INSERT YOUR API KEY'

w3 = Web3(Web3.HTTPProvider(eth))
print("This the status of your connection to the blockchain: " + str(w3.isConnected()))

# Getting information about the latest block -------------------------------------------------
latest_block = w3.eth.get_block('latest')
print(latest_block)
# Traversing or iterating over the latest block
print("These are the latest block information ------>")
for i,j in latest_block.items():
    print(i,j)

# if we want to see the specific information about the latest block---------------------------
print("This is the latest block timestamp----------------------------")
print(latest_block['timestamp'])

# Skip from showing this one in class
# if we want to get the block number ---------------------------------------------------------
print("This also gives the latest block number-------------------------------")
print(w3.eth.block_number)





