"""BSC Merchant Agent Implementation."""

import os
from typing import Dict, Any
from x402_a2a import create_payment_requirements, x402PaymentRequiredException


class BSCMerchantAgent:
    """Merchant agent that accepts BSC payments."""
    
    def __init__(self):
        """Initialize BSC merchant agent."""
        self.network = os.getenv("BSC_NETWORK", "bsc")
        self.wallet_address = os.getenv("MERCHANT_WALLET", "0x" + "Merchant" * 5)
        
        # Common BSC token addresses
        self.tokens = {
            "USDC": "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",
            "USDT": "0x55d398326f99059fF775485246999027B3197955",
            "BUSD": "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56"
        }
        
        print(f"🏪 BSC Merchant Agent initialized")
        print(f"  Network: {self.network}")
        print(f"  Wallet: {self.wallet_address}")
    
    async def sell_service(self, service_name: str) -> Dict[str, Any]:
        """
        Sell a service, requiring BSC payment.
        
        Args:
            service_name: Name of the service to sell
            
        Returns:
            Service delivery result
            
        Raises:
            x402PaymentRequiredException: When payment is required
        """
        print(f"\n🛒 Requested service: {service_name}")
        
        # Determine price based on service
        prices = {
            "AI Image Generation": "$2.00",
            "Premium API Access": "$10.00",
            "Custom AI Model": "$50.00"
        }
        
        price = prices.get(service_name, "$5.00")
        
        # Create payment requirements for BSC
        payment_req = create_payment_requirements(
            price=price,
            pay_to_address=self.wallet_address,
            resource=f"/services/{service_name.replace(' ', '_').lower()}",
            network=self.network,
            asset=self.tokens["USDC"],  # Use USDC by default
            description=f"Payment for {service_name}",
        )
        
        print(f"💰 Payment required: {price} USDC on {self.network}")
        print(f"  Resource: {payment_req.resource}")
        print(f"  Asset: {payment_req.asset}")
        
        # Raise payment exception (will be caught by executor)
        raise x402PaymentRequiredException(
            message=f"Payment required for {service_name}",
            payment_requirements=[payment_req]
        )
    
    async def deliver_service(self, service_name: str) -> Dict[str, Any]:
        """
        Deliver a service after payment is verified.
        
        Args:
            service_name: Name of the service to deliver
            
        Returns:
            Service delivery result
        """
        print(f"\n✅ Delivering service: {service_name}")
        
        # Simulate service delivery
        results = {
            "AI Image Generation": {
                "status": "generated",
                "image_url": "https://example.com/generated-image.png",
                "metadata": {"model": "DALL-E 3", "resolution": "1024x1024"}
            },
            "Premium API Access": {
                "status": "active",
                "api_key": "sk-" + "a" * 48,
                "rate_limit": "10,000 requests/day"
            },
            "Custom AI Model": {
                "status": "deployed",
                "model_id": "custom-model-123",
                "endpoint": "https://api.example.com/models/custom-model-123"
            }
        }
        
        return results.get(service_name, {
            "status": "completed",
            "message": f"Service {service_name} delivered successfully"
        })
