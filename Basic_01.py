import web3.eth
from web3 import Web3, EthereumTesterProvider

# Making the connection to a provider
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
# w3 = Web3(Web3.WebsocketProvider('wss://127.0.0.1:8545'))
print(w3.isConnected())

# If you stick to the default ports or IPC file locations,
# you can utilize a convenience method to automatically detect the provider and save a few keystrokes:
from web3.auto import w3
print(w3.isConnected())

# The quickest way to interact with the Ethereum blockchain is to use a remote node provider,
# like Infura, Alchemy, or QuickNode. You can connect to a remote node by specifying the endpoint,
# just like the previous local node example:
# from web3 import Web3
# This endpoint is provided by the remote node service after you create an account.

# w3 = Web3(Web3.HTTPProvider('https://<your-provider-url>'))
# w3 = Web3(Web3.WebsocketProvider('wss://<your-provider-url>'))

print(w3.eth.get_block('latest'))
block = w3.eth.get_block('latest')
# Traversing the last block:
for i,j in block.items():
    print(i,j)

# Web3.py can help you read block data, sign and send transactions, deploy and interact with contracts,
# and a number of other features.

# Getting all the accounts details
print(w3.eth.accounts)
# Traversing through the accounts:
Account = w3.eth.accounts
for i in Account:
    print(i)


# Getting the balance of the accounts --->
Balances = w3.eth.get_balance("0xAae7CcebA33685691338646A9fF691456509bc71")
print("The balance of this account is " + str(Balances))
# This will show that the balance of the corresponding account

#
# # Deploying a contract --->
# print("This is the abi ------------>")
# f = open("abi.json", "r")
# abi = f.read()
# print(abi)
#
# print("This is the bytecode ------->")
# f = open("bytecode.json", "r")
# bytecode = f.read()
# print(bytecode)

# Need to check how to deploy, the following doesn't work
# Storage = w3.eth.contract(abi=abi, bytecode=bytecode)
# ExampleContract = w3.eth.contract(abi=abi, bytecode=bytecode)
# tx_hash = ExampleContract.constructor().transact()
# tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
# tx_receipt.contractAddress
# working with the deployed functions
# deployed_contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
# deployed_contract.functions.myFunction(42).transact()
# Using ContractFunction.call
# deployed_contract.functions.getMyValue().call()
# # Using ContractCaller
# deployed_contract.caller().getMyValue()
# 42

# Gives the connection status
print("The connection status is ------>")
print(w3.isConnected())

# Currency conversion
print(Web3.toWei(1, 'ether'))
print(Web3.fromWei(1000000000000000000, 'ether'))

# Check for a recognised address
print(Web3.isAddress("0xebbCe9911D3d99c9B6b5E9830583B522b7ecce71"))

#checking for the latest block
block = web3.eth.get_block('latest')
print(block)