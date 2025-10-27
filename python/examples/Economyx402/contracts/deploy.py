"""
Deploy AuthTransferToken to Binance Smart Chain
"""

import os
from web3 import Web3
from eth_account import Account

# BSC Configuration
BSC_MAINNET_RPC = "https://bsc-dataseed1.binance.org/"
BSC_TESTNET_RPC = "https://data-seed-prebsc-1-s1.binance.org:8545/"
CHAIN_ID = 56  # BSC Mainnet (use 97 for testnet)

# Contract bytecode (you'll need to compile first)
# This is a placeholder - you need to compile the contract
CONTRACT_BYTECODE = "0x..."  # Replace with actual bytecode

CONTRACT_ABI = [
    {
        "constant": False,
        "inputs": [
            {"name": "from", "type": "address"},
            {"name": "to", "type": "address"},
            {"name": "value", "type": "uint256"},
            {"name": "validAfter", "type": "uint256"},
            {"name": "validBefore", "type": "uint256"},
            {"name": "nonce", "type": "bytes32"},
            {"name": "v", "type": "uint8"},
            {"name": "r", "type": "bytes32"},
            {"name": "s", "type": "bytes32"}
        ],
        "name": "transferWithAuthorization",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function"
    }
]


def deploy_contract():
    """Deploy AuthTransferToken to BSC."""
    
    # Get private key from environment
    private_key = os.getenv("PRIVATE_KEY")
    if not private_key:
        raise ValueError("PRIVATE_KEY environment variable not set")
    
    # Connect to BSC
    use_testnet = os.getenv("USE_TESTNET", "false").lower() == "true"
    rpc_url = BSC_TESTNET_RPC if use_testnet else BSC_MAINNET_RPC
    
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    if not w3.is_connected():
        raise Exception("Failed to connect to BSC network")
    
    # Create account
    account = Account.from_key(private_key)
    address = account.address
    
    print(f"📡 Connected to BSC {'Testnet' if use_testnet else 'Mainnet'}")
    print(f"👤 Deployer address: {address}")
    print(f"💰 Balance: {w3.from_wei(w3.eth.get_balance(address), 'ether')} BNB")
    
    # Get nonce
    nonce = w3.eth.get_transaction_count(address)
    
    # Prepare deployment transaction
    constructor = w3.eth.contract(abi=CONTRACT_ABI)
    
    # Example deployment with initial supply
    deployment_data = constructor.constructor(
        "Binance Payment Token",  # name
        "BPT",                     # symbol
        18,                        # decimals
        Web3.to_wei(1000000, 'ether')  # initial supply
    ).build_transaction({
        'chainId': CHAIN_ID,
        'gas': 3000000,
        'gasPrice': w3.eth.gas_price,
        'nonce': nonce,
    })
    
    # Sign transaction
    signed_txn = w3.eth.account.sign_transaction(deployment_data, private_key)
    
    # Send transaction
    print("\n🚀 Deploying contract...")
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    
    print(f"📝 Transaction hash: {tx_hash.hex()}")
    print("⏳ Waiting for confirmation...")
    
    # Wait for receipt
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    
    contract_address = tx_receipt.contractAddress
    
    print(f"\n✅ Contract deployed!")
    print(f"📍 Address: {contract_address}")
    print(f"⛽ Gas used: {tx_receipt.gasUsed:,}")
    print(f"\n📊 View on BscScan:")
    network_name = "testnet" if use_testnet else ""
    print(f"   https://bscscan.com{network_name}/address/{contract_address}")
    
    return contract_address


if __name__ == "__main__":
    import sys
    
    # Check for private key
    if not os.getenv("PRIVATE_KEY"):
        print("❌ Error: PRIVATE_KEY environment variable not set")
        print("\nSet it with:")
        print("  export PRIVATE_KEY=0x...")
        sys.exit(1)
    
    try:
        address = deploy_contract()
        print(f"\n💾 Save this address: {address}")
        
    except Exception as e:
        print(f"❌ Deployment failed: {e}")
        sys.exit(1)
