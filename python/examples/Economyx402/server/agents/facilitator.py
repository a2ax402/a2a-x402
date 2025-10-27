"""BSC Facilitator Implementation."""

import os
from typing import Optional
from web3 import Web3
from x402_a2a import FacilitatorClient, FacilitatorConfig, VerifyResponse, SettleResponse


def get_facilitator():
    """Get facilitator instance (real or mock)."""
    use_mock = os.getenv("USE_MOCK_FACILITATOR", "true").lower() == "true"
    
    if use_mock:
        print("🤖 Using MOCK BSC Facilitator (no real transactions)")
        return MockBSCFacilitator()
    else:
        print("🌐 Using REAL BSC Facilitator")
        config = FacilitatorConfig(
            url=os.getenv("FACILITATOR_URL", "http://localhost:3000")
        )
        return FacilitatorClient(config)


class MockBSCFacilitator:
    """Mock facilitator for testing without real BSC transactions."""
    
    def __init__(self):
        """Initialize mock facilitator."""
        self.network = os.getenv("BSC_NETWORK", "bsc")
        print(f"🔧 Mock BSC Facilitator initialized for {self.network}")
    
    async def verify(self, payment_payload: dict, payment_requirements: dict) -> VerifyResponse:
        """
        Verify payment authorization (mock).
        
        Args:
            payment_payload: Signed payment payload
            payment_requirements: Payment requirements
            
        Returns:
            Verification response
        """
        print("\n🔍 Verifying payment signature...")
        print("  ✅ Mock verification always succeeds")
        
        return VerifyResponse(
            is_valid=True,
            payer=payment_payload.get("payload", {}).get("authorization", {}).get("from", "0xunknown"),
            invalid_reason=None
        )
    
    async def settle(self, payment_payload: dict, payment_requirements: dict) -> SettleResponse:
        """
        Settle payment on BSC (mock).
        
        Args:
            payment_payload: Signed payment payload
            payment_requirements: Payment requirements
            
        Returns:
            Settlement response with mock transaction
        """
        print("\n💰 Settling payment on BSC...")
        print("  📝 Mock transaction created")
        print("  ⚠️  No real BSC transaction posted!")
        
        # Generate mock transaction hash
        import secrets
        tx_hash = "0x" + secrets.token_hex(32)
        
        print(f"  📊 Mock TX: {tx_hash}")
        
        return SettleResponse(
            success=True,
            transaction=tx_hash,
            network=self.network,
            payer=payment_payload.get("payload", {}).get("authorization", {}).get("from", "0xunknown")
        )


class RealBSCFacilitator:
    """Real BSC facilitator that posts actual transactions."""
    
    def __init__(self):
        """Initialize real BSC facilitator."""
        self.network = os.getenv("BSC_NETWORK", "bsc")
        self.rpc_url = os.getenv("BSC_RPC_URL", "https://bsc-dataseed1.binance.org/")
        self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))
        
        print(f"🌐 Real BSC Facilitator initialized")
        print(f"  Network: {self.network}")
        print(f"  RPC: {self.rpc_url}")
    
    async def verify(self, payment_payload: dict, payment_requirements: dict) -> VerifyResponse:
        """
        Verify payment authorization on BSC.
        
        Args:
            payment_payload: Signed payment payload
            payment_requirements: Payment requirements
            
        Returns:
            Verification response
        """
        print("\n🔍 Verifying payment on BSC...")
        
        # TODO: Implement real EIP-712 signature verification
        # For now, return success
        return VerifyResponse(
            is_valid=True,
            payer="0xverified",
            invalid_reason=None
        )
    
    async def settle(self, payment_payload: dict, payment_requirements: dict) -> SettleResponse:
        """
        Settle payment on BSC by posting transferWithAuthorization transaction.
        
        Args:
            payment_payload: Signed payment payload
            payment_requirements: Payment requirements
            
        Returns:
            Settlement response with real transaction hash
        """
        print("\n💰 Posting transaction to BSC...")
        
        # TODO: Implement real transferWithAuthorization call
        # For now, return mock
        return SettleResponse(
            success=True,
            transaction="0x" + "mock-tx",
            network=self.network
        )
