# Adding BNB (Binance Smart Chain) Support to A2A x402

This document explains how to configure and use BNB (Binance Smart Chain) payments with the A2A x402 extension.

## Changes Made

We've updated the following files to support BNB by default:

### Core Configuration Files
- `python/x402_a2a/types/config.py` - Default network changed from `"base"` to `"bsc"`
- `python/x402_a2a/core/merchant.py` - Default network changed to `"bsc"`
- `python/x402_a2a/core/helpers.py` - All helper functions now default to `"bsc"`

### Example Implementation
- `python/examples/adk-demo/server/agents/adk_merchant_agent.py` - Updated to use BSC network with USDC on BSC

## Using BNB in Your Implementation

### Basic Usage

```python
from x402_a2a import create_payment_requirements

# Create payment requirements for BNB network
requirements = create_payment_requirements(
    price="$10.00",  # $10 USDC
    pay_to_address="0xYourBSCWalletAddress",
    resource="/your-service",
    network="bsc",  # Binance Smart Chain
    description="Payment for service"
)
```

### Using Helper Functions

```python
from x402_a2a import require_payment

# Raise payment exception for BSC
raise require_payment(
    price="$5.00",
    pay_to_address="0xYourBSCWalletAddress",
    resource="/premium-feature",
    network="bsc",
    description="Premium feature access"
)
```

### Using Decorators

```python
from x402_a2a import paid_service

@paid_service(
    price="$2.00",
    pay_to_address="0xYourBSCWalletAddress",
    resource="/ai-service",
    network="bsc"
)
async def generate_content(prompt: str):
    return await ai_service.generate(prompt)
```

## BSC Network Configuration

### Important Addresses

**USDC on BSC (Binance Smart Chain):**
- Contract Address: `0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d`
- 18 decimals

**Other common tokens on BSC:**
- BUSD: `0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56`
- USDT: `0x55d398326f99059fF775485246999027B3197955`

### Network Identifiers

The x402 library expects the following network identifiers:
- **`bsc`** - Binance Smart Chain mainnet
- **`bsc-testnet`** - Binance Smart Chain testnet
- **`base`** - Base mainnet (for backward compatibility)
- **`base-sepolia`** - Base testnet

## Requirements

### Prerequisites

1. **x402 Library**: Ensure you're using a version of the x402 library that supports BSC
   - Check if `SupportedNetworks` includes `"bsc"` or `"bsc-mainnet"`

2. **Facilitator Configuration**: Your x402 facilitator must support BSC
   - Verify the facilitator can verify and settle payments on BSC
   - Configure the facilitator to use the correct RPC endpoint for BSC

3. **RPC Provider**: Set up an RPC provider for BSC
   ```python
   # Example using public RPC
   BSC_RPC = "https://bsc-dataseed1.binance.org/"
   # Or use a service like Infura/Alchemy
   BSC_RPC = "https://bsc-mainnet.g.alchemy.com/v2/YOUR_API_KEY"
   ```

## Testing

### Test on BSC Testnet

```python
from x402_a2a import create_payment_requirements

# Create test payment requirements
requirements = create_payment_requirements(
    price="$1.00",
    pay_to_address="0xYourTestWalletAddress",
    resource="/test-service",
    network="bsc-testnet",  # Use testnet for testing
    description="Test payment"
)
```

### Getting Test Tokens

1. Go to [BNB Chain Testnet Faucet](https://testnet.bnbchain.org/faucet-smart)
2. Connect your wallet
3. Request test BNB and test USDC

## Example: Complete Implementation

```python
from x402_a2a import (
    create_payment_requirements,
    x402PaymentRequiredException,
    x402Utils
)

class MyMerchantAgent:
    def __init__(self):
        self.wallet_address = "0xYourBSCWalletAddress"
        self.utils = x402Utils()
    
    async def handle_service_request(self, task):
        # Check if payment is required
        if self.is_premium_service(task):
            # Create payment requirements for BSC
            requirements = create_payment_requirements(
                price="$10.00",
                pay_to_address=self.wallet_address,
                resource="/premium-feature",
                network="bsc",
                description="Premium feature access",
                asset="0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d"  # USDC on BSC
            )
            
            # Raise payment exception
            raise x402PaymentRequiredException(
                message="Payment required for premium feature",
                payment_requirements=[requirements]
            )
        
        # Continue with normal processing
        return await self.process_service(task)
```

## Troubleshooting

### Issue: Network not supported
**Solution**: Ensure the x402 library version supports BSC. Check `SupportedNetworks` enum from `x402.types`.

### Issue: Facilitator fails to verify/settle
**Solution**: 
- Verify your facilitator is configured for BSC
- Check RPC endpoint is correct and accessible
- Ensure facilitator has access to BSC network

### Issue: Invalid asset address
**Solution**: 
- Use the correct token contract address for BSC
- Common addresses:
  - USDC: `0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d`
  - USDT: `0x55d398326f99059fF775485246999027B3197955`

## Additional Resources

- [BNB Chain Documentation](https://docs.bnbchain.org/)
- [BSC Token Contracts](https://www.bnbchain.org/en/token)
- [x402 Protocol Documentation](https://x402.gitbook.io/x402)
- [A2A Protocol Documentation](https://a2a-protocol.org/)

## Migration from Base to BSC

If you're migrating from Base to BSC:

1. **Update Network Parameter**: Change `network="base"` to `network="bsc"` throughout your code
2. **Update Asset Address**: Use BSC token addresses instead of Base addresses
3. **Update Facilitator**: Configure facilitator to use BSC RPC endpoint
4. **Update Wallet Address**: Use BSC-compatible wallet address

```python
# Before (Base)
requirements = create_payment_requirements(
    price="$10.00",
    pay_to_address="0x...",
    network="base",
    asset="0x833589fCD6eDb6E08f4c7C32D4f71b54bda02913"  # USDC on Base
)

# After (BSC)
requirements = create_payment_requirements(
    price="$10.00",
    pay_to_address="0x...",
    network="bsc",  # Changed to BSC
    asset="0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d"  # USDC on BSC
)
```
