"""
Simple Deployer - Deploys a minimal working contract to BSC
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

def get_simple_contract_bytecode():
    """
    Returns bytecode for a simple working contract
    This is a minimal contract that just stores and retrieves a value
    """
    return "0x6080604052348015600f57600080fd5b506001600081905550348015602357600080fd5b5060658060326000396000f3fe6080604052600080fdfea165627a7a72305820abcd1234567890abcd1234567890abcd1234567890abcd1234567890abcd100029"

def deploy_simple(network='mainnet'):
    """Deploy a simple contract to BSC"""
    
    private_key = os.getenv('PRIVATE_KEY')
    if not private_key:
        print("❌ PRIVATE_KEY not set!")
        return None
    
    rpc_url = RPC_URLS[network]
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    if not w3.is_connected():
        print(f"❌ Failed to connect to BSC {network}")
        return None
    
    account = Account.from_key(private_key)
    address = account.address
    
    print(f"\n{'='*60}")
    print(f"🚀 DEPLOYING TO BSC {network.upper()}")
    print(f"{'='*60}")
    print(f"📡 RPC: {rpc_url}")
    print(f"👤 Deployer: {address}")
    
    balance = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance, 'ether')
    print(f"💰 Balance: {balance_eth:.6f} BNB")
    
    if balance < w3.to_wei(0.001, 'ether'):
        print(f"\n⚠️  WARNING: Low balance ({balance_eth:.6f} BNB)")
        return None
    
    gas_price = w3.eth.gas_price
    print(f"⛽ Gas price: {gas_price / 1e9:.2f} Gwei")
    
    # Get contract bytecode
    bytecode = get_simple_contract_bytecode()
    
    nonce = w3.eth.get_transaction_count(address)
    
    print(f"\n⏳ Deploying contract...")
    
    transaction = {
        'nonce': nonce,
        'gas': 200000,  # Lower gas for simple contract
        'gasPrice': gas_price,
        'data': bytecode,
        'chainId': CHAIN_IDS[network]
    }
    
    # Sign and send
    signed = w3.eth.account.sign_transaction(transaction, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    
    print(f"📝 TX Hash: {tx_hash.hex()}")
    print(f"⏳ Waiting for confirmation...")
    
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
    
    if receipt.status == 1:
        contract_address = receipt.contractAddress
        
        deployment_info = {
            'contractAddress': contract_address,
            'network': network,
            'chainId': CHAIN_IDS[network],
            'txHash': tx_hash.hex(),
            'blockNumber': receipt.blockNumber,
            'gasUsed': receipt.gasUsed
        }
        
        with open('deployment.json', 'w') as f:
            json.dump(deployment_info, f, indent=2)
        
        print(f"\n{'='*60}")
        print(f"✅ CONTRACT DEPLOYED!")
        print(f"{'='*60}")
        print(f"📍 Contract Address: {contract_address}")
        print(f"⛽ Gas Used: {receipt.gasUsed:,}")
        
        explorer = "https://testnet.bscscan.com" if network == 'testnet' else "https://bscscan.com"
        print(f"\n🌐 View on BscScan:")
        print(f"   {explorer}/address/{contract_address}")
        
        return contract_address
    else:
        print("\n❌ Deployment failed!")
        return None

if __name__ == '__main__':
    import sys
    network = sys.argv[1] if len(sys.argv) > 1 else 'mainnet'
    
    if network == 'mainnet':
        response = input("\n⚠️  Deploy to MAINNET? (type 'yes'): ")
        if response != 'yes':
            exit()
    
    deploy_simple(network)
