"""
GET STARTED WITH BSC NOW - NO DEPLOYMENT NEEDED!
This script shows you how to use BSC with x402_a2a
"""

import os
from x402_a2a import create_payment_requirements, x402PaymentRequiredException

# BSC USDC Contract (Already Deployed!)
BSC_USDC = "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d"
BSC_USDT = "0x55d398326f99059fF775485246999027B3197955"

def create_bsc_payment(price: str, pay_to: str, service: str):
    """
    Create BSC payment requirements - NO DEPLOYMENT NEEDED!
    
    USDC on BSC already supports EIP-3009.
    Just use it directly!
    """
    
    requirements = create_payment_requirements(
        price=price,
        pay_to_address=pay_to,
        resource=f"/{service.replace(' ', '_').lower()}",
        network="bsc",  # Binance Smart Chain
        asset=BSC_USDC,  # USDC on BSC (already deployed!)
        description=f"Payment for {service}"
    )
    
    print(f"\n✅ BSC Payment Requirements Created!")
    print(f"  💰 Amount: {price}")
    print(f"  🏗️  Network: BSC (Binance Smart Chain)")
    print(f"  💵 Token: USDC")
    print(f"  📍 Asset: {BSC_USDC}")
    print(f"  🎯 Pay To: {pay_to}")
    
    return requirements


def demo_usage():
    """Demo of how to use BSC payments"""
    
    print("="*60)
    print("🚀 BSC x402 Payment Demo - NO DEPLOYMENT NEEDED!")
    print("="*60)
    
    # Example 1: Create payment requirement
    print("\n📝 Example 1: Create BSC Payment")
    requirement = create_bsc_payment(
        price="$10.00",
        pay_to="0xYourWalletAddress",
        service="AI Image Generation"
    )
    
    print(f"\n📋 Payment Requirement:")
    print(f"  Scheme: {requirement.scheme}")
    print(f"  Network: {requirement.network}")
    print(f"  Max Amount: {requirement.max_amount_required}")
    
    # Example 2: Multiple payment options
    print("\n📝 Example 2: Multiple Payment Options")
    
    # USDC option
    usdc_option = create_payment_requirements(
        price="$10.00",
        pay_to_address="0xYourWallet",
        resource="/premium-service",
        network="bsc",
        asset=BSC_USDC,
        description="Pay with USDC on BSC"
    )
    
    # USDT option
    usdt_option = create_payment_requirements(
        price="$10.00",
        pay_to_address="0xYourWallet",
        resource="/premium-service",
        network="bsc",
        asset=BSC_USDT,
        description="Pay with USDT on BSC"
    )
    
    print("\n✅ Two payment options:")
    print(f"  Option 1: USDC - {usdc_option.asset}")
    print(f"  Option 2: USDT - {usdt_option.asset}")
    
    # Example 3: Raise payment exception (merchant side)
    print("\n📝 Example 3: Merchant Requires Payment")
    
    def merchant_sell_service(service_name: str, price: str):
        """Merchant selling a service"""
        
        # Create payment requirement
        payment_req = create_bsc_payment(
            price=price,
            pay_to="0xMerchantWallet",
            service=service_name
        )
        
        # Raise exception to signal payment required
        raise x402PaymentRequiredException(
            message=f"Payment required for {service_name}",
            payment_requirements=[payment_req]
        )
    
    print("\n🏪 Merchant is selling services...")
    print("💰 When a customer requests a paid service:")
    
    try:
        merchant_sell_service("AI Image Generation", "$5.00")
    except x402PaymentRequiredException as e:
        print(f"  ✅ Payment required!")
        print(f"  💰 Amount: {e.payment_requirements[0].max_amount_required}")
        print(f"  🌐 Network: {e.payment_requirements[0].network}")
    
    print("\n" + "="*60)
    print("✅ That's it! No deployment needed!")
    print("="*60)
    print("\n🚀 You can now use BSC for x402 payments!")
    print("   - Use existing USDC/USDT contracts")
    print("   - No smart contract deployment needed")
    print("   - Just configure and use!")
    print("\n📚 Next: See DEPLOY_NOW.txt if you want to deploy")


if __name__ == "__main__":
    demo_usage()
