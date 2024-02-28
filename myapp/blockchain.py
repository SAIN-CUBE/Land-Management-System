from web3 import Web3

# Connect to an Ethereum node (e.g., Infura)
web3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/b2af7fbe77b041a8a38a34a87c224bc0'))

# Define the contract address and ABI (Application Binary Interface)
contract_address = '0x31151f2A742263F38e7C8aAF598a178036b45897'
contract_abi = [{"inputs":[{"internalType":"uint256","name":"_uniqueId","type":"uint256"},{"internalType":"uint256","name":"_areaAsPerDeed","type":"uint256"},{"internalType":"uint256","name":"_areaAsPerSurvey","type":"uint256"},{"internalType":"address","name":"_coordinator","type":"address"},{"internalType":"string","name":"_city","type":"string"},{"internalType":"string","name":"_subdivision","type":"string"},{"internalType":"string[]","name":"_neighborhoods","type":"string[]"}],"name":"addLand","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_landId","type":"uint256"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"uint256","name":"_id","type":"uint256"},{"internalType":"uint256","name":"_percentageOwnership","type":"uint256"}],"name":"addOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_landId","type":"uint256"},{"internalType":"address","name":"_owner","type":"address"}],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"landOwners","outputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"percentageOwnership","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"landTransactions","outputs":[{"internalType":"string","name":"purpose","type":"string"},{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"landId","type":"uint256"},{"internalType":"uint256","name":"timestamp","type":"uint256"},{"internalType":"bytes32","name":"previousTransactionHash","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"lands","outputs":[{"internalType":"uint256","name":"uniqueId","type":"uint256"},{"internalType":"uint256","name":"areaAsPerDeed","type":"uint256"},{"internalType":"uint256","name":"areaAsPerSurvey","type":"uint256"},{"internalType":"address","name":"coordinator","type":"address"},{"internalType":"string","name":"city","type":"string"},{"internalType":"string","name":"subdivision","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_landId","type":"uint256"},{"internalType":"string","name":"_purpose","type":"string"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"bytes32","name":"_previousTransactionHash","type":"bytes32"}],"name":"performTransaction","outputs":[],"stateMutability":"nonpayable","type":"function"}]

# Instantiate the contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)


def add_land():
    # Call the addLand function
    tx_hash = contract.functions.addLand(
        _uniqueId=123,
        _areaAsPerDeed=1000,
        _areaAsPerSurvey=1100,
        _coordinator=web3.eth.accounts[0],
        _city="Sample City",
        _subdivision="Sample Subdivision",
        _neighborhoods=["Neighborhood 1", "Neighborhood 2"]
    ).transact()

    # Wait for the transaction to be mined
    web3.eth.waitForTransactionReceipt(tx_hash)

    print("Land added successfully.")


# Call the performTransaction function
tx_hash = contract.functions.performTransaction(
    _landId=123,
    _purpose="Sample purpose",
    _to="0xRecipientAddress",
    _previousTransactionHash=b'\x00' * 32  # Example previous transaction hash
).transact()

# Wait for the transaction to be mined
web3.eth.waitForTransactionReceipt(tx_hash)

print("Transaction performed successfully.")