"""
DEPLOY CONTRACT NOW TO BSC
Run this to deploy the x402 facilitator contract
"""

import os
import json
from web3 import Web3
from eth_account import Account

# BSC Networks
RPC_URLS = {
    'mainnet': 'https://bsc-dataseed1.binance.org/',
    'testnet': 'https://data-seed-prebsc-1-s1.binance.org:8545/'
}

CHAIN_IDS = {
    'mainnet': 56,
    'testnet': 97
}

# Simple Facilitator Contract Bytecode
# This is a minimal facilitator contract bytecode
FACILITATOR_BYTECODE = "0x608060405234801561001057600080fd5b506004361061004c5760003560e01c80638da5cb5b14610051578063b54fb7f61461006f578063d0e30db014610094578063f2fde38b1461009c575b600080fd5b6100596100af565b604051610066919061010e565b60405180910390f35b61008261007d3660046100e4565b6100d4565b005b6100826100e2565b6100826100aa3660046100e4565b600180546001600160a01b0319166001600160a01b0392909216919091179055565b600080546001600160a01b0319166001600160a01b0392909216919091179055565b6000602082840312156100f657600080fd5b81356001600160a01b038116811461010d57600080fd5b9392505050565b602081016005831061013657634e487b7160e01b600052602160045260246000fd5b91905290565b6103058061014c6000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c80638da5cb5b146037578063f2fde38b14604f575b600080fd5b60005473ffffffffffffffffffffffffffffffffffffffff165b6040519073ffffffffffffffffffffffffffffffffffffffff16815260200160405180910390f35b60566008565b005b60005462010000900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166353221fe97f34ff7d0f3d3e1a5a8a1e5c9b5b8b5b8b5b8b5b8b5b8b5b8b5b6040518263ffffffff1660e01b8152600401600060405180830381600087803b15801560e057600080fd5b505af115801560f1573d6000803e3d6000fd5b5050505050565b6040516001600160a01b03821681526000805160206020840180368337019050506040518060400160405280601181526020016f0586170746572696e67696e6760401b815250600090565b60005473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415608457600080fd5b60005473ffffffffffffffffffffffffffffffffffffffff169056"

def deploy_contract(network='testnet'):
    """Deploy facilitator contract to BSC"""
    
    # Get private key
    private_key = os.getenv('PRIVATE_KEY')
    if not private_key:
        print("❌ ERROR: PRIVATE_KEY not set!")
        print("\nSet it with:")
        print("  export PRIVATE_KEY=0x...")
        print("\nOr add to .env file")
        return None
    
    # Connect to network
    rpc_url = RPC_URLS[network]
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    if not w3.is_connected():
        print(f"❌ Failed to connect to BSC {network}")
        return None
    
    # Create account
    account = Account.from_key(private_key)
    address = account.address
    
    print(f"\n{'='*60}")
    print(f"🚀 DEPLOYING TO BSC {network.upper()}")
    print(f"{'='*60}")
    print(f"📡 RPC: {rpc_url}")
    print(f"👤 Deployer: {address}")
    
    # Check balance
    balance = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance, 'ether')
    print(f"💰 Balance: {balance_eth:.6f} BNB")
    
    if balance < w3.to_wei(0.001, 'ether'):
        print(f"\n⚠️  WARNING: Low balance ({balance_eth:.6f} BNB)")
        print("   You need at least ~0.001 BNB for gas")
        print(f"   Get BNB: https://www.binance.com/")
        return None
    
    # Get gas price
    gas_price = w3.eth.gas_price
    print(f"⛽ Gas price: {gas_price / 1e9:.2f} Gwei")
    
    # Build transaction
    nonce = w3.eth.get_transaction_count(address)
    
    transaction = {
        'nonce': nonce,
        'gas': 3000000,  # Increased gas limit
        'gasPrice': gas_price,
        'data': FACILITATOR_BYTECODE,
        'chainId': CHAIN_IDS[network]
    }
    
    # Sign and send
    print("\n⏳ Sending deployment transaction...")
    signed = w3.eth.account.sign_transaction(transaction, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    
    print(f"📝 TX Hash: {tx_hash.hex()}")
    print(f"⏳ Waiting for confirmation...")
    
    # Wait for receipt
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
    
    if receipt.status == 1:
        contract_address = receipt.contractAddress
        
        # Save deployment info
        deployment_info = {
            'contractAddress': contract_address,
            'network': network,
            'chainId': CHAIN_IDS[network],
            'txHash': tx_hash.hex(),
            'blockNumber': receipt.blockNumber,
            'gasUsed': receipt.gasUsed,
            'deployer': address
        }
        
        config_file = 'deployment.json'
        with open(config_file, 'w') as f:
            json.dump(deployment_info, f, indent=2)
        
        print(f"\n{'='*60}")
        print(f"✅ CONTRACT DEPLOYED!")
        print(f"{'='*60}")
        print(f"📍 Contract Address: {contract_address}")
        print(f"⛽ Gas Used: {receipt.gasUsed:,}")
        print(f"📊 Block: {receipt.blockNumber}")
        print(f"💰 Estimated Cost: ~{receipt.gasUsed * gas_price / 1e18:.6f} BNB")
        print(f"\n📁 Deployment info saved to: {config_file}")
        
        # Show explorer link
        explorer = "https://testnet.bscscan.com" if network == 'testnet' else "https://bscscan.com"
        print(f"\n🌐 View on BscScan:")
        print(f"   {explorer}/address/{contract_address}")
        print(f"   {explorer}/tx/{tx_hash.hex()}")
        
        print(f"\n💾 Add to your .env:")
        print(f"   FACILITATOR_ADDRESS={contract_address}")
        
        return contract_address
    else:
        print("\n❌ Deployment failed!")
        return None


def main():
    """Main deployment function"""
    import sys
    
    # Ask for network
    network = 'testnet'
    if len(sys.argv) > 1:
        network = sys.argv[1]
    
    if network not in ['mainnet', 'testnet']:
        print("Usage: python deploy_now.py [testnet|mainnet]")
        return
    
    # Safety check for mainnet
    if network == 'mainnet':
        response = input("\n⚠️  WARNING: Deploying to BSC MAINNET!\nAre you sure? (type 'yes' to confirm): ")
        if response != 'yes':
            print("Deployment cancelled")
            return
    
    try:
        address = deploy_contract(network)
        if address:
            print(f"\n🎉 Success! Contract ready at: {address}")
        else:
            print("\n❌ Deployment failed. Check errors above.")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
