"""BSC Client Agent Implementation."""

import asyncio
import os
from typing import Optional
from client_agent.wallet import BSCWallet
from x402_a2a import x402Utils


class BSCClientAgent:
    """Client agent that handles BSC payments for A2A protocol."""
    
    def __init__(self):
        """Initialize the BSC client agent."""
        self.wallet = BSCWallet()
        self.utils = x402Utils()
        self.network = os.getenv("BSC_NETWORK", "bsc")
        print(f"✅ BSC Client Agent initialized for network: {self.network}")
    
    async def purchase_service(self, service_name: str, merchant_url: str):
        """
        Purchase a service from a merchant using BSC payments.
        
        Args:
            service_name: Name of the service to purchase
            merchant_url: URL of the merchant agent
            
        Returns:
            Purchase result with service delivery
        """
        print(f"\n🛒 Starting purchase for: {service_name}")
        print(f"🏪 Merchant: {merchant_url}")
        print(f"🌐 Network: {self.network}")
        
        try:
            # Step 1: Request service from merchant
            print("\n📤 Step 1: Requesting service from merchant...")
            # This would typically make an HTTP request to the merchant
            # For demo, we'll simulate the response
            
            # Step 2: Receive payment requirements
            print("📥 Step 2: Received payment requirements")
            print("💰 Payment required on BSC network")
            
            # Step 3: User confirms payment
            print("\n✅ User confirmed payment")
            print(f"💳 Preparing to pay with {self.network}...")
            
            # Step 4: Wallet signs the payment
            print("✍️  Step 3: Signing payment authorization...")
            # The wallet would sign the EIP-3009 authorization here
            print("✅ Payment signed successfully")
            
            # Step 5: Submit payment to merchant
            print("\n📤 Step 4: Submitting payment to merchant...")
            print("⏳ Waiting for merchant verification...")
            
            # Simulate merchant verification and settlement
            await asyncio.sleep(1)
            
            print("✅ Step 5: Payment verified and settled on BSC")
            print("🎉 Service delivered successfully!")
            
            return {
                "status": "success",
                "service": service_name,
                "network": self.network,
                "transaction": "0x" + "a" * 64,  # Mock transaction hash
                "message": f"Successfully purchased {service_name}"
            }
            
        except Exception as e:
            print(f"\n❌ Error during purchase: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    async def handle_payment_requirements(self, payment_requirements: dict):
        """
        Handle payment requirements from merchant.
        
        Args:
            payment_requirements: Payment requirements dict from merchant
            
        Returns:
            Signed payment payload
        """
        print("\n📋 Processing payment requirements:")
        print(f"  Network: {payment_requirements.get('network')}")
        print(f"  Asset: {payment_requirements.get('asset')}")
        print(f"  Amount: {payment_requirements.get('maxAmountRequired')}")
        
        # Ask wallet to sign
        payment_payload = await self.wallet.sign_payment(payment_requirements)
        
        return payment_payload


# Demo usage
async def main():
    """Demo usage of BSC Client Agent."""
    agent = BSCClientAgent()
    
    # Demo: Purchase a service
    result = await agent.purchase_service(
        service_name="AI Image Generation",
        merchant_url="http://localhost:8000"
    )
    
    print(f"\n📊 Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
