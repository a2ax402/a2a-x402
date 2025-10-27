# Minimal x402 Implementation for BSC

## Simplest Possible Code

```python
from x402_a2a import require_payment

# Just decorate your function
@require_payment(
    price="$0.001",
    pay_to_address="0xYourWallet",
    network="bsc"
)
def get_random_number(min: int, max: int):
    return {"number": random.randint(min, max)}
```

## That's It!

Your service automatically:
- ✅ Requires payment before running
- ✅ Accepts BSC payments
- ✅ Handles all payment logic
- ✅ Returns service result after payment

## Full Integration

```python
from x402_a2a import require_payment
import random

class MyService:
    def __init__(self, wallet_address: str):
        self.wallet = wallet_address
    
    @require_payment(
        price="$0.001",
        pay_to_address=self.wallet,
        network="bsc",
        resource="/get_random"
    )
    def get_random(self, min: int, max: int):
        """Get random number - requires BSC payment first"""
        return {"number": random.randint(min, max), "status": "paid"}
```

## For MCP Servers

```python
from x402_a2a import paid_service

@paid_service(
    price="$0.001",
    pay_to_address="0x123...",
    network="bsc"
)
def get_random_number(min: int, max: int):
    return random.randint(min, max)
```

That's the minimal code! 🎉
