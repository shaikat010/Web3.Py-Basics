import web3.eth
from web3 import Web3
from solcx import compile_source

#connecting to a node
eth = 'http://127.0.0.1:8545'
w3 = Web3(Web3.HTTPProvider(eth))
chain_id = 1337
print("This the status of your connection to the blockchain: " + str(w3.isConnected()))

my_address = "0xf437c6bED277012b0dd83B93d4848Ef7d39EfC2B"
private_key = "0x30c2424e0bc9e3b89c74b8199c168462a77dd82436ef67c8bb3a5e82c89e52ee"

# Solidity source code
# ------------------------------------------------------------------------
f = open("contract.sol", "r")
x = f.read()
compiled_sol = compile_source(x,output_values=['abi', 'bin'])
# ------------------------------------------------------------------------

# retrieve the contract interface -----------------------------------------
contract_id, contract_interface = compiled_sol.popitem()

# get bytecode / bin ----------------
bytecode = contract_interface['bin']
print("This is the bytecode ------------------>")
print(bytecode)
# get abi ---------------------------
abi = contract_interface['abi']
print("This is the ABI ------------------------>")
print(abi)

# The compiled code ------------------------------------
print("This is the compiled code ------------------>")
compiled_sol = compile_source(x,output_values=['abi', 'bin'])



# set pre-funded account as sender
w3.eth.default_account = w3.eth.accounts[0]
print("This is the default account: " + str(w3.eth.default_account))

# Creating the contract object ------------------------------------------------------
Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)
print(" This is the Greeter contract : " + str(Greeter))

# Get the latest transactionCount
nonce = w3.eth.getTransactionCount(my_address)
# Submit the transaction that deploys the contract
transaction = Greeter.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)

# Sign the transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print("Deploying Contract!")

# Sending the transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# Wait for the transaction to be mined, and get the transaction receipt
print("Waiting for transaction to finish...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Done! Contract deployed to {tx_receipt.contractAddress}")
# -----------------------------------------------------------------------------------------


# Submit the transaction that deploys the contract-------------------------------------
tx_hash = Greeter.constructor().transact()
print("The transaction has occurred and this is the transaction hash: ")
print(tx_hash)


# Calling the greet function -----------------------
# Working with deployed Contracts
Greeter = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
print(f"This is the greet function:  {Greeter.functions.greet().call()}")

# --------------------------------------------------------------------------------------------
tx_hash = Greeter.functions.setGreeting('Shaikat').transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("This is the other transaction hash: " + str(tx_hash))

# Can further iterate the tx_receipt-----------------------
print(tx_receipt)

# Calling the greet() function again
print(Greeter.functions.greet().call())






