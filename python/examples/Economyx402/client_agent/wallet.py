"""BSC Wallet Implementation for x402 payments."""

import os
from typing import Dict, Any
from eth_account import Account
from web3 import Web3
from x402_a2a import process_payment, PaymentRequirements, PaymentPayload


class BSCWallet:
    """Wallet for signing BSC payments using EIP-3009."""
    
    def __init__(self):
        """Initialize BSC wallet with private key."""
        self.private_key = os.getenv("PRIVATE_KEY", "0x" + "0" * 64)
        self.account = Account.from_key(self.private_key)
        self.network = os.getenv("BSC_NETWORK", "bsc")
        self.rpc_url = os.getenv("BSC_RPC_URL", "https://bsc-dataseed1.binance.org/")
        
        # Initialize Web3 connection
        self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))
        
        print(f"💼 Wallet initialized")
        print(f"  Address: {self.account.address}")
        print(f"  Network: {self.network}")
    
    async def sign_payment(self, payment_requirements: Dict[str, Any]) -> PaymentPayload:
        """
        Sign payment requirements using EIP-3009 authorization.
        
        Args:
            payment_requirements: Payment requirements from merchant
            
        Returns:
            Signed payment payload
        """
        print("\n🔐 Signing payment with BSC wallet...")
        print(f"  Amount: {payment_requirements.get('maxAmountRequired')}")
        print(f"  To: {payment_requirements.get('payTo')}")
        
        # Convert dict to PaymentRequirements object
        requirement = PaymentRequirements(**payment_requirements)
        
        # Sign the payment using x402_a2a library
        # This creates an EIP-3009 authorization signature
        payment_payload = process_payment(
            requirements=requirement,
            account=self.account
        )
        
        print("✅ Payment signed successfully")
        print(f"  Authorization from: {payment_payload.payload.authorization.from_}")
        print(f"  Nonce: {payment_payload.payload.authorization.nonce}")
        
        return payment_payload
    
    async def get_balance(self, token_address: str = None) -> str:
        """
        Get balance of BNB or ERC-20 token.
        
        Args:
            token_address: Token contract address (None for BNB)
            
        Returns:
            Balance as string
        """
        if token_address:
            # ERC-20 token balance
            contract = self.w3.eth.contract(
                address=Web3.to_checksum_address(token_address),
                abi=self._get_erc20_abi()
            )
            balance = contract.functions.balanceOf(self.account.address).call()
            decimals = contract.functions.decimals().call()
            balance_eth = balance / (10 ** decimals)
            return str(balance_eth)
        else:
            # BNB balance
            balance_wei = self.w3.eth.get_balance(self.account.address)
            balance_eth = Web3.from_wei(balance_wei, 'ether')
            return str(balance_eth)
    
    def _get_erc20_abi(self):
        """Standard ERC-20 ABI."""
        return [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "type": "function"
            },
            {
                "constant": True,
                "inputs": [],
                "name": "decimals",
                "outputs": [{"name": "", "type": "uint8"}],
                "type": "function"
            }
        ]


class MockBSCWallet:
    """Mock wallet for testing without real transactions."""
    
    def __init__(self):
        """Initialize mock wallet."""
        self.network = os.getenv("BSC_NETWORK", "bsc")
        print(f"💼 Mock BSC Wallet initialized (network: {self.network})")
    
    async def sign_payment(self, payment_requirements: Dict[str, Any]) -> Dict[str, Any]:
        """Mock signing - returns a dummy signature."""
        print("\n🔐 Mock signing payment...")
        print("⚠️  WARNING: This is a MOCK wallet - no real signature!")
        
        return {
            "x402Version": 1,
            "scheme": "exact",
            "network": self.network,
            "payload": {
                "signature": "0x" + "f" * 130,
                "authorization": {
                    "from": "0x" + "1" * 40,
                    "to": payment_requirements.get("payTo"),
                    "value": payment_requirements.get("maxAmountRequired"),
                    "validAfter": "0",
                    "validBefore": "9999999999",
                    "nonce": "0x" + "a" * 64
                }
            }
        }
