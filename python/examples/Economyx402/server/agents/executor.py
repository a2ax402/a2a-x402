"""BSC Executor for x402 payment flow."""

import os
from typing import Dict, Any
from server.agents.merchant_agent import BSCMerchantAgent
from x402_a2a import x402Utils
from x402_a2a.types import PaymentStatus


class BSCExecutor:
    """Executor that handles BSC payment flow for merchant agent."""
    
    def __init__(self, merchant: BSCMerchantAgent, facilitator=None):
        """
        Initialize BSC executor.
        
        Args:
            merchant: BSC merchant agent
            facilitator: Facilitator for verification and settlement
        """
        self.merchant = merchant
        self.facilitator = facilitator
        self.utils = x402Utils()
        self.network = os.getenv("BSC_NETWORK", "bsc")
        print(f"🔧 BSC Executor initialized")
    
    async def sell_service(self, service_name: str) -> Dict[str, Any]:
        """
        Sell a service with BSC payment flow.
        
        Args:
            service_name: Name of the service to sell
            
        Returns:
            Service delivery result
        """
        print(f"\n{'='*60}")
        print(f"🏪 BSC Payment Flow Started")
        print(f"{'='*60}")
        print(f"Service: {service_name}")
        print(f"Network: {self.network}")
        
        try:
            # Try to sell service - this will raise payment exception
            result = await self.merchant.sell_service(service_name)
            return result
            
        except Exception as e:
            # Check if this is a payment required exception
            if hasattr(e, 'payment_requirements'):
                print("\n💳 Payment required - handling x402 flow")
                
                # In a real implementation, we would:
                # 1. Receive payment requirements from exception
                # 2. Wait for client to submit payment
                # 3. Verify payment with facilitator
                # 4. Settle payment on BSC
                # 5. Deliver service
                
                # For this demo, simulate the flow
                print("⏳ Waiting for client to submit payment...")
                
                # Simulate payment submission
                print("✅ Payment received")
                
                # Verify payment
                if self.facilitator:
                    verify_result = await self.facilitator.verify(
                        payment_payload={"mock": True},
                        payment_requirements={}
                    )
                    
                    if verify_result.is_valid:
                        print("✅ Payment verified")
                        
                        # Settle payment
                        settle_result = await self.facilitator.settle(
                            payment_payload={"mock": True},
                            payment_requirements={}
                        )
                        
                        if settle_result.success:
                            print(f"💰 Payment settled on {self.network}")
                            print(f"   TX: {settle_result.transaction}")
                            
                            # Deliver service
                            print("\n📦 Delivering service...")
                            return await self.merchant.deliver_service(service_name)
                        else:
                            return {
                                "status": "error",
                                "error": "Payment settlement failed"
                            }
                    else:
                        return {
                            "status": "error",
                            "error": "Payment verification failed"
                        }
                
                # Deliver service (mock facilitator always succeeds)
                print("\n📦 Delivering service...")
                return await self.merchant.deliver_service(service_name)
            else:
                # Re-raise other exceptions
                raise
    
    async def handle_payment_submitted(self, payment_payload: dict) -> Dict[str, Any]:
        """
        Handle payment submission from client.
        
        Args:
            payment_payload: Signed payment payload from client
            
        Returns:
            Processing result
        """
        print("\n📨 Processing payment submission...")
        
        # Verify payment
        verify_result = await self.facilitator.verify(
            payment_payload=payment_payload,
            payment_requirements={}
        )
        
        if verify_result.is_valid:
            # Settle payment
            settle_result = await self.facilitator.settle(
                payment_payload=payment_payload,
                payment_requirements={}
            )
            
            return {
                "status": "success" if settle_result.success else "failed",
                "transaction": settle_result.transaction,
                "network": settle_result.network
            }
        else:
            return {
                "status": "failed",
                "error": "Payment verification failed"
            }
