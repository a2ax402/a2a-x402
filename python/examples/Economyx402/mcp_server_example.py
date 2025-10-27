"""
Minimal x402 MCP Server Example for BSC
"""

from x402_a2a import create_payment_requirements, require_payment
from typing import Dict, Any

def create_paid_mcp_handler(recipient_address: str):
    """
    Create a paid MCP handler for BSC.
    
    Example usage:
        handler = create_paid_mcp_handler("0xYourWallet")
        
        @handler.get_random_number(price=0.001)
        def get_random_number(min: int, max: int):
            return {
                "content": [{"type": "text", "text": str(random.randint(min, max))}]
            }
    """
    
    def paid_tool(tool_name: str, description: str, price: float, schema: Dict, handler):
        """Create a paid tool"""
        
        @require_payment(
            price=f"${price}",
            pay_to_address=recipient_address,
            resource=f"/{tool_name}",
            network="bsc",
            description=description
        )
        async def wrapper(*args, **kwargs):
            return await handler(*args, **kwargs)
        
        return wrapper
    
    return paid_tool


# Example: Minimal implementation
def minimal_paid_service():
    """Minimal paid service example"""
    
    from x402_a2a import create_payment_requirements
    
    # Simple payment requirement
    req = create_payment_requirements(
        price="$0.001",
        pay_to_address="0xYourWallet",
        resource="/get_random_number",
        network="bsc",
        description="Get random number service"
    )
    
    # Just raise the payment exception
    raise require_payment(
        price="$0.001",
        pay_to_address="0xYourWallet",
        resource="/service",
        network="bsc"
    )


# Usage in your service
if __name__ == "__main__":
    # Your handler gets called after payment
    def get_random_number(min: int, max: int):
        import random
        return {"number": random.randint(min, max)}
    
    # It's that simple!
    result = get_random_number(1, 100)
    print(f"Random number: {result}")
