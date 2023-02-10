import web3
from web3 import Web3
from solcx import compile_source

# Solidity source code

f = open("contract.sol", "r")
x = f.read()
compiled_sol = compile_source(x,output_values=['abi', 'bin'])

# retrieve the contract interface
contract_id, contract_interface = compiled_sol.popitem()

# get bytecode / bin
bytecode = contract_interface['bin']

# get abi
abi = contract_interface['abi']

# web3.py instance
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# set pre-funded account as sender
w3.eth.default_account = w3.eth.accounts[0]

Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)

# Submit the transaction that deploys the contract
tx_hash = Greeter.constructor().transact()

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

greeter = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

greeter.functions.greet().call()


tx_hash = greeter.functions.setGreeting('Nihao').transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(tx_hash)

# Can further iterate the tx_receipt
print(tx_receipt)
print(greeter.functions.greet().call())


