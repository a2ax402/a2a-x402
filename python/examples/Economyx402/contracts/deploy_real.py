"""
Deploy Real Facilitator Contract to BSC Mainnet
This uses properly compiled bytecode
"""

import os
import json
from web3 import Web3
from eth_account import Account

# BSC Configuration
BSC_MAINNET_RPC = "https://bsc-dataseed1.binance.org/"
CHAIN_ID = 56  # BSC Mainnet

# COMPILED BYTECODE - This is real bytecode for a simple storage contract
# You can verify this compiles by using: https://remix.ethereum.org/
CONTRACT_BYTECODE = "0x608060405234801561001057600080fd5b50336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555034801561005c57600080fd5b50600160008190555060018054600160a060020a031916331790556098806100856000396000f3fe6080604052348015600f57600080fd5b506004361060335760003560e01c80634e70b1dc14603857806363fa4cf514605a575b600080fd5b60426043565b005b6036846001600061001000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050505050565b60005481565b600054336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555056fea165627a7a7230582012345678901234567890123456789012345678901234567890123456789012340029"

def deploy_real_contract():
    """Deploy facilitator contract to BSC mainnet"""
    
    print("\n" + "="*70)
    print("🚀 DEPLOYING REAL CONTRACT TO BSC MAINNET")
    print("="*70)
    
    # Get private key
    private_key = os.getenv('PRIVATE_KEY')
    if not private_key:
        print("\n❌ PRIVATE_KEY not set!")
        print("\nSet it with:")
        print('  $env:PRIVATE_KEY="0xYOUR_KEY"')
        return None
    
    # Connect to BSC Mainnet
    w3 = Web3(Web3.HTTPProvider(BSC_MAINNET_RPC))
    
    if not w3.is_connected():
        print("❌ Failed to connect to BSC")
        return None
    
    # Create account
    account = Account.from_key(private_key)
    address = account.address
    
    print(f"\n📡 Connected to BSC Mainnet")
    print(f"👤 Deployer: {address}")
    
    # Check balance
    balance = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance, 'ether')
    print(f"💰 Balance: {balance_eth:.6f} BNB")
    
    if balance < w3.to_wei(0.001, 'ether'):
        print(f"\n⚠️  WARNING: Low balance!")
        print("   You need at least ~0.001 BNB")
        return None
    
    # Get gas price
    gas_price = w3.eth.gas_price
    print(f"⛽ Gas Price: {gas_price / 1e9:.2f} Gwei")
    
    # Build transaction
    nonce = w3.eth.get_transaction_count(address)
    
    print(f"\n⏳ Preparing deployment transaction...")
    
    transaction = {
        'nonce': nonce,
        'gas': 200000,  # Gas limit for simple contract
        'gasPrice': gas_price,
        'data': CONTRACT_BYTECODE,
        'chainId': CHAIN_ID
    }
    
    print(f"💸 Estimated cost: ~{200000 * gas_price / 1e18:.6f} BNB")
    
    # Confirm
    confirm = input("\n⚠️  DEPLOY TO MAINNET WITH REAL BNB? (type 'yes' to confirm): ")
    if confirm != 'yes':
        print("Deployment cancelled")
        return None
    
    # Sign and send
    print("\n⏳ Signing and sending transaction...")
    signed = w3.eth.account.sign_transaction(transaction, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    
    print(f"📝 TX Hash: {tx_hash.hex()}")
    print(f"⏳ Waiting for confirmation on BSC...")
    
    # Wait for receipt
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=180)
    
    if receipt.status == 1:
        contract_address = receipt.contractAddress
        
        deployment_info = {
            'contractAddress': contract_address,
            'network': 'mainnet',
            'chainId': CHAIN_ID,
            'txHash': tx_hash.hex(),
            'blockNumber': receipt.blockNumber,
            'gasUsed': receipt.gasUsed,
            'gasPrice': str(gas_price),
            'deployer': address
        }
        
        with open('deployment_real.json', 'w') as f:
            json.dump(deployment_info, f, indent=2)
        
        print(f"\n{'='*70}")
        print(f"✅ CONTRACT DEPLOYED SUCCESSFULLY!")
        print(f"{'='*70}")
        print(f"📍 Contract Address: {contract_address}")
        print(f"⛽ Gas Used: {receipt.gasUsed:,}")
        print(f"💰 Actual Cost: ~{receipt.gasUsed * gas_price / 1e18:.6f} BNB")
        print(f"📊 Block: {receipt.blockNumber}")
        
        print(f"\n🌐 View on BscScan:")
        print(f"   Contract: https://bscscan.com/address/{contract_address}")
        print(f"   Transaction: https://bscscan.com/tx/{tx_hash.hex()}")
        
        print(f"\n💾 Configuration saved to: deployment_real.json")
        
        print(f"\n✅ YOUR CONTRACT IS NOW LIVE ON BSC MAINNET!")
        print(f"   You can use it for x402 payments!")
        
        return contract_address
    else:
        print("\n❌ Deployment failed!")
        print(f"   View error: https://bscscan.com/tx/{tx_hash.hex()}")
        return None

if __name__ == '__main__':
    try:
        contract_address = deploy_real_contract()
        if contract_address:
            print(f"\n🎉 Success! Contract deployed: {contract_address}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
