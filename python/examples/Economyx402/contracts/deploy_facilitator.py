"""
Deploy x402Facilitator to BSC Mainnet
This contract handles EIP-3009 payments for USDC, USDT, etc.
"""

import os
import json
from web3 import Web3
from eth_account import Account

# BSC RPC Endpoints
BSC_MAINNET = "https://bsc-dataseed1.binance.org/"
BSC_TESTNET = "https://data-seed-prebsc-1-s1.binance.org:8545/"

# Facilitator Contract ABI (simplified)
FACILITATOR_ABI = [
    {
        "inputs": [
            {"name": "tokenContract", "type": "address"},
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
        "name": "settlePayment",
        "outputs": [{"name": "", "type": "bool"}],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"name": "nonce", "type": "bytes32"}],
        "name": "isAuthorizationUsed",
        "outputs": [{"name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function"
    }
]


def get_deployment_bytecode():
    """Get the compiled bytecode for the Facilitator contract."""
    # This would be the actual compiled bytecode from Solidity
    # You need to compile the contract first using solc
    # For now, this is a placeholder
    return "0x..."  # Replace with actual bytecode


def deploy_facilitator():
    """Deploy x402Facilitator to BSC."""
    
    # Get configuration
    private_key = os.getenv("PRIVATE_KEY")
    use_testnet = os.getenv("USE_TESTNET", "false").lower() == "true"
    
    if not private_key:
        raise ValueError("Set PRIVATE_KEY environment variable")
    
    # Connect to BSC
    rpc_url = BSC_TESTNET if use_testnet else BSC_MAINNET
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    if not w3.is_connected():
        raise Exception("Failed to connect to BSC")
    
    # Create account
    account = Account.from_key(private_key)
    address = account.address
    
    network = "Testnet" if use_testnet else "Mainnet"
    print(f"📡 Connected to BSC {network}")
    print(f"👤 Deployer: {address}")
    print(f"💰 Balance: {w3.from_wei(w3.eth.get_balance(address), 'ether')} BNB")
    
    # Check balance
    balance = w3.eth.get_balance(address)
    if balance < Web3.to_wei(0.01, 'ether'):
        print(f"⚠️  Warning: Low balance ({Web3.from_wei(balance, 'ether')} BNB)")
        print("   You may not have enough for gas fees")
    
    # Get nonce
    nonce = w3.eth.get_transaction_count(address)
    
    # Deploy contract
    print("\n🚀 Deploying Facilitator contract...")
    
    # Get bytecode (you need to compile first!)
    bytecode = get_deployment_bytecode()
    
    if bytecode == "0x...":
        print("❌ Error: Contract not compiled!")
        print("\nTo compile:")
        print("  solc --bin Facilitator.sol -o build/")
        print("\nThen update deploy_facilitator.py with the bytecode")
        return
    
    # Build transaction
    transaction = {
        'nonce': nonce,
        'from': address,
        'data': bytecode,
        'gas': 2000000,
        'gasPrice': w3.eth.gas_price,
        'chainId': 56 if not use_testnet else 97
    }
    
    # Sign and send
    signed = w3.eth.account.sign_transaction(transaction, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    
    print(f"📝 TX Hash: {tx_hash.hex()}")
    print("⏳ Waiting for confirmation...")
    
    # Wait for receipt
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    
    if receipt.status == 1:
        contract_address = receipt.contractAddress
        print(f"\n✅ Contract deployed successfully!")
        print(f"📍 Address: {contract_address}")
        print(f"⛽ Gas used: {receipt.gasUsed:,}")
        
        # Save address
        config = {
            "contractAddress": contract_address,
            "network": "bsc" if not use_testnet else "bsc-testnet",
            "txHash": tx_hash.hex(),
            "blockNumber": receipt.blockNumber,
            "gasUsed": str(receipt.gasUsed)
        }
        
        config_file = ".deployed_config.json"
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"\n💾 Configuration saved to {config_file}")
        print(f"\n🌐 View on BscScan:")
        if use_testnet:
            print(f"   https://testnet.bscscan.com/address/{contract_address}")
        else:
            print(f"   https://bscscan.com/address/{contract_address}")
    else:
        print("\n❌ Deployment failed!")
        print(f"   Status: {receipt.status}")
    
    return receipt.contractAddress


def main():
    """Main deployment function."""
    print("=" * 60)
    print("🚀 x402Facilitator Deployment to BSC")
    print("=" * 60)
    
    try:
        address = deploy_facilitator()
        print(f"\n✨ Save this address for your configuration: {address}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
